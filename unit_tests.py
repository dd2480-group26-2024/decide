import unittest
import decide



class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)
    

    def test_LIC12_insufficient_points(self):
        decide.POINTS = [[0,2]]
        decide.NUMPOINTS = len(decide.POINTS)
        self.assertFalse(decide.LIC12())

    def test_LIC12_no_condition_met(self):
        decide.POINTS = [[0,2], [0,4], [0,6]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["LENGTH1"] = 10
        decide.PARAMETERS["LENGTH2"] = 1
        decide.PARAMETERS["K_PTS"] = 0
        self.assertFalse(decide.LIC12())

    def test_LIC12_only_first_condition(self):
        decide.POINTS = [[0,2], [0,4], [0,6]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["LENGTH1"] = 1
        decide.PARAMETERS["LENGTH2"] = 1
        decide.PARAMETERS["K_PTS"] = 0
        self.assertFalse(decide.LIC12())

    def test_LIC12_only_second_condition(self):
        decide.POINTS = [[0,2], [0,4], [0,6]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["LENGTH1"] = 10
        decide.PARAMETERS["LENGTH2"] = 10
        decide.PARAMETERS["K_PTS"] = 0
        self.assertFalse(decide.LIC12())

    def test_LIC12_both_conditions(self):
        decide.POINTS = [[0,2], [0,4], [0,6]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["LENGTH1"] = 1
        decide.PARAMETERS["LENGTH2"] = 10
        decide.PARAMETERS["K_PTS"] = 0
        self.assertTrue(decide.LIC12())
       
    def test_LIC12_equal_lengths(self):
        decide.POINTS = [[0,2], [0,4], [0,6]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["LENGTH1"] = 2
        decide.PARAMETERS["LENGTH2"] = 2
        decide.PARAMETERS["K_PTS"] = 0
        self.assertFalse(decide.LIC12())
    




if __name__ == '__main__':
    unittest.main()