#ifndef CREATEPROCESSSTRINGS_H
#define CREATEPROCESSSTRINGS_H

#include <string.h>
#include <stdlib.h>

int createVenv(char* pydir, char* venvdir);
int installDeps(char* venvpydir);
int exec(char* venvdir,int argv, char** argc);

#endif
