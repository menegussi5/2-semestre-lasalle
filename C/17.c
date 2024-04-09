#include <stdio.h>

#define LIN 15
#define COL 20

int main() {
    double matriz[LIN][COL];
  
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
        printf("Digite o elemento da linha %d e coluna %d: ", i + 1, j + 1);
        scanf("%lf", &matriz[i][j]);
        }
    }
  
    for (int j = 0; j < COL; j++) {
        double soma = 0;
        for (int i = 0; i < LIN; i++) {
        soma += matriz[i][j];
        }
        printf("A soma da coluna %d eh %.2f\n", j + 1, soma);
    }
}