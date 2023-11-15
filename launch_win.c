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

#define COMMANDBUFFER (DWORD)128
#define PATHBUFFER (DWORD)2048
#define FILENAMEBUFFER (DWORD)2048

#define OPENENVFAILED -2
#define PYTHONNOTFOUND -3
#define COULDNOTOPENPROCCESS -4

// Typedefs
typedef char** stringlist_t;

// Forward declaration
stringlist_t splitString(const char* str, char delim);
void freeStringList(stringlist_t list);

// WinFindPython finds the path to Python.exe given a list of paths.
char* win32FindPython(stringlist_t list);

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

    printf("%s", PATH);

    // If Python is not installed, notify the user and exit.

    return 0;
}

stringlist_t splitString(const char* str, char delim)
{
    //
    int count = 0;
    int currentStrCount = 0;

    for (int i = 0; i < strlen(str); ++i)
    {
        if (str[i] == delim)
        {
            if (currentStrCount > 0){
                ++count;
            }
        }

        if (i == strlen(str) - 1 && str[i] != delim)
        {
            ++count;
        }
    }

    if (!count)
    {
        return NULL;
    }

    char** stringlist = (char**)malloc((count + 1) * sizeof(char*));
    int* stringlistCounts = (int*)malloc(count * sizeof(int));
    stringlist[count] = NULL;



}
