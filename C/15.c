#include <stdio.h>

#define LIN 7
#define COL 9

int main() {
    int matriz[LIN][COL];
    int soma = 0;
    int i, j;

    printf("Digite os elementos da matriz %d x %d:\n", LIN, COL);
    for (i = 0; i < LIN; i++) {
        for (j = 0; j < COL; j++) {
        scanf("%d", &matriz[i][j]);
        }
    }

    printf("\nA matriz digitada eh:\n");
    for (i = 0; i < LIN; i++) {
        for (j = 0; j < COL; j++) {
        printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < LIN; i++) {
        for (j = 0; j < COL; j++) {
        soma = soma + matriz[i][j];
        }
    }

    printf("A soma dos elementos da matriz eh: %d\n", soma);
}