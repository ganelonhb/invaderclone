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
#include "utils.h"

#define COMMANDBUFFER (DWORD)1024
#define PATHBUFFER (DWORD)2048
#define FILENAMEBUFFER (DWORD)2048

#define OPENENVFAILED -2
#define PYTHONNOTFOUND -3
#define COULDNOTOPENPROCCESS -4

#define UNICODE 1
#define __unused__(x) (void)(x)

int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPTSTR lpCmdLine, int cmdShow) {
    //construct a string to execute the creation of an env
    if (!fileExists("gamedata\\env\\Scripts\\python.exe"))
    {
        char execDir[FILENAMEBUFFER] = { 0 };

        DWORD returnGetModuleFileName = GetModuleFileName(
            NULL,
            execDir,
            FILENAMEBUFFER
        );
        __unused__(returnGetModuleFileName);

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
        __unused__(retGetPath);

        stringlist_t path = splitString(PATH, ';');

        char* pythonPath = win32FindPython(path);

        if (pythonPath != NULL)
        {
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
                    int mbGoodBye = MessageBox(
                        NULL,
                        "You have selected to quit the app. You can manually install the dependencies using the Python Pip package manager by navigating to the \"data\" directory bundled with this executable, then typing the following commands.\n\npython -m venv env\nenv\\Scripts\\activate\npython -m pip install -r requirements.txt\ndeactivate\n\nGoodbye!\n",
                        "Consent Not Granted! Sorry :(",
                        MB_OK | MB_ICONEXCLAMATION
                    );
                    __unused__(mbGoodBye);
                    freeStringList(path);
                    free(pythonPath);

                    return 0;
                }

            }
            freeStringList(path);
            free(pythonPath);
        }
        else
        {
            int mbErr = MessageBox(
                NULL,
                "Python could not be found. If it is installed on your system, make sure your PATH variable points to it. If not, please install it!",
                "ERROR",
                MB_OK | MB_ICONEXCLAMATION
            );
            __unused__(mbErr);

            freeStringList(path);
            return -1;
        }

        freeStringList(path);

        DWORD err = Win32ApiCreateProcess("python -m venv gamedata\\env");
        if (!err)
            return err;

        int mbInst = MessageBox(
            NULL,
            "The dependencies will be installed into your environment. Please wait a few minutes.",
            "Installing... Please Wait",
            MB_OK | MB_ICONQUESTION
        );
        __unused__(mbInst);
    }

    DWORD err = Win32ApiCreateProcess("gamedata\\env\\Scripts\\python.exe -m pip install --upgrade pip invaderclone");

    char* command = CreateCommandString("gamedata\\env\\Scripts\\python.exe -m invaders", lpCmdLine);

    err = Win32ApiCreateProcess(command);

    free(command);

    if (err)
        return err;

    return 0;
}
