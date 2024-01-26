import unittest
import decide



class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)

    def test_LIC14_insufficient_points(self):
        decide.POINTS = [[0,2]]
        decide.NUMPOINTS = len(decide.POINTS)
        self.assertFalse(decide.LIC14())
    
    
    def test_LIC14_no_condition_met(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA"] = 25
        decide.PARAMETERS["AREA2"] = 5
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
    
    def test_LIC14_only_first_condition(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA"] = 10
        decide.PARAMETERS["AREA2"] = 5
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
        
    def test_LIC14_only_second_condition(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA"] = 20
        decide.PARAMETERS["AREA2"] = 14
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
    
    def test_LIC14_both_conditions(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA"] = 10
        decide.PARAMETERS["AREA2"] = 15
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertTrue(decide.LIC14())

    def test_LIC14_equal_areas(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA"] = 17.5
        decide.PARAMETERS["AREA2"] = 10
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
    




if __name__ == '__main__':
    unittest.main()