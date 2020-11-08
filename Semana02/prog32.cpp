
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

double AddNumbers (double num1, double num2);
int AssignAge2(int age);

int main(int argc, char **argv)
{
	
	int age43 = 43;
	age43 = AssignAge2(age43);
	cout << age43;
 
    
	return 0;
}

double AddNumbers (double num1 = 0, double num2 = 0){
	return num1 + num2;
	
	}
	
	int AssignAge2(int age){
		age = 24;
		return age;
		
		}

