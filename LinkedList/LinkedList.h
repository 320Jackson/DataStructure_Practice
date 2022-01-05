typedef struct Node Node;
struct Node {
    int Data;
    struct Node *next;
};

Node *createList(int);

Node *addFront(Node *, int);
void addBack(Node *, int);

Node *delFront(Node *);
void delBack(Node *);

Node *Clear(Node *);
void insertNode(Node *, int);
void delNode(Node *);