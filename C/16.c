#include <stdio.h>

int main() {
    int matriz[10][10];
  
    int contador = 1;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
        matriz[i][j] = contador;
        contador++;
        }
    }
  
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
        printf("%d\t", matriz[i][j]);
        }
        printf("\n");
    }
}