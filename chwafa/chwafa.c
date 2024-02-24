#include "chwafa.h"

int append(char c)
{
	if (!c)
	{
		free(mystr.str);
		return (1);
	}
	int len = strlen(mystr.str), i = 0, j = 0;
	char *buff = malloc(len + 2);
	while (i != len + 2)
	{
		if (mystr.str[j] != '\0')
			buff[i] = mystr.str[j++];
		else
		{
			buff[i++] = c;
			buff[i] = '\0';
		}
		i++;
	}
	if (len != 0)
		free(mystr.str);
	mystr.str = buff;
	return (1);
}

int main(void)
{
	srand(time(NULL));
	mystr.append = append;
	mystr.str = "";
	char c, i = 0;
	char *si7r[] = {"bhgit nswlk ", "wa chwafa", "arbi magoli liya "};
	turnOffEcho();
	int index = rand() % 3;
	c = getchar();
	while (c != '/')
	{
		mystr.append(c);
		turnOnEcho();
		if (i < strlen(si7r[index]))
		{
			printf("%c", si7r[index][i]);
			i++;
		}
		turnOffEcho();
		c = getchar();
	}
	turnOnEcho();
	while (i < strlen(si7r[index]))
	{
		printf("%c", si7r[index][i]);
		i++;
	}

	char line[325];
	fgets(line, 325, stdin);
	printf("%s\n", mystr.str);
	mystr.append(0);
	return (0);
}
