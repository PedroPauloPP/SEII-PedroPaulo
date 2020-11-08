
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
void AssignAge3(int* pAge);

void DoubleArray(int *arr, int size);

int main(int argc, char **argv)
{
	int age2  = 43;
	int* pAge2 = NULL;
	pAge2 = &age2;
	cout << "Address : " << pAge2 << endl;
	cout << "Value : " << *pAge2 << endl;
	
	int intArray[] = {1,2,3,4};
    int* pIntArray = intArray;
    cout << "1st " << *pIntArray <<
            " Address " << pIntArray << endl;
    pIntArray++;
    cout << "2nd " << *pIntArray <<
            " Address " << pIntArray << "endl;
    pIntArray--;
    cout << "1st " << *pIntArray <<
            " Address " << pIntArray << endl;
 
 DoubleArray(intArray, 4);
 for(int i = 0; i < 4; ++i){
	 cout << "Array" << intArray[i] << endl;
	 }
    
	return 0;
}

double AddNumbers (double num1 = 0, double num2 = 0){
	return num1 + num2;
	
	}
	
	void DoubleArray(int *arr, int size){
		for(int i = 0; i < size; ++i){
			arr[i] = arr[i] * 2;
			}
		}

