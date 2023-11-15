portable_linux:
	gcc launch.c -o "InvaderClone"

system_linux:
	gcc launch.c -o "InvaderClone" -DCOMPILE_MODE=1

windows:
	x86_64-w64-mingw32-gcc launch_win.c -o "InvaderClone.exe"

clean:
	rm -rf ./data/env
	rm "InvaderClone"
	rm "InvaderClone.exe"
