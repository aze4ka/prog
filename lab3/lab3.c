#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Data storage structure
typedef struct Data {
    enum {INT} tag;
    union {
        int i;
    } d;
} Data;

// Unidirectional list
typedef struct List {
    Data data;
    struct List *next;
} List;

// Function for adding an item to a list
void list_append(List **l, const Data d) {
    List *new_node = malloc(sizeof(List));
    new_node->data = d;
    new_node->next = NULL;

    if (*l == NULL) {
        *l = new_node;
    } else {
        List *temp = *l;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = new_node;
    }
}

// A function for filling a list with random numbers
void fill(int n, List **l) {
    for (int i = 0; i < n; ++i) {
        int num = (rand() % 101) - 50; // Random numbers from -50 to 50
        Data data = {.tag = INT, .d.i = num};
        list_append(l, data);
    }
}

// A function for searching for three maximum values and calculating the result
int compute(int n, List *l) {
    int M[3] = {-9999, -9999, -9999}; // An array for storing three maximum values
    int I[3] = {-1, -1, -1}; // An array for storing indexes of these values

    List *p = l;
    for (int i = 0; i < n; ++i) {
        if (p->data.d.i > M[0]) {
            M[2] = M[1];
            I[2] = I[1];
            M[1] = M[0];
            I[1] = I[0];
            M[0] = p->data.d.i;
            I[0] = i;
        } else if (p->data.d.i > M[1]) {
            M[2] = M[1];
            I[2] = I[1];
            M[1] = p->data.d.i;
            I[1] = i;
        } else if (p->data.d.i > M[2]) {
            M[2] = p->data.d.i;
            I[2] = i;
        }
        p = p->next;
    }

    printf("Three maxima: %i, %i, %i\n", M[0], M[1], M[2]);
    printf("Indexes: %i, %i, %i\n", I[0], I[1], I[2]);

    return (M[0] * M[1] * M[2]) - ((I[0] + I[1] + I[2]) % n);
}

int main() {
    srand(time(NULL));
    List *l = NULL; // Pointer to the beginning of the list
    int n;

    printf("Enter the number of array elements n: ");
    scanf("%d", &n);

    fill(n, &l);
    
    int result = compute(n, l);
    printf("Result: %i\n", result);

    // Freeing up memory
    List *temp;
    while (l != NULL) {
        temp = l;
        l = l->next;
        free(temp);
    }

    return 0;
}
