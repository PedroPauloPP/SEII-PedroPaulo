
#include <cstdlib>
#include <iostream>
#include <string>
#include <limits>
#include <vector>
#include <sstream>
#include <numeric>
#include <ctime>
#include <cmath>


using namespace std;

int imGlobal = 0;
const double PI = 3.141;

int main(int argc, char **argv)
{
	int arrnNums[10] = {1};
	int arrnNums2[] = {1,2,3};
	int arrnNums3[5] = {8, 9};
	cout << "1st Value : " << arrnNums3[0] << endl;
    arrnNums3[0] = 7;
    cout << "1st Value : " << arrnNums3[0] << endl;
    int arrnNums4[2][2][2] = {{{1,2}, {3,4}},
    {{5,6}, {7,8}}};
    cout << arrnNums4[0][1][1] << endl;
    
    
    
	return 0;
}

