#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "db_stack.h"

int main() {

    Node * stack = nullptr;

    char buf[32];
    scanf("%31s", buf);


    for (int i = 0 ; i < strlen(buf); i++) {
        if (i % 2 == 0 || i % 5 == 0) {
            stack = stack_push(stack, buf[i]);
        }
        else {
            stack = stack_pop(stack);
        }
    }

    if (!stack_empty(stack)) {
        printf("top node data: %c\n", stack_top(stack)->data);
    }
    
    // int size = stack_size(stack);
    // printf("size: %d\n", size);

    stack_clear(stack);

}