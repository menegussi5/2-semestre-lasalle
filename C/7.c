#include <stdio.h>
#include <stdlib.h>

int main() {

    int senha;

    while (senha != 2807) {
    printf("Digite a senha:\n");
    scanf("%d", &senha);

    if (senha == 2807) {
        printf("ACESSO PERMITIDO\n");
        break;
        }
    else {
        printf("SENHA INVALIDA\n");
        }
    }
}