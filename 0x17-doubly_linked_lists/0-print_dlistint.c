#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * struct listint_s - singly linked list
 * @h: linked list to print
 *
 * Description: print all elements
 * Return: Number of count
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t count = 0;
    while (h != NULL)
    {
        printf("%d\n", h->n);
        h = h->next;
        count++;
    }
    return count;  
}