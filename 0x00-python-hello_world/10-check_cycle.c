#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - This is a function prototype
 * @list: Recive a pointer from the main function
 * Description: Function that checks if a singly linked list has a cycle in it
 * Section header: Section description
 * Return: 1, otherwise 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp;
	int cnt;

	if (list == NULL)
	{
		return (0);
	}
	for (cnt = 0; list->next == NULL; cnt++)
	if (cnt == 0)
	{
		return (0);
	}
	tmp = list;
	while (list != NULL)
	{
		tmp = tmp->next;
		list = list->next->next;
		if (tmp == list)
		{
			return (1);
		}
	}
	return (0);
}
