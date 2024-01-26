import unittest
import decide



class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)
    

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



if __name__ == '__main__':
    unittest.main()