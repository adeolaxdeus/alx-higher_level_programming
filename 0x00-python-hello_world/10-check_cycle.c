#include "lists.h"
#include <stdlib.h>
/**
 *  check_cycle -  Check if a singly linked list has a cycle in it
 *  @list: Pointwr to singly linked list head
 *
 *  Return: 0 if there is no cycle found else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
