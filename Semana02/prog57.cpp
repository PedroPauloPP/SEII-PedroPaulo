
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

vector<int> GenerateRandVec(int numofNums, int min, int max);

int main(int argc, char **argv){
	
   vector<int> vecVals = GenerateRandVec(10, 1, 50);
   int sum = 0;
   for_each(vecVals.begin(), vecVals.end().
            [&](int x) {sum += x;});
            
            cout << "Sum : " <<sum <<endl;
           
	return 0;
}




