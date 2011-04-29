import unittest
import ps9

class Test_Triangle(unittest.TestCase):
    def test_Triangle___init__(self):
        self.triangle1 = ps9.Triangle(1.1, 2.2)
        self.assertEqual(self.triangle1.base, 1.1)
        self.assertEqual(self.triangle1.height, 2.2)
	
    def test_Triangle_area(self):
        self.triangle1 = ps9.Triangle(1.1, 9.3)
        self.assertAlmostEqual(self.triangle1.area(), ((1.1 * 9.3) / 2), 1)

    def test_Triangle___eq__(self):
        self.triangle1 = ps9.Triangle(2.2, 3.3)
        self.triangle2 = ps9.Triangle(2.2, 3.3)
        self.triangle3 = ps9.Triangle(2.2, 4.1)
        
        self.assertTrue(self.triangle1 == self.triangle2)
        self.assertTrue(self.triangle1 == self.triangle2)
        self.assertTrue(self.triangle2 == self.triangle1)
        self.assertFalse(self.triangle1 == self.triangle3)
        self.assertFalse(self.triangle3 == self.triangle1)
        
if __name__ == '__main__':
    unittest.main()