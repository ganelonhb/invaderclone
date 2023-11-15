#ifndef WIN32FINDENV_H
#define WIN32FINDENV_H

#include <windows.h>
#include <fileapi.h>
#include <stdbool.h>
#include <errhandlingapi.h>
#include <string.h>

// Given the dir of the executable, we search for the env folder.
bool win32FindEnv(const char* execDir);

#endif
