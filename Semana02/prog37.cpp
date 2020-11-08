#ifndef SHAPE_H
#define SHAPE_H

class Shape {
protected:
	double height;
	double width;
public:
    Shape();
    Shape(const Shape& orig);
    virtual ~Shape();


};

#endif
