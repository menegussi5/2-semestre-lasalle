#include <stdio.h>
#include <stdlib.h>

main()
{
	float salario, SR;

	printf ("Informe o salario: ");
	scanf ("%f", &salario);

	if (salario < 500)
		SR = (salario * 1.15);
	else
		if (salario <= 1000)
			SR = (salario * 1.10);
		else
			SR = (salario * 1.05);

	printf ("Salario com reajuste: %.2f \n", SR);
}