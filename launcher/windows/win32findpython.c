#include "win32findpython.h"

char* win32FindPython(stringlist_t list)
{
    int listLength = strlistlen(list);

    if (!listLength)
    {
        return NULL;
    }

    // Essentially, we construct a string that includes a path retrieved by the string list
    // combined with \Python.exe then use the windows API to search for that file.
    // If it can be found, then we return the string. Else, we return NULL.
    for (int i = 0; i < listLength; ++i)
    {
        WIN32_FIND_DATA dummy;

        int strLen = strlen(list[i]);

        int lastCharDelim = list[i][strLen - 1] == '\\' ? 12 : 11;
        int numberBytes = (strLen + lastCharDelim) * sizeof(char);
        char* str = (char*)malloc(numberBytes);
        memset(str, '\0', numberBytes);

        for (int j = 0; j < strLen; ++j)
        {
            str[j] = list[i][j];
        }

        char python[12] = "\\Python.exe\0";

        int p = list[i][strLen - 1] == '\\' ? 0 : 1;
        for (int k = strLen; k < strLen + lastCharDelim - 1; ++k)
        {
            str[k] = python[p];
            ++p;
        }

        printf("%s\n", str);

        HANDLE fileHandle = FindFirstFileA(
            str,
            &dummy
        );

        DWORD lastError = GetLastError();

        FindClose(fileHandle);

        if (lastError != ERROR_FILE_NOT_FOUND)
        {
            return str;
        }

        free(str);
    }

    return NULL;
}
