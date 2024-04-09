#include <stdio.h>
#include <stdlib.h>

int main() {

    int num, cont;

    printf("Digite um numero: ");
    scanf("%d", &num);

    while (num >= 0) {
      printf("Tabuada do %d:\n", num);
      for (cont = 1; cont <= 10; cont++) {
        printf("%d x %d = %d\n", num, cont, num * cont);
      }
      printf("Digite outro numero ou um numero negativo para sair: ");
      scanf("%d", &num);
    }
    printf("Encerrando programa\n");
}