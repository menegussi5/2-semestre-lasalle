#include <stdio.h>

void leValoresImprimeMaiorMenor() {
    int i, numero, maior, menor;

    printf("Digite o primeiro numero: ");
    scanf("%d", &numero);

    maior = numero;
    menor = numero;
    for(i = 1; i < 50; i++) {
        printf("Digite o proximo numero: ");
        scanf("%d", &numero);

        if(numero > maior) {
            maior = numero;
        }
        if(numero < menor) {
            menor = numero;
        }
    }
    printf("O maior numero digitado foi: %d\n", maior);
    printf("O menor numero digitado foi: %d\n", menor);
}


int main() {
    leValoresImprimeMaiorMenor();
}