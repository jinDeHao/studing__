#include <stdio.h>
#include <stdlib.h>
#include "monthy.h"
#include <string.h>

void *stack_insert(stack_t **head, int n)
{
	/* allocate enough memory for the node */
	stack_t *new_node = malloc(sizeof(stack_t));
	/* check if the node allocated */
	if (!new_node)
		return (NULL);
	/* fill the node's data */
	new_node->n = n;
	/* set the next of the new_node to the head */
	new_node->next = *head;
	/* set the prev of the new_node to NULL */
	new_node->prev = NULL;
	/* set the prev of the head to the new_node */
	if (*head)
		(*head)->prev = new_node;
	*head = new_node;
}

char *parseline(char *str)
{
	char *new_str = strdup(str), *endofstr, i = 0;
	endofstr = new_str;
	while (*endofstr != '\0')
		endofstr++;
	while (*(endofstr - 1) == ' ' || *(endofstr - 1) == '\n')
		endofstr--;
	*endofstr = '\0';
	while (*new_str == ' ' && *new_str != '\0')
		new_str++;

	return new_str;
}

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		fprintf(stderr, "USAGE: monty file\n");
		return (1);
	}
	FILE *file = fopen(argv[1], "r");
	if (!file)
	{
		fprintf(stderr, "Error: Can't open file %s\n", argv[1]);
		return (1);
	}
	char line[1024];
	int num_of_line = 0;
	while (fgets(line, 1024, file))
	{
		char *parsedline = parseline(line);
		if (*parsedline == '\0')
			continue;
		fprintf(stdout, "%s\n", parsedline);
		fprintf(stdout, "%ld\n", strlen(parsedline));
		num_of_line++;
	}
	return (0);
}
