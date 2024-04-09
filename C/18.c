#include <stdio.h>

#define MATRIZ 10

int main() {
    int matriz[MATRIZ][MATRIZ];
    
    for (int i = 0; i < MATRIZ; i++) {
        for (int j = 0; j < MATRIZ; j++) {
        printf("Digite o elemento da linha %d e coluna %d: ", i + 1, j + 1);
        scanf("%d", &matriz[i][j]);
        }
    }
    
    int soma = 0;
    for (int i = 0; i < MATRIZ; i++) {
        soma += matriz[i][i];
    }
    double media = (double) soma / MATRIZ;
    
    printf("A media dos elementos da diagonal principal eh %.2f\n", media);
}
