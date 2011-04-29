# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: length of the base of the triangle
		height: height of the triangle
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        Returns approximate area of the triangle
        """
        return (self.base * self.height) / 2
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same base and height.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.list = []
        self.current_item = 0
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for item in self.list:
            if item == sh:
                return
        
        self.list.append(sh)
        #print('Appending ' + str(sh) + ' to the ShapeSet')
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.current_item = 0
        return self
    
    def __next__(self):
        if (self.current_item == len(self.list)):
            raise StopIteration
        else:
            value = self.list[self.current_item]
            self.current_item += 1
            #print('Returning ' + str(value))
            return value
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        the_string = ''
        for shape in self.list:
            the_string += str(shape) + '\n'
            
        return the_string
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest_area = 0.0
    largest_shapes = ()
    
    for shape in shapes:
        if shape.area() > largest_area:
            largest_area = shape.area()
    
    for shape in shapes:
        if shape.area() >= largest_area:
            largest_shapes += (shape,)
    
    return largest_shapes

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ss = ShapeSet()

    my_file = open(filename)

    for line in my_file.readlines():
        shape_info = line.split(',')
        
        if shape_info[0] == 'square':
            shape = Square(shape_info[1])
        elif shape_info[0] == 'circle':
            shape = Circle(shape_info[1])
        elif shape_info[0] == 'triangle':
            shape = Triangle(shape_info[1], shape_info[2])
        
        ss.addShape(shape)

    my_file.close()

    print(str(ss))
