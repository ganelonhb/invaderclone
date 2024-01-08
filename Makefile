# ----------------------------------------------------

GCC	= gcc
WCC	= x86_64-w64-mingw32-gcc
LFL	= ./launcher/linux/*.c
WFL	= ./launcher/windows/*.c
WRC	= ./launcher/windows/*.res
LFLGS	= -O3 -DNDEBUG -Wall
WFLGS	= -O3 -DNDEBUG -s -Wall -mwindows
NAME	= InvaderClone

# ----------------------------------------------------

linux:
	$(GCC) $(LFL) $(LFLGS) -o $(NAME)

windows:
	 $(WCC) $(WFL) $(WRC) $(WFLGS) -o $(NAME).exe

debug_make_to_vm:
	$(WCC) $(WFL) $(WRC) $(WFLGS) -o /home/donquixote/VMs/windows/$(NAME).exe

clean:
	rm -rf ./data/env
	rm -rf ./data/videogame/__pycache__
	rm -rf ./data/videogame/videogame.egg-info
	rm "InvaderClone"
	rm "InvaderClone.exe"
