#include <stdio.h>
#include <stdlib.h>

main()
{
	int a,b,c,x;

	printf ("Informe 3 valores: ");
	scanf ("%d %d %d", &x, &a, &b);

	if (!(x>5))
		c = (a+b)*x;
	else
		c = (a-b)*x;

	printf ("Valor de c: %d \n", c);
}