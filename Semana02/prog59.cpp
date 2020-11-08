
#include <cstdlib>
#include <iostream>
#include <string>
#include <limits>
#include <vector>
#include <sstream>
#include <numeric>
#include <ctime>
#include <cmath>
#include <fstream>



using namespace std;

double MultBy2(double num){
    return num * 2;
}
 double DoMath(function<double(double)> func, double num){
    return func(num);
}
double MultBy3(double num){
    return num * 3;
}
 
int main(int argc, char **argv){
	
	auto times2 = MultBy2;
    cout << "5 * 2 = " <<
            times2(5) << endl;
    cout << "6 * 2 = " <<
            DoMath(times2, 6) << endl;
    vector<function<double(double)>> funcs (2);
    funcs[0] = MultBy2;
    funcs[1] = MultBy3;
    cout << "2 * 10 = " <<
            funcs[0](10) << endl;
 
 
   
   
	return 0;
}




