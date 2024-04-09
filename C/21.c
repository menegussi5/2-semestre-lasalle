#include <stdio.h>

int verificaPar(int num) {
    if (num % 2 == 0) {
        printf("1");
    }
    else {
        printf("2");
    }
}


main() {
    int x;
    printf("Digite um valor inteiro: ");
    scanf("%d", &x);

    verificaPar(x);
}