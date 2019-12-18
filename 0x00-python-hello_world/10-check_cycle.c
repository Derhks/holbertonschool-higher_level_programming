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

	if (list == NULL)
	{
		return (0);
	}
	if (list->next == NULL)
	{
		return (0);
	}
	tmp = list;
	while (list != NULL && list->next != NULL)
	{
		tmp = tmp->next;
		list = list->next->next;
		if (tmp <= list)
		{
			return (1);
		}
	}
	return (0);
}
