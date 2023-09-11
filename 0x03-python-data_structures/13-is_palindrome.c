/*
 * File: 13-is_palindrome.c
 * Auth: Salmane Ben Messaoud
 * */

#include "lists.h"
/*
 * Function to reverse a linked list.
 * @head: pointer to pointer of first node of listint_t list
 */
listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * Function to check if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list
 */
int is_palindrome(listint_t **head) {
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *second_half = NULL;
    listint_t *prev_of_slow_ptr = *head;
    int is_palindrome = 1; 

    if (*head == NULL || (*head)->next == NULL) {
        return 1;
    }

    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        fast_ptr = fast_ptr->next->next;
        prev_of_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    if (fast_ptr != NULL) {
        slow_ptr = slow_ptr->next;
    }

    second_half = reverse_list(slow_ptr);

    while (second_half != NULL) {
        if ((*head)->n != second_half->n) {
            is_palindrome = 0; 
            break;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    second_half = reverse_list(second_half);
    prev_of_slow_ptr->next = second_half;

    return is_palindrome;
}
