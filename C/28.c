#include <stdio.h>

void verificarPositivoOuNegativo(int valor) {
    if (valor > 0) {
        printf("O numero %d eh positivo\n", valor);
    }
    else if (valor < 0) {
        printf("O numero %d eh negativo\n", valor);
    }
    else {
        printf("O numero %d eh zero\n", valor);
    }
}


main() {
    int numero;
    printf("Digite um numero: ");
    scanf("%d", &numero);
    verificarPositivoOuNegativo(numero);
}