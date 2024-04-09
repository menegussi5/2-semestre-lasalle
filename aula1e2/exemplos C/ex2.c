#include <stdio.h>
#include <stdlib.h>

int main()
{
  int j, k;
  printf("Digite valor para k:\n");
  scanf("%d", &k);
  
  printf("Digite valor para j:\n");
  scanf("%d", &j);
  
  printf("Voce digitou k = %d\nj = %d\n", k, j);
  printf("A soma de %d com %d eh %d\n", k, j, k+j);
}