#include "utils.h"

char* CreateCommandString(const char* base, int argc, char** argv)
{
	int cliCmdLen = strlen(base) + 1; // This should cover every single token, injected parenthesis when needed, and the basic str above.
	int seek = cliCmdLen - 1;

	bool encounteredSwitch = false;
	bool nextHasSwitchOrIsEnd = false;
	bool lastHasSwitch = true;
	bool switchMode = false;
	for (int i = 1; i < argc; ++i)
	{
		encounteredSwitch = argv[i][0] == '-';
		lastHasSwitch = argv[i-1][0] == '-';
		nextHasSwitchOrIsEnd = i == argc - 1 || argv[i+1][0] == '-';

		if (encounteredSwitch && !nextHasSwitchOrIsEnd)
		{
			switchMode = true;
		}

		if (switchMode && lastHasSwitch)
		{
			++cliCmdLen;
		}

		if (switchMode && nextHasSwitchOrIsEnd)
		{
			++cliCmdLen;
			switchMode = false;
		}


		cliCmdLen += strlen(argv[i]) + 1;
	}

	char* command = malloc(sizeof(char) * cliCmdLen);
	memset(command, '\0', cliCmdLen);

	for (int i = 0; i < strlen(base); ++i)
	{
		command[i] = base[i];
	}


	encounteredSwitch = false;
	nextHasSwitchOrIsEnd = false;
	lastHasSwitch = true;
	switchMode = false;
	for (int i = 1; i < argc; ++i)
	{
		command[seek] = ' ';
		++seek;

		encounteredSwitch = argv[i][0] == '-';
		lastHasSwitch = argv[i-1][0] == '-';
		nextHasSwitchOrIsEnd = i == argc - 1 || argv[i+1][0] == '-';

		if (encounteredSwitch && !nextHasSwitchOrIsEnd)
		{
			switchMode = true;
		}

		if (switchMode && lastHasSwitch)
		{
			command[seek] = '\"';
			++seek;
		}

		for (int j = 0; j < strlen(argv[i]); ++j)
		{
			command[seek] = argv[i][j];
			++seek;
		}

		if (switchMode && nextHasSwitchOrIsEnd)
		{
			command[seek] = '\"';
			++seek;
			switchMode = false;
		}

	}

	command[seek] = '\0';

	return command;
}
