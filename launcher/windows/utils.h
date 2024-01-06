#ifndef UTILS_H
#define UTILS_H

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#include <windows.h>

#include <fileapi.h>
#include <winbase.h>
#include <winuser.h>

#define UNICODE 1

bool fileExists(const LPCSTR str);
DWORD Win32ApiCreateProcess(const LPSTR str);
LPTSTR CreateCommandString(const LPTSTR base, LPTSTR cmd);

#endif
