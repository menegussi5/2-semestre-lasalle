/* Exemplo 1 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
 {
      int x, y, soma, sub;
      float modulo, div, mult, raiz;
      x = 69;
      y = 24;
      
      soma = x + y;
      sub = x - y;
      mult = (float) x *y;
      div = (float) x/y;
      modulo = x % y;
      raiz = sqrt(y);
      printf ("%d + %d = %d\n", x, y, soma);
      printf ("%d - %d = %d\n", x, y, sub);
      printf ("%d x %d = %f\n", x, y, mult);
      printf ("%d / %d = %f\n", x, y, div);
      printf ("%d mod %d = %f\n", x, y, modulo);
      printf ("Raiz %d = %f\n", y, raiz);
 }