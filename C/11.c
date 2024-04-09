#include <stdio.h>

int main() {
    int X[10];
    int i;
    for (i = 0; i < 10; i++) {
        X[i] = 30;
    }
    printf("O vetor X eh: ");
    for (i = 0; i < 10; i++) {
        printf("%d ", X[i]);
    }
}