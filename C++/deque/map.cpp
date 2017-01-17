#include <map>
#include <iostream>
using namespace std;
int  main(int argc, char const *argv[])
{
	map<int , string>mapStu;
	typedef pair<int,string> _pair;
	for(int i = 0 ; i < 15 ; i++)
	{
		mapStu.insert(_pair(15 - i,"a"));

	}

	map<int,string>::iterator iter;
	for(iter = mapStu.begin() ; iter != mapStu.end() ; iter++)
	{
		cout<<iter->first<<"  "<<iter->second<<endl;
	}

	return 0;
}
