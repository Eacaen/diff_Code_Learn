#include <iostream>
#include "stdio.h"
using namespace std;
double warning = 0.3;

double ppp()
{
	extern double warning;
	printf("%f\n", warning);
	
	return 0;
}

double pp()
{
	warning = 0.5;
	printf("%f\n", warning);

	extern double warning;
	printf("%f\n", warning);

	return 0;
}


int main(int argc, char const *argv[])
{
	ppp();
	pp();
	return 0;
}