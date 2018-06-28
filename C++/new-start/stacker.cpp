#include <iostream>
#include <cctype>
#include "stack.h"
int main(int argc, char const *argv[])
{
	using namespace std;
	Stack st;
	char ch;
	unsigned long po;

	while(cin >> ch && toupper(ch) != 'Q')
	{
		while(cin.get() != '\n')
			continue;
		if(!isalpha(ch))
		{
			cout << "\a";
			continue;
		}
		switch(ch)
		{
			case 'A' :
			case 'a' : cout << "enter a p0 number to add";
				cin >> po;
				if(st.isfull())
				{
					cout<< "stack is full";
				}
				else
					st.push(po);
			break;

			case 'P' :
			case 'p' : 
				if(st.isempty())
					cout<<"stack is empty";
				else
				{
					st.pop(po);
					cout << "-----" << po <<"poped \n";
				}
			break;
		}
		cout<<"continue\n";
	}
	return 0;
}