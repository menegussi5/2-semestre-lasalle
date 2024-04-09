#include <stdio.h>
#include <stdlib.h>
#include <string.h>

main() {

    char dia[20];
    printf("Digite o dia da semana:\n");
    scanf("%s", dia);

    if (((strcmp(dia, "sabado") == 0)) || ((strcmp(dia, "domingo") == 0)))
        printf("Final de Semana");

    else if (((strcmp(dia, "segunda") == 0)) || ((strcmp(dia, "terca") == 0)) || ((strcmp(dia, "quarta") == 0)) || ((strcmp(dia, "quinta") == 0)) || ((strcmp(dia, "sexta") == 0)))
        printf("Dia util");
    else
        printf("Dia invalido");
}