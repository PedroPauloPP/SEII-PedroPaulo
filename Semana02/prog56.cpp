
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
   copy_if(vecVals.begin(), vecVals.end(),
           back_inserter(evenVecVals),
           [](int x){ return (x % 2) == 0; });
           
           for(auto val: evenVecVals)
               cout << val << endl;
           
	return 0;
}




