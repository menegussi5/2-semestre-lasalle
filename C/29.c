#include <stdio.h>

char conceito(float media) {
    if (media >= 0 && media < 5) {
        return 'D';
    }
    else if (media >= 5 && media < 7) {
        return 'C';
    }
    else if (media >= 7 && media < 9) {
        return 'B';
    }
    else if (media >= 9 && media < 10) {
        return 'A';
    }
    else {
        return 'X';
    }
}


main() {
    float media;
    printf("Digite a media do aluno: ");
    scanf("%f", &media);
    printf("O conceito do aluno eh: %c\n", conceito(media));
}