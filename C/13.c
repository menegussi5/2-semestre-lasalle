#include <stdio.h>

int main() {
    int vetor[20];
    int i, pares = 0;

    printf("Digite 20 valores inteiros:\n");
    for (i = 0; i < 20; i++) {
        scanf("%d", &vetor[i]);
        if (vetor[i] % 2 == 0) {
        pares++;
        }
    }

    printf("O vetor digitado foi:\n");
    for (i = 0; i < 20; i++) {
        printf("%d ", vetor[i]);
    }

    printf("\n");
    printf("O numero de valores pares no vetor eh: %d\n", pares);
}
