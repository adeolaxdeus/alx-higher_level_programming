#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Insert a number into a sorted singly linked list
 * @head: Pointer to singly linked list
 * @number: Number to be inserted
 *
 * Return: Pointer to new node on success otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	/** insert at the beginning or in  an empty list **/
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
	 {
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
