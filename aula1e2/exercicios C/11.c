#include <stdio.h>
#include <stdlib.h>

int main() {

    int senha;
    
    printf("Digite a senha:\n");
    scanf("%d", &senha);

    if (senha == 1234) {
        printf("ACESSO PERMITIDO\n");
    }
    else {
        printf("ACESSO NEGADO\n");
    }
    
}