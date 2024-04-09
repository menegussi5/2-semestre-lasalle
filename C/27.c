#include <stdio.h>

int fatorial(int n) {
    if (n == 0)
        return 1;
    else
        return n * fatorial(n - 1);
}


main() {
    int num;
    printf("Digite um numero inteiro: ");
    scanf("%d", &num);
    if (num < 0)
        printf("Erro! Fatorial de um numero negativo nao existe");
    else
        printf("Fatorial de %d = %d", num, fatorial(num));
}