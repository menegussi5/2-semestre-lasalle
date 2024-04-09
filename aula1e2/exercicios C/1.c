#include <stdio.h>
#include <stdlib.h>

int main()
{

    int x;

    printf("Digite um valor numerico inteiro: ");
    scanf("%i", &x);
    
    if ((x) >= 0)
        printf("o numero %d e positivo\n", x);
    if ((x) < 0)
        printf("o numero %d e negativo\n", x);

}