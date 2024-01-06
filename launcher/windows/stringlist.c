#include "stringlist.h"

stringlist_t splitString(const char* str, char delim)
{
    // Find the number of paths, and the lengths of the strings in those paths.
    int count = 0;
    int currentStrCount = 0;
    int stringlistCounts[2048] = { 0 };

    for (int i = 0; i < strlen(str); ++i)
    {
        if (str[i] == delim)
        {
            if (currentStrCount > 0){
                stringlistCounts[count] = currentStrCount + 1;
                ++count;
            }

            currentStrCount = 0;
        }

        if (i == strlen(str) - 1 && str[i] != delim)
        {
            stringlistCounts[count] = currentStrCount + 1;
            ++count;
        }

        ++currentStrCount;
    }

    // Return a null pointer if no paths were found.
    if (!count)
    {
        return NULL;
    }

    // Create space for the stringlist and its strings.
    char** stringlist = (char**)malloc((count + 1) * sizeof(char*));
    stringlist[count] = NULL;

    for (int j = 0; j < count; ++j)
    {
        stringlist[j] = (char*)malloc(stringlistCounts[j] * sizeof(char*));
    }

    // Now, we need to copy each string into the string list at each index.
    count = 0;
    currentStrCount = 0;

    for(int seek = 0; seek < strlen(str); ++seek)
    {
        if (str[seek] == delim && currentStrCount > 0)
        {
            ++count;
            currentStrCount = 0;
        }
        else
        {
            stringlist[count][currentStrCount] = str[seek];
            ++currentStrCount;
        }
    }

    return stringlist;
}

int strlistlen(stringlist_t str)
{
    int length = 0;

    for(int i = 0; str[i] != NULL; ++i)
    {
        ++length;
    }

    return length;
}

void freeStringList(stringlist_t list)
{
    // Loop through the strings until we find a pointer that is null.

    for (int i = 0;;++i)
    {
        if (list[i] == NULL)
        {
            break;
        }

        free(list[i]);
    }

    // Free the list itself.
    free(list);

    // Set the list to NULL in case any other program checks for this.
    list = NULL;
}
