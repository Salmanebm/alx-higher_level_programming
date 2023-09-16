#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 * @next: points to the prev node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct dlistint_t
{
    int n;
    struct dlistint_t *next;
    struct dlistint_t *prev;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);

#endif /* LISTS_H */