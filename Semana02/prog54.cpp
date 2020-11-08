
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

struct Shape{
    double length, width;
    Shape(double l = 1, double w = 1){
        length = l;
        width = w;
    }
    double Area(){
        return length * width;
    }
private:
    int id;
};

struct Circle : Shape{
    Circle(double width){
        this->width = width;
    }
    double Area(){
        return 3.14159 * pow((width / 2), 2);
    }
};


int main(int argc, char **argv){
	
	Shape shape(10, 10);
	cout << "Square Area : " << shape.Area() << endl;
	Cirlce circle(10);
	cout << "Circle Area : " << circle.Area() << endl;
	Shape rectangle{10, 15};
	cout << "Rectangle Area : " << rectangle.Area() << endl;
	
 
    
	return 0;
}




