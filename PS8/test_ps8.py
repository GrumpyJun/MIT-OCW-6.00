import unittest

class TestPS8(unittest.TestCase):

    def test_loadSubjectEqT(self):
        self.assertEqual(1 + 2, 3, "1 + 2 not equal to 3")

    def test_loadSubjectEqF(self):
        self.assertEqual(1 + 2, 4, "1 + 2 not equal to 4")

if __name__ == '__main__':
    unittest.main()
