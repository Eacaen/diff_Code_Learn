#include <iostream>
#include <cmath>
#include "coordin.h"

polar rect_to_polar(rect xypos) 
{
	using namespace std;
	polar ans;

	ans.distance = 
		sqrt( xypos.x * xypos.x + xypos.y * xypos.y);
	ans.angle = atan2(xypos.y , xypos.x);

	return ans;
}
void show_polar(polar dapos)
{
	using namespace std;
	const double Red_to_deg = 57.29577;

	cout << "distance = " << dapos.distance;
	cout << "\n angle = " << dapos.angle * Red_to_deg;
}