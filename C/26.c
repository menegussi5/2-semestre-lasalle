#include <stdio.h>

int idadeEmDias(int anos) {
    return (anos * 365);
}


main() {
    int idade;
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    printf("A sua idade em dias eh: %d", idadeEmDias(idade));
}