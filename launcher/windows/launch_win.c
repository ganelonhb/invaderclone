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

#include "stringlist.h"
#include "win32findpython.h"

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

    for (int i = 0; path[i] != NULL; ++i)
    {
        printf("%s\n", path[i]);
    }
    printf("%s", PATH);

    freeStringList(path);

    // If Python is not installed, notify the user and exit.

    return 0;
}
