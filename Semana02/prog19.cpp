
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
	
    int age43 = 43;
    bool canIVote = (age43 >= 18) ? true : false;
    cout.setf(ios::boolalpha);
    cout << "Can Derek Vote : " << canIVote << endl;
    
    
	return 0;
}

