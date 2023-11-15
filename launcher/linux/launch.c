#include <stdio.h>
#include <dirent.h>
#include <errno.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#include "manylinuxnotify.h"

#define COMMANDBUFFER 1024

#define OPENENVFAILED -2
#define PYTHONNOTFOUND -3
#define COULDNOTOPENPROCCESS -4

// 0 = portable
// 1 = system
#ifndef COMPILE_MODE
#define COMPILE_MODE 0
#endif


int main(int argc, char** argv)
{

#if COMPILE_MODE == 1
	DIR* systemDir = opendir("/opt/invaderclone/");
	if (!systemDir)
	{
		mkdir("/opt/invaderclone/", S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
	}
	closedir(systemDir);

	DIR* dir = opendir("/opt/invaderclone/data/env/");

#elif COMPILE_MODE == 0
	DIR* dir = opendir("./data/env/");
#endif

	// Check if dir "./data/env/" exists.
	if (dir)
	{
		// If exists, the program simply needs to be launched
		printf("The python virtual env exists. Launching the program.");
		closedir(dir);
	}
	else if (ENOENT == errno)
	{
		closedir(dir);

		int answer = manylinuxNotify("Confirm Operation", "In order to run the game, some python requirements need to be downloaded.\nMake sure you are both connected to the internet, and okay with this.\nIf you are okay with the requirements being downloaded, hit \"yes.\"\n", true);

		fflush(stdout);

		if (answer == -1)
		{
			fprintf(stderr, "ERROR: You don't have any graphical dialog box applications installed on your machine. In order to run this version of the game, you should install kdialog, yad, or zenity.\nYou can also install this game using pip, or, if available, on your system repository.\n");
			return -1;
		}
		else if (answer == 0)
		{
			printf("You chose not to download the dependencies for the game. You can also install this game using pip, or, if available, on your system repository.\n");
			return 0;
		}

		// Ask the user if it's ok to download a python virtual env.

		// Notify the user that a virtual env needs to be made.
		manylinuxNotify("No Virtual Environment", "A Python Virtual Environment is being created. Please wait up to a few minutes.", false);

		bool py3 = !access("/bin/python3", F_OK) || !access("/usr/bin/python3", F_OK);

		// Check if python3 was found on the system, and notify the user + exit if not.
		if (!py3)
		{
			manylinuxNotify("ERROR", "Python could not be found. Is it installed on your system?", false);
			return PYTHONNOTFOUND;
		}

#if COMPILE_MODE == 0
		char command[COMMANDBUFFER] = "python3 -m venv ./data/env";
		char pipcmd[COMMANDBUFFER] = "./data/env/bin/python -m pip install -r ./data/requirements.txt";
#elif COMPILE_MODE == 1
		char command[COMMANDBUFFER] = "python3 -m venv /opt/invaderclone/data/env";
		char pipcmd[COMMANDBUFFER] = "/opt/invaderclone/data/env/bin/python -m pip install -r /opt/invaderclone/data/requirements.txt";
#endif

		FILE* python = popen(command, "w");

		// Check if python3 could be launched, and notify the user + exit if not.
		if (!python)
		{
			manylinuxNotify("ERROR", "Could not open Python process. Check your privelages?", false);
			return COULDNOTOPENPROCCESS;
		}

		pclose(python);

		FILE* pip = popen(pipcmd, "w");

		// Check if pip could be launched, and notify the user + exit if not.
		if (!pip)
		{
			manylinuxNotify("ERROR", "Could not open Python pip. Is pip installed?", false);
			return COULDNOTOPENPROCCESS;
		}

		pclose(pip);

	}
	else {
		closedir(dir);

		// Check if python virtual env could be launched, and notify the user + exit if not.
		manylinuxNotify("ERROR", "Failed to open the python virtual env. You may not have permissions to this folder.", false);
		return OPENENVFAILED;
	}

	fflush(stdout);


	// Launch the program from the virtual env that was created.
#if COMPILE_MODE == 0
	int cliLen = 41;
	for (int i = 1; i < argc; ++i)
	{
		cliLen += strlen(argv[i]) + 1;
	}

	char command[cliLen];

	char commandStart[] = "./data/env/bin/python ./data/invaders.py";
	for (int i = 0; i < strlen(commandStart); ++i)
	{
		command[i] = commandStart[i];
	}

	int seek = 40;

	for (int i = 1; i < argc; ++i)
	{
		command[seek] = ' ';
		++seek;

		for (int j = 0; j < strlen(argv[i]); ++j)
		{
			command[seek] = argv[i][j];
			++seek;
		}
	}

	command[seek] = '\0';


	FILE* proccess = popen(command, "w");
#elif COMPILE_MODE == 1
	int cliLen = 73;
	for (int i = 1; i < argc; ++i)
	{
		cliLen += strlen(argv[i]) + 1;
	}

	char command[cliLen];

	char commandStart[] = "/opt/invaderclone/data/env/bin/python /opt/invaderclone/data/invaders.py";
	for (int i = 0; i < strlen(commandStart); ++i)
	{
		command[i] = commandStart[i];
	}

	int seek = 72;

	for (int i = 1; i < argc; ++i)
	{
		command[seek] = ' ';
		++seek;

		for (int j = 0; j < strlen(argv[i]); ++j)
		{
			command[seek] = argv[i][j];
			++seek;
		}
	}

	command[seek] = '\0';


	FILE* proccess = popen(command, "w");
#endif


	// Check if the process could be created, and notify the user if not.
	if (!proccess)
	{
		manylinuxNotify("ERROR", "Could not launch the game. Did you modify the data directory? You can delete the \"env\" directory to reinstall all requirements.", false);
		return COULDNOTOPENPROCCESS;
	}

	// Wait for the game to close.
	return pclose(proccess);
}