#ifndef WIN32FINDPYTHON_H
#define WIN32FINDPYTHON_H

#include <windows.h>
#include <fileapi.h>
#include <stdbool.h>
#include <string.h>
#include <errhandlingapi.h>

#include "stringlist.h"

// WinFindPython finds the path to Python.exe given a list of paths.
char* win32FindPython(stringlist_t list);

#endif
