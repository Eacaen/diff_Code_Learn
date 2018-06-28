#include <iostream>
#include "coordin.h"
using namespace std;
int main(int argc, char const *argv[])
{
	rect replace;
	polar pplace;

	cout << "Enter the x and y values ";
	while(cin >> replace.x >> replace.y)
	{
		pplace = rect_to_polar(replace);
		show_polar(pplace);
		cout << "Next two numbers ";
	}
	cout << "Bye\n" ;
	return 0;
}