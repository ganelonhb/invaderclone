# ----------------------------------------------------

GCC	= gcc
WCC	= x86_64-w64-mingw32-gcc
LFL	= ./launcher/linux/*.c
WFL	= ./launcher/windows/*.c
LFLGS	= -O2 -DNDEBUG -s
NAME	= InvaderClone

# ----------------------------------------------------

linux:
	$(GCC) $(LFL) -o $(NAME)

windows:
	 $(WCC) $(WFL) -o $(NAME).exe

debug_make_to_vm:
	$(WCC) $(WFL) -o /home/donquixote/VMs/windows/$(NAME).exe

clean:
	rm -rf ./data/env
	rm -rf ./data/videogame/__pycache__
	rm -rf ./data/videogame/videogame.egg-info
	rm "InvaderClone"
	rm "InvaderClone.exe"
