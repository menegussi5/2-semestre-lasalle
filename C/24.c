#include <stdio.h>

int num_divisores(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            count++;
        }
    }
    return count;
}


main() {
    int valor;
    printf("Digite um numero inteiro e positivo: ");
    scanf("%d", &valor);
    
    if (valor > 0) {
        printf("O numero de divisores de %d eh: %d\n", valor, num_divisores(valor));
    }
    else {
        printf("Por favor, insira um número inteiro e positivo\n");
    }
}
