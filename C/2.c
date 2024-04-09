#include <stdio.h>
#include <stdlib.h>

int main() {

    float media, nota1, nota2;

    printf("Digite sua primeira nota:\n");
    scanf("%f", &nota1);
    printf("Digite sua segunda nota:\n");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

    if (media >= 6)
        printf("PARABENS! Voce foi aprovado");
    if (media < 6)
        printf("Voce foi REPROVADO! Estude mais");

}