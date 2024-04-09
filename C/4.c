#include <stdio.h>
#include <stdlib.h>

int main() {

    char caracter;

    printf("Digite uma das letras: C, S, D ou V\n");
    scanf("%s", &caracter);

    if (caracter == 'C' || caracter == 'c') {
        printf("Casado(a)");
    }
    else if (caracter == 'S' || caracter == 's') {
        printf("Solteiro(a)");
    }
    else if (caracter == 'D' || caracter == 'd') {
        printf("Divorciado(a)");
    }
    else if (caracter == 'V' || caracter == 'v') {
        printf("Viuvo(a)");
    }    
    else {
        printf("Nao e uma das letras!");
    }

}