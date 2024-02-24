#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <termios.h>
#include <unistd.h>
#include <time.h>

#define ENTER 13
#define BACKSPACE 8

// Function to turn off terminal echo
void turnOffEcho()
{
	struct termios term;
	tcgetattr(STDIN_FILENO, &term);
	term.c_lflag &= ~(ECHO | ICANON); // Turn off echo and canonical mode
	tcsetattr(STDIN_FILENO, TCSANOW, &term);
}

// Function to turn on terminal echo
void turnOnEcho()
{
	struct termios term;
	tcgetattr(STDIN_FILENO, &term);
	term.c_lflag |= ECHO | ICANON; // Turn on echo and canonical mode
	tcsetattr(STDIN_FILENO, TCSANOW, &term);
}

int append(char c);

typedef struct string
{
	int (*append)(char c);
	char *str;
} str;

str mystr;
