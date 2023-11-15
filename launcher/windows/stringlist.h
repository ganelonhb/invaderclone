#ifndef STRINGLIST_H
#define STRINGLIST_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Typedefs
typedef char** stringlist_t;

// Forward declaration
stringlist_t splitString(const char* str, char delim);
int strlistlen(stringlist_t str);
void freeStringList(stringlist_t list);

#endif
