#include <stdio.h>

#define VET 80

int main() {
    int vetor[VET];
    int menor, posicao;
    int i;

    for (i = 0; i < VET; i++) {
        printf("Digite o valor da posicao %d: ", i);
        scanf("%d", &vetor[i]);
    }

    menor = vetor[0];
    posicao = 0;

    for (i = 1; i < VET; i++) {
        if (vetor[i] < menor) {
        menor = vetor[i];
        posicao = i;
        }
    }

    printf("O menor valor eh %d e esta na posicao %d.\n", menor, posicao);
}