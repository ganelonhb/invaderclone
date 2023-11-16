#include "win32findenv.h"

bool win32FindEnv(const char* execDir)
{
    // First, we construct a search string that is the concatenation of execDir and \data\env
    char relativeEnv[11] = "\\data\\env\\\0";

    int execDirStrLen = strlen(execDir);

    int startIdx = (execDir[execDirStrLen - 1] == '\\') ? 1 : 0;
    int searchStrLen = execDirStrLen + 11 - startIdx;
    int nBytes = (searchStrLen) * sizeof(char);
    char* searchStr = (char*)calloc(nBytes);

    for (int i = 0; i < execDirStrLen; ++i)
    {
        searchStr[i] = execDir[i];
    }

    int relativeIdx = startIdx;
    for (int j = execDirStrLen; j < searchStrLen; ++j )
    {
        searchStr[j] = relativeEnv[relativeIdx];
        ++relativeIdx;
    }

    // Now, we use the Windows API to find the file.

    WIN32_FIND_DATA dummy;
    HANDLE fileHandle = FindFirstFile(
        searchStr,
        &dummy
    );

    DWORD lastError = GetLastError();

    FindClose(fileHandle);

    free(searchStr);

    // Return the status of ERROR_FILE_NOT_FOUND
    return lastError != ERROR_FILE_NOT_FOUND;
}
