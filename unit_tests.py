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



if __name__ == '__main__':
    unittest.main()