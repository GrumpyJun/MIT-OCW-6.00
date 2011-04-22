import unittest
import ps8

class TestPS8_loadSubjects(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.subj_dict_comp = {"2.00":(5,9), "2.01":(2,2), "2.02":(1,17)}
        self.subj_dict = ps8.loadSubjects("test_input.txt")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    # Make sure the dictionaries are the same length
    def test_loadSubjects_length(self):
        self.assertEqual(len(self.subj_dict_comp), len(self.subj_dict))

    # Make sure all of the keys match
    def test_loadSubjects_keys(self):
        for key in self.subj_dict_comp.keys():
            self.assertTrue(key in self.subj_dict.keys(), "Key " + str(key) + " is not in the subject dictionary.  Dictionary contains " + str(self.subj_dict_comp.keys()))

    # Make sure all the first entries of the tuple of each dictionary entry match
    def test_loadSubjects_firstTupleEntries(self):
        for key in self.subj_dict_comp.keys():
            self.assertEqual(self.subj_dict_comp[key][0], self.subj_dict[key][0], "Tuple entries 0 from key " + str(key) + " don't match.  They are " + str(self.subj_dict_comp[key][0]) + " and " + str(self.subj_dict_comp[key][0]))

    # Make sure all the second entries of the tuple of each dictionary entry match
    def test_loadSubjects_secondTupleEntries(self):
        for key in self.subj_dict_comp.keys():
            self.assertEqual(self.subj_dict_comp[key][1], self.subj_dict[key][1], "Tuple entries 1 from key " + str(key) + " don't match.  They are " + str(self.subj_dict_comp[key][1]) + " and " + str(self.subj_dict_comp[key][1]))

class TestPS8_greedyAdvisor(unittest.TestCase):
    def dictsAreIdentical(self, dict1, dict2):
        # Make sure they are the same length
        if len(dict1) != len(dict2):
            return False

        # Make sure keys are identical
        for key in dict1.keys():
            if key not in dict2.keys():
                return False

        # Make sure tuples are the same
        for key in dict1.keys():
            if dict1[key][0] != dict2[key][0] or dict1[key][1] != dict2[key][1]:
                return False

        return True

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.input_dict = {"6.00":(16,8), "1.00":(7,7), "6.01":(5,3), "15.01":(9,6)}

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_greedyAdvisor_cmpValue(self):
        self.solved_dict = {'6.00': (16, 8),'15.01': (9, 6)}
        self.returned_dict = ps8.greedyAdvisor(self.input_dict, 15, ps8.cmpValue)
        self.assertTrue(self.dictsAreIdentical(self.solved_dict, self.returned_dict))

    def test_greedyAdvisor_cmpWork(self):
        self.solved_dict = {'6.01': (5, 3),'15.01': (9, 6)}
        self.returned_dict = ps8.greedyAdvisor(self.input_dict, 15, ps8.cmpWork)
        self.assertTrue(self.dictsAreIdentical(self.solved_dict, self.returned_dict))

    def test_greedyAdvisor_cmpValue(self):
        self.solved_dict = {'6.00': (16, 8),'6.01': (5, 3)}
        self.returned_dict = ps8.greedyAdvisor(self.input_dict, 15, ps8.cmpRatio)
        self.assertTrue(self.dictsAreIdentical(self.solved_dict, self.returned_dict))

if __name__ == '__main__':
    unittest.main()
