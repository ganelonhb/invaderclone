#include "manylinuxnotify.h"

int manylinuxNotify(const char* title, const char* body, bool question)
{
	// First, we print the message to stdout.
	printf("%s: %s", title, body);

	const int lenTitle = strlen(title);
	const int lenBody = strlen(body);

	// Check for kdialog, yad, and zenity.
	bool kdialog = !access("/usr/bin/kdialog", F_OK) || !access("/bin/kdialog", F_OK);
	bool yad = !access("/usr/bin/yad", F_OK) || !access("/bin/yad", F_OK);
	bool zenity = !access("/usr/bin/zenity", F_OK) || !access("/bin/zenity", F_OK);

	// yes is true, no is false
	int answer = false;


	// The check goes kdialog > yad > zenity.
	// This is because users who use KDE will typically also have some GNOME applications installed, but not necessarily vice-versa.
	// Then, yad comes before zenity because yad is a fork of zenity, and users who have yad installed may want to use it over zenity.
	// We already printed the message in the terminal, so if the user really needs to know what's going on then they can run from their favorite
	// terminal emulator.
	if (kdialog)
	{
		const int kdialogStringLength = (question ? 30 : 31)  + lenTitle + lenBody;
		char* kdialogString = (char*)malloc(kdialogStringLength * sizeof(char));
		memset(kdialogString, '\0', kdialogStringLength * sizeof(char));
		if (question)
		{
			sprintf(kdialogString, "kdialog --title \"%s\" --yesno \"%s\"", title, body);
		}
		else
		{
			sprintf(kdialogString, "kdialog --title \"%s\" --msgbox \"%s\"", title, body);
		}

		FILE* kdia = popen(kdialogString, "w");

		free(kdialogString);
		answer = pclose(kdia) ? 0 : 1;
	}
	else if (yad)
	{
		const int yadStringLength = (question ? 54 : 38) + lenTitle + lenBody;
		char* yadString = (char*)malloc(yadStringLength * sizeof(char));
		memset(yadString, '\0', yadStringLength * sizeof(char));

		if (question)
		{
			sprintf(yadString, "yad --button=Yes:0 --button=No:1 --title \"%s\" --text \"%s\"", title, body);
		}
		else
		{
			sprintf(yadString, "yad --no-buttons --title \"%s\" --text \"%s\"", title, body);
		}

		FILE* ya = popen(yadString, "w");

		free(yadString);
		answer = pclose(ya) ? 0 : 1;
	}
	else if (zenity)
	{
		const int zenityStringLength = (question ? 39 : 35) + lenTitle + lenBody;
		char* zenityString = (char*)malloc(zenityStringLength * sizeof(char));
		memset(zenityString, '\0', zenityStringLength * sizeof(char));

		if (question)
		{
			sprintf(zenityString, "zenity --question --title \"%s\" --text \"%s\"", title, body);
		}
		else
		{
			sprintf(zenityString, "zenity --info --title \"%s\" --text \"%s\"", title, body);
		}

		FILE* zen = popen(zenityString, "w");

		free(zenityString);
		answer = pclose(zen) ? 0 : 1;
	}
	else
	{
		return -1;
	}

	fflush(stdout);

	return answer;
}
