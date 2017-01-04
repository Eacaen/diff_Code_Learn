#include <map>
#include <iostream>
using namespace std;

bool fncomp(char ls , char _ls)
{
    return ls > _ls;
}

class classcomp
{
public:
	bool operator() (const char& ls , const char& _ls)const
	{return ls > _ls;}
};

//bool FuncT(const char& ls , const char& _ls , classcomp& funct)
bool FuncT(const char& ls , const char& _ls )
{
    classcomp funct;
    return funct(ls,_ls);
}
/*
bool ffffunct(const char& ls , const char& _ls)
{
    classcomp  funct;
    FuncT(ls,_ls,funct);
}
*/
int  main()
{
   classcomp class_comp;

	map<char , int> first;
	typedef pair<char,int> _pair;

	first.insert(_pair('a' , 10));
	first.insert(_pair('b' , 30));
	first.insert(_pair('c' , 50));
	first.insert(_pair('d' , 70));


	map<char , int>::iterator iter;
	for(iter = first.begin() ; iter != first.end() ; iter++)
	{
		cout<<iter->first<<"  "<<iter->second<<endl;
	}

	map<char,int>second(first.begin(),first.end());
	for(iter = second.begin() ; iter != second.end() ; iter++)
	{
		cout<<iter->first<<"  "<<iter->second<<endl;
	}

	//bool (* fn_pt)(char,char) = fncomp;
	//bool(*fn_pt)(const char& ls , const char& _ls) = ffffunct;

	bool (* fn_pt)(const char& ls , const char& _ls) = FuncT;

	map<char,int, bool(*)(const char&, const char&) > third(fn_pt);
    third.insert(_pair('a' , 10));
	third.insert(_pair('b' , 30));
	third.insert(_pair('c' , 50));
	third.insert(_pair('d' , 70));
	for(iter = third.begin() ; iter != third.end() ; iter++)
	{
		cout<<iter->first<<"  "<<iter->second<<endl;
	}
	return 0;
}
