#include <iostream>
#include <deque>
#include <string>
#include <algorithm>
#include <iterator>
using namespace std;
int main(int argc, char const *argv[])
{
	deque<string> strdeq;
	strdeq.assign(4,string("ABCDE"));
	strdeq.push_back("last_string");
	strdeq.push_front("first_string");

	copy(strdeq.begin(),strdeq.end(),ostream_iterator<string>(cout,""));
	cout<<endl;

	strdeq.pop_front();
	strdeq.pop_back();
	copy(strdeq.begin(),strdeq.end(),ostream_iterator<string>(cout,""));
	cout<<endl;

	strdeq.resize(4,"resized string");
	copy(strdeq.begin(),strdeq.end(),ostream_iterator<string>(cout,""));
	cout<<endl;	

	return 0;
}
