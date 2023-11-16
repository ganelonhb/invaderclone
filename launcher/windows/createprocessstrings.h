#ifndef CREATEPROCESSSTRINGS_H
#define CREATEPROCESSSTRINGS_H

#include <string.h>
#include <stdlib.h>

char* createVenvStr();
char* installDepsStr();
char* execStr(int argv, char** argc);

#endif
