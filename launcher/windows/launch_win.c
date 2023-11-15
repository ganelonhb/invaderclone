#include <stdio.h>
#include <dirent.h>
#include <errno.h>
#include <unistd.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#include <windows.h>

#include <fileapi.h>
#include <libloaderapi.h>
#include <winbase.h>
#include <winuser.h>

#include "stringlist.h"
#include "win32findpython.h"
#include "win32findenv.h"

#define COMMANDBUFFER (DWORD)1024
#define PATHBUFFER (DWORD)2048
#define FILENAMEBUFFER (DWORD)2048

#define OPENENVFAILED -2
#define PYTHONNOTFOUND -3
#define COULDNOTOPENPROCCESS -4


int main(int argc, char** argv) {

    // Get the location of the executable. This will be used to locate the data and env dirs.
    char execDir[FILENAMEBUFFER] = { 0 };

    DWORD returnGetModuleFileName = GetModuleFileName(
        NULL,
        execDir,
        FILENAMEBUFFER
    );

    for (int i = FILENAMEBUFFER - 1; i >= 0; --i){
        if (execDir[i] == '\\')
            break;

        execDir[i] = '\0';
    }

    // Check if Python is installed on the machine.
    char PATH[PATHBUFFER] = { 0 };

    DWORD retGetPath = GetEnvironmentVariable(
        "PATH",
        PATH,
        PATHBUFFER
    );

    stringlist_t path = splitString(PATH, ';');

    char* pythonPath = win32FindPython(path);

    if (pythonPath != NULL)
    {
        printf("\nFOUND: %s\n", pythonPath);

        // Find the data\env dir.
        bool envNotFound = win32FindEnv(execDir);

        if (envNotFound)
        {
            // Ask the user if they want to install the requirements
            int mbOkayToInstall = MessageBox(
                NULL,
                "This game requires dependencies to be downloaded from the internet. Please ensure that:\n    1) You are okay with this.\n    2) You have a stable internet connection to complete this task.\nIf you would like to download the requirements for this game, select \"Yes.\" If you select \"No,\" the app will quit.",
                "Consent Required",
                MB_YESNO | MB_ICONQUESTION | MB_DEFBUTTON2
            );

            if (mbOkayToInstall == IDNO)
            {
                printf("You have selected to quit the app. You can manually install the dependencies using the Python Pip package manager by navigating to the \"data\" directory bundled with this executable, then typing the following commands.\n\npython -m venv env\nenv\\Scripts\\activate\npython -m pip install -r requirements.txt\ndeactivate\n\nGoodbye!\n");

                return 0;
            }
        }

        free(pythonPath);
    }
    else
    {
        printf("ERROR: Python could not be found. If it is installed on your system, make sure your PATH variable points to it. If not, please install it!");
        int mbErr = MessageBox(
            NULL,
            "Python could not be found. If it is installed on your system, make sure your PATH variable points to it. If not, please install it!",
            "ERROR",
            MB_OK | MB_ICONEXCLAMATION
        );
    }


    freeStringList(path);

    // If Python is not installed, notify the user and exit.

    return 0;
}
