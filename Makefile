# ----------------------------------------------------

GCC	= gcc
WCC	= x86_64-w64-mingw32-gcc
LFL	= ./launcher/linux/*.c
WFL	= ./launcher/windows/*.c
LFLGS	= -O2 -DNDEBUG -s
LSYS	= -DCOMPILE_MODE=1
NAME	= InvaderClone

# ----------------------------------------------------

portable_linux:
	$(GCC) $(LFL) -o $(NAME)

system_linux:
	$(GCC) $(LFL) -o $(NAME) $(LSYS)

windows:
	 $(WCC) $(WFL) -o $(NAME).exe

clean:
	rm -rf ./data/env
	rm "InvaderClone"
	rm "InvaderClone.exe"
