#ifndef SHAPE_H
#define SHAPE_H

class Shape {
protected:
	double height;
	double width;
public:
    static int numOfshapes;
    Shape(double length);
    Shape(double height, double width);
    Shape();
    
    virtual ~Shape();


};

#endif
