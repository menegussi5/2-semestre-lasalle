#include <stdio.h>

void tabuada(int N) {
    printf("Tabuada do %d:\n", N);
    for (int j = 1; j <= 10; j++) {
        printf("%d x %d = %d\n", N, j, N*j);
    }
    printf("\n");
}


int main() {
    int N;
    printf("Digite um numero: ");
    scanf("%d", &N);
    tabuada(N);
}