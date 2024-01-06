#include <stdio.h>
#include <dirent.h>
#include <errno.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#include "manylinuxnotify.h"
#include "utils.h"

#define COMMANDBUFFER 1024

#define OPENENVFAILED -2
#define PYTHONNOTFOUND -3
#define COULDNOTOPENPROCCESS -4


int main(int argc, char** argv)
{

	DIR* dir = opendir("./gamedata/env/");

	// Check if dir "./data/env/" exists.
	if (dir)
	{
		// If exists, the program simply needs to be launched
		//printf("The python virtual env exists. Launching the program.");
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

		char command[COMMANDBUFFER] = "python3 -m venv ./gamedata/env";
		char pipcmd[COMMANDBUFFER] = "./gamedata/env/bin/python -m pip install invaderclone";

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

	// Try to update invaderclone.

	char updcmd[COMMANDBUFFER] = "./gamedata/env/bin/python3 -m pip install --quiet --upgrade pip invaderclone";

	FILE* updoot = popen(updcmd, "w");

	// does not need to check if update failed. At this point, a failure to update means there is no new version.

	pclose(updoot);

	fflush(stdout);


	// Launch the program from the virtual env that was created.

	char* command = CreateCommandString("./gamedata/env/bin/python3 -m invaders", argc, argv);

	FILE* proccess = popen(command, "w");

	free(command);

	// Check if the process could be created, and notify the user if not.
	if (!proccess)
	{
		manylinuxNotify("ERROR", "Could not launch the game. Did you modify the data directory? You can delete the \"env\" directory to reinstall all requirements.", false);
		return COULDNOTOPENPROCCESS;
	}

	// Wait for the game to close.
	return pclose(proccess);
}
