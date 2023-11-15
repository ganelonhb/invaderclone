#ifndef MANYLINUXNOTIFY_H
#define MANYLINUXNOTIFY_H

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// manylinuxNotify will try and find one of the many popular dialog box notification systems
// on the user's machine to display a gui notification with the given title and body text.
int manylinuxNotify(const char*, const char*, bool);

#endif
