
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
	vector<int> vNums(2);
    vNums[0] = 1;
    vNums[1] = 2;
    vNums.push_back(3);
    cout << "Vector Size : " << vNums.size() << endl;
 
    
    
	return 0;
}

