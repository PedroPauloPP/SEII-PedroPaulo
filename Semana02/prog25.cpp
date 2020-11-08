
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
	vector<string> words;
    stringstream ss("Some Random Words");
    string word;
    while(getline(ss, word, ' ')){
        words.push_back(word);
    }
 
    
 
    
    
	return 0;
}

