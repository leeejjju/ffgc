#include "db_stack.h"
#include <stdio.h>

// removes all the nodes from the p(stack)
// if stack is nomarlly cleared return 0, otherwise return 1
int stack_clear(Node * p) {
    if (stack_empty(p)) {
        return 0;
    }
    Node * curr = p;
    while (curr != nullptr) {
        Node * temp = curr;
        curr = curr->next;
        delete temp;
    }
    return 0;
}

// returns true if the stack(p) is empty
bool stack_empty(Node * p) {
    return p == nullptr;
}

// returns the number of nodes in the stack(p)
int stack_size(Node * p) {
    if (stack_empty(p)) {
        return 0;
    }
    int count = 0;
    while (p != nullptr) {
        p = p->next;
        count++;
    }
	return count;
}

// inserts a new node with val at the end of stack(p)
// return the first node of stack(p)
Node * stack_push(Node * p, char val) {
    Node * start = p;
    if (p == nullptr) {
        return p = new Node{val, nullptr};
    }

    Node * prev = nullptr;
    while (p != nullptr) {
        prev = p;
        p = p->next;
    }
    p = new Node{val, nullptr};
    prev->next = p;

    return start;
}

// removes the last node in the stack(p)
// return the first node of stack(p)
Node * stack_pop(Node * p) {
    Node * start = p;
    if (stack_empty(p)) {
        return p;
    }

    Node * prev = nullptr;
    while (p->next != nullptr) {
        prev = p;
        p = p->next;
    }
    if (prev != nullptr) {
        prev->next = nullptr;
    }
    delete p;

    if (prev == nullptr) {
        return nullptr;
    }
    return start;
}

// return the top node stack
Node * stack_top(Node * p) {
    if (stack_empty(p)) {
        return p;
    }

    int count = 0;
    while (p->next != nullptr) {
        p = p->next;
        count++;
    }
    return p;
}