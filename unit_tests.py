import unittest
import decide



class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)
        
 
    def test_LIC7_satisfied(self):
        """ Test if LIC7 is true when there exists a pair of points more than LENGTH1 units apart """
        decide.POINTS = [[0, 0], [1, 1], [2, 2], [4, 4]]
        decide.NUMPOINTS = 4
        decide.PARAMETERS['K_PTS'] = 1
        decide.PARAMETERS['LENGTH1'] = 2
        self.assertTrue(decide.LIC7())

    def test_LIC7_not_satisfied(self):
        """ Test if LIC7 is false when no pair of points is more than LENGTH1 units apart """
        decide.POINTS = [[0, 0], [1, 1], [2, 2], [3, 3]]
        decide.NUMPOINTS = 4
        decide.PARAMETERS['K_PTS'] = 1
        decide.PARAMETERS['LENGTH1'] = 3
        self.assertFalse(decide.LIC7())

    def test_LIC7_num_not_satisfied(self):
        """ Test if LIC7 is false when the number of points is less than 3 """
        decide.POINTS = [[0, 0], [1, 1]]
        decide.NUMPOINTS = 2
        decide.PARAMETERS['K_PTS']  = 1
        decide.PARAMETERS['LENGTH1'] = 2
        self.assertFalse(decide.LIC7())

    def test_LIC7_k_pts_invalid(self):
        """ Test if LIC7 is false when K_PTS is outside the valid range """
        decide.POINTS = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        decide.NUMPOINTS = 5
        decide.PARAMETERS['K_PTS'] = 4 
        decide.PARAMETERS['LENGTH1'] = 2
        self.assertFalse(decide.LIC7())
        
    def test_LIC6_satisfied(self):
        """ Test if LIC6 is true when the distance meets the requirement """
        decide.POINTS = [[2.0, 2.0], [3.0, 1.0], [3.0, 3.0]]
        decide.NUMPOINTS = 3
        decide.PARAMETERS['N_PTS'] = 3
        decide.PARAMETERS['DIST'] = 1
        self.assertTrue(decide.LIC6())

    def test_LIC6_not_satisfied(self):
        """ Test if LIC6 is false when the distance doesn't meet the requirement """
        decide.POINTS = [[2.0, 2.0], [1.0, 2.0], [1.0, 3.0]]
        decide.NUMPOINTS = 3
        decide.PARAMETERS['N_PTS'] = 3
        decide.PARAMETERS['DIST'] = 1
        self.assertFalse(decide.LIC6())

    def test_LIC6_num_not_satisfied(self):
        """ Test if LIC6 is false when the number of points is less than 3 """
        decide.POINTS = [[1.0, 1.0], [2.0, 2.0]]

        decide.NUMPOINTS  = 2
        decide.PARAMETERS['N_PTS'] = 3
        decide.PARAMETERS['DIST'] = 0.5
        self.assertFalse(decide.LIC6())
        
    def test_LIC8_not_satisfied(self):
        """ Test LIC8 a triangle"""
        # Setup for triangle
        decide.POINTS = [[0.0, 0.0],[0.0, 0.0], [3.0, 0.0],[0.0, 0.0], [1, 2]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 2
        result = decide.LIC8()

        self.assertFalse(result)
        
    def test_LIC8_satisfied(self):
        """ Test LIC8 a triangle"""
        decide.POINTS = [[0.0, 0.0],[0.0, 0.0], [3.0, 0.0],[0.0, 0.0], [1, 2]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 1.5
        result = decide.LIC8()
        self.assertTrue(result)

    def test_LIC8_not_satisfied(self):
            """ Test LIC8 on a straght line"""
            decide.POINTS = [[1.0, 0.0],[0.0, 0.0], [3.0, 0.0],[4.0, 0.0], [0, 0]]
            decide.NUMPOINTS = len(decide.POINTS)
            decide.PARAMETERS['A_PTS'] = 1
            decide.PARAMETERS['B_PTS'] = 1
            decide.PARAMETERS['RADIUS1'] = 2
            result = decide.LIC8()
            self.assertFalse(result)
            
    def test_LIC13_insufficient_points(self):
        decide.POINTS = [[0,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        self.assertFalse(decide.LIC13())
        
    def test_LIC13_no_condition_met(self):
        decide.POINTS = [[0, 0], [0, 0], [3, 0], [0, 0], [1, 2]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 100
        decide.PARAMETERS['RADIUS2'] = 0.1
        self.assertFalse(decide.LIC13())
        
    def test_LIC13_only_first_condition_met(self):
        decide.POINTS = [[0, 0], [0, 0], [3, 0], [0, 0], [1, 2]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 0.1
        decide.PARAMETERS['RADIUS2'] = 0.1
        self.assertFalse(decide.LIC13())
        
    def test_LIC13_only_second_condition_met(self):
        decide.POINTS = [[0, 0], [0, 0], [3, 0], [0, 0], [1, 2]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 100
        decide.PARAMETERS['RADIUS2'] = 100
        self.assertFalse(decide.LIC13())
        
    def test_LIC13_both_conditions_met(self):
        decide.POINTS = [[0, 0], [0, 0], [3, 0], [0, 0], [1, 2]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 0.1
        decide.PARAMETERS['RADIUS2'] = 100
        self.assertTrue(decide.LIC13())
        
    def test_LIC13_edge_case_first_condition(self):
        decide.POINTS = [[0, 0], [0, 0], [4, 0], [0, 0], [4, 3]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 2.5
        decide.PARAMETERS['RADIUS2'] = 100
        self.assertFalse(decide.LIC13())
        
    def test_LIC13_edge_case_second_condition(self):
        decide.POINTS = [[0, 0], [0, 0], [4, 0], [0, 0], [4, 3]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 0.1
        decide.PARAMETERS['RADIUS2'] = 2.5
        self.assertTrue(decide.LIC13())

if __name__ == '__main__':
    unittest.main()