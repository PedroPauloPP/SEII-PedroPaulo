
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
	cout << "Hello World" << endl;
	
	 bool married = true;
	 char myGrade = 'A';
	 
	 cout << "Min float " <<
            numeric_limits<float>::min()
            << endl;
    cout << "Max float " <<
            numeric_limits<float>::max()
            << endl;
    cout << "Min double " <<
            numeric_limits<double>::min()
            << endl;
    cout << "Max double " <<
            numeric_limits<double>::max()
            << endl;
    cout << "Min long double " <<
            numeric_limits<long double>::min()
            << endl;
    cout << "Max long double " <<
            numeric_limits<long double>::max()
            << endl;
	
	return 0;
}

