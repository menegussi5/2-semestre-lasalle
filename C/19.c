#include <stdio.h>

int main() {
    int matriz[3][3];
    
    printf("Digite os elementos da matriz 3x3:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &matriz[i][j]);
        }
    }
    
    int soma = 0;
    for (int i = 0; i < 3; i++) {
        soma += matriz[i][2-i];
    }
    double media = (double) soma / 3;
    
    for (int i = 0; i < 3; i++) {
        matriz[i][i] *= media;
    }
    
    printf("A matriz resultante eh:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d\t", matriz[i][j]);
        }
        printf("\n");
    }
}
