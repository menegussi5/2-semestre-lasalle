#include <stdio.h>
#include <stdlib.h>


main()
{
	char sexo;

	printf ("Informe o sexo: ");
	scanf ("%c", &sexo);

	if (sexo == 'M' || sexo == 'm' || sexo == 'F' || sexo == 'f')
		printf  ("Sexo valido\n");
	else 
		printf ("Sexo invalido\n");
}