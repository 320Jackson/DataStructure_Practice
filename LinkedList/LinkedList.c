#include "LinkedList.h"
#include <stdlib.h>
#include <stdio.h>

Node *createList(int Data) {
    return addFront(NULL, Data);
}

Node *addFront(Node *StartPoint, int Data) {
    Node *newPoint = malloc(sizeof(Node));
    newPoint->Data = Data;
    newPoint->next = StartPoint;
    return newPoint;
}

void addBack(Node *List, int Data) {
    Node *Current = List;
    while(Current->next != NULL) {
        Current = Current->next;
    }
    Current->next = malloc(sizeof(Node));
    Current->next->Data = Data;
    Current->next->next = NULL;
    return;
}

Node *delFront(Node *StartPoint) {
    Node *removePoint = StartPoint;
    StartPoint = StartPoint->next;
    free(removePoint);
    return StartPoint;
}

void delBack(Node *List) {
    Node *Current = List;
    while(Current->next->next != NULL) {
        Current = Current->next;
    }
    free(Current->next->next);
    Current->next = NULL;
    return;
}

Node *Clear(Node *List) {
    while(List != NULL) {
        Node *removePoint = List;
        List = List->next;
        free(removePoint);
    }
    return NULL;
}

void insertNode(Node *Current, int Data) {
    Node *newPoint = malloc(sizeof(Node));
    newPoint->Data = Data;
    newPoint->next = Current->next;
    Current->next = newPoint;
    return;
}

void delNode(Node *Current) {
    Node *removeNode = Current->next;
    Current->next = removeNode->next;
    free(removeNode);
    return;
}