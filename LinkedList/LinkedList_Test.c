#include <stdio.h>
#include "LinkedList.h"

void printList(Node *List) {
    Node *Current = List;
    while (Current != NULL) {
        printf("%d\n", Current->Data);
        Current = Current->next;
    }
}

int main() {
    Node *StartPoint = NULL;
    StartPoint = addFront(StartPoint, 0);
    for (int Run = 1; Run < 10; Run++) {
        addBack(StartPoint, Run);
    }
    printList(StartPoint);
    printf("\n");
    delBack(StartPoint);
    printList(StartPoint);
    printf("\n");
    StartPoint = delFront(StartPoint);
    printList(StartPoint);
    printf("\n");

    StartPoint = addFront(StartPoint, 256);
    addBack(StartPoint, 128);
    printList(StartPoint);

    StartPoint = Clear(StartPoint);
    return 0;
}