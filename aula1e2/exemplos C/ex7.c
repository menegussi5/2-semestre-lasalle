#include <stdio.h>
#include <stdlib.h>

main()
{
	int A,B,C,D,X;

	printf ("Informe 3 valores: ");
	scanf ("%d %d %d", &X, &A, &B);

	if (!(X>5))
	  {   // início do bloco
	    C = (A+B)*X;
	    D = A+1;
	  } // fim do bloco
	else 
	  {
	     C = (A-B)*X;
	     D = B+1;
	  }

	printf ("Valor de C: %d \n", C);
	printf ("Valor de D: %d \n", D);
}