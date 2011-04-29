from ps9 import *

def test_findLargest1():
    ss = ShapeSet()
    ss.addShape(Triangle(1.2,2.5))
    ss.addShape(Circle(4))
    ss.addShape(Square(3.6))
    ss.addShape(Triangle(1.6,6.4))
    ss.addShape(Circle(2.2))
    largest = findLargest(ss)

    for e in largest:
        print (e)
        
    print()

def test_findLargest2():
    ss = ShapeSet()
    ss.addShape(Triangle(3,8))
    ss.addShape(Circle(1))
    ss.addShape(Triangle(4,6))
    largest = findLargest(ss)

    for e in largest:
        print (e)
        
    print()

def test_findLargest3():
    t = Triangle(6,6)
    c = Circle(1)
    ss = ShapeSet()
    ss.addShape(t)
    ss.addShape(c)
    largest = findLargest(ss)
    
    for e in largest:
        print (e)

    print(largest[0] is t)

    print(largest[0] is c)

def test_readShapesFromFile():
    readShapesFromFile('shapes.txt')

if __name__ == '__main__':
    #test_findLargest1()
    #test_findLargest2()
    #test_findLargest3()
    test_readShapesFromFile()