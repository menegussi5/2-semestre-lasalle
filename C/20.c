#include <stdio.h>

int lerVar() {
    int num;
    printf("Digite um numero: ");
    scanf("%d", &num);
    return num;
}


void escreveVar() {
    int x;
    x = lerVar();
    printf("Voce digitou o numero: %d", x);
}


main() {
    escreveVar();
}