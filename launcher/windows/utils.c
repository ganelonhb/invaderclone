#include "utils.h"

bool fileExists(LPCSTR str)
{
    DWORD attributes = GetFileAttributes(str);

    return (attributes != INVALID_FILE_ATTRIBUTES
        && !(attributes & FILE_ATTRIBUTE_DIRECTORY));
}

DWORD Win32ApiCreateProcess(const LPSTR str)
{
    STARTUPINFO startupInfo;
    PROCESS_INFORMATION processInfo;

    ZeroMemory(&startupInfo, sizeof(STARTUPINFO));
    startupInfo.cb = sizeof(STARTUPINFO);
	startupInfo.dwFlags = STARTF_USESHOWWINDOW;
	startupInfo.wShowWindow = SW_HIDE;
    ZeroMemory(&processInfo, sizeof(PROCESS_INFORMATION));

	CreateProcess(
		NULL,
		str,
		NULL,
		NULL,
		FALSE,
		0,
		NULL,
		NULL,
		&startupInfo,
		&processInfo
	);

    WaitForSingleObject(processInfo.hProcess, INFINITE);

    CloseHandle(processInfo.hProcess);
    CloseHandle(processInfo.hThread);

    return GetLastError();
}

LPTSTR CreateCommandString(const LPTSTR base, LPTSTR command)
{
	int cliCmdLen = lstrlen(base) + 2; // This should cover every single token, injected parenthesis when needed, and the basic str above.

	bool encounteredWhiteSpace = false;
	for (int i = 0; i < lstrlen(command); ++i)
	{
		++cliCmdLen;
		encounteredWhiteSpace = false;
		if (
			command[i] == (TCHAR)'-'
			&& command[i+1] != (TCHAR)'-'
		)
		{
			for (int j = i+1; j < lstrlen(command); ++j)
			{
				if (command[j] == (TCHAR)' ' || command[j] == (TCHAR)'\t')
				{
					encounteredWhiteSpace = true;
				}

				if (encounteredWhiteSpace && command[j] != (TCHAR)'-')
				{
					cliCmdLen += 2;
					break;
				}
				else if (command[j] == (TCHAR)'-')
				{
					break;
				}
			}
		}
	}

	int seek = 0;
	LPTSTR returnValue = malloc(sizeof(TCHAR) * cliCmdLen);
	memset(returnValue, 0, sizeof(TCHAR) * cliCmdLen);
	for (int i = 0; i < lstrlen(base); ++i){
		returnValue[i] = (TCHAR)base[i];
		++seek;
	}

	returnValue[seek] = (TCHAR)' ';
	++seek;

	encounteredWhiteSpace = false;
	bool encounteredValuedSwitch = false;
	bool placedFirstParenthesis = false;
	for (int i = 0; i < lstrlen(command); ++i)
	{
		encounteredWhiteSpace = false;
		if (
			command[i] == (TCHAR)'-'
			&& command[i+1] != (TCHAR)'-'
		)
		{
			for (int j = i+1; j < lstrlen(command); ++j)
			{
				if (command[j] == (TCHAR)' ' || command[j] == (TCHAR)'\t')
					encounteredWhiteSpace = true;

				if (encounteredWhiteSpace && command[j] != (TCHAR)'-')
				{
					encounteredValuedSwitch = true;
					break;
				}
				else if (command[j] == (TCHAR)'-')
				{
					break;
				}
			}
		}

		returnValue[seek] = (TCHAR)command[i];
		++seek;

		if (encounteredValuedSwitch
			&& !placedFirstParenthesis
			&& (command[i] == (TCHAR)' ' || command[i] == (TCHAR)'\t')
			&& (command[i+1] != (TCHAR)' ' && command[i+1] != (TCHAR)'\t')
		)
		{
			placedFirstParenthesis = true;
			returnValue[seek] = (TCHAR)'\"';
			++seek;
		}

		if (encounteredValuedSwitch
			&& placedFirstParenthesis
			&& (command[i+1] == (TCHAR)' ' || command[i+1] == (TCHAR)'\t')
		)
		{
			bool nextTokenIsSwitchOrEnd = true;
			for (int j = i + 1; j < lstrlen(command); ++j)
			{
				if (command[j] == (TCHAR)'-')
					break;

				if (command[j] != (TCHAR)' ' && command[j] != (TCHAR)'\t')
				{
					nextTokenIsSwitchOrEnd = false;
				}
			}

			if (nextTokenIsSwitchOrEnd)
			{
				returnValue[seek] = (TCHAR)'\"';
				++seek;

				encounteredValuedSwitch = false;
				placedFirstParenthesis = false;
			}
		}
	}

	if (encounteredValuedSwitch)
	{
		returnValue[seek] = (TCHAR)'\"';
		++seek;
	}
	returnValue[seek] = (TCHAR)'\0';

	return returnValue;
}
