#include <stdio.h>

int somatorio(int n) {
    int soma = 0;
    for(int i = 1; i <= n; i++) {
        soma += i;
    }
    return soma;
}


main() {
    int valor;
    printf("Digite um numero inteiro e positivo: ");
    scanf("%d", &valor);
    
    if (valor > 0) {
        printf("O somatório de %d eh: %d\n", valor, somatorio(valor));
    }
    else {
        printf("Por favor, insira um número inteiro e positivo\n");
    }
}