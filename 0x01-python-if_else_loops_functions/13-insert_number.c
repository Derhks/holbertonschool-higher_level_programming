#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - This is a function prototype
 * @head: Recive a string from the main function
 * @number: Recive a digit from the main function
 * Description: Function that inserts a number
 * section Header: Section description
 * Return: The address of the new node, otherwise NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new_node = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		return (new_node);
	}

	tmp = *head;
	while (tmp->next != NULL)
	{
		tmp = tmp->next;
		if (tmp->n < number && number < tmp->next->n)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
		}
	}
	return (new_node);
}
