#include <stdio.h>

int main() {
    int v1[10], v2[10], v3[10];

    printf("Digite os elementos do primeiro vetor:\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &v1[i]);
    }
    
    printf("Digite os elementos do segundo vetor:\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &v2[i]);
    }
    
    for (int i = 0; i < 10; i++) {
        v3[i] = v1[i] * v2[i];
    }
    
    printf("O vetor resultante eh:\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", v3[i]);
    }
}