import unittest
import decide
import math


class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)

    def test_LIC9_True(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["C_PTS"] = 1
        decide.PARAMETERS["D_PTS"] = 1
        decide.PARAMETERS["EPSILON"] = math.pi / 2
        decide.X = [0, 1, 0, 2, 3]
        decide.Y = [0, 2, 0, 3, 4]
        lic9_result = decide.LIC9()
        self.assertTrue(lic9_result)

    def test_LIC9_False(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["C_PTS"] = 1
        decide.PARAMETERS["D_PTS"]= 1
        decide.PARAMETERS["EPSILON"] = math.pi * 4 / 5
        decide.X = [0, 1, 2, 3, 4]
        decide.Y = [0, 1, 3, 1, 0]
        lic9_result = decide.LIC9()
        self.assertFalse(lic9_result)
    
    def test_LIC10_True(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["E_PTS"] = 1
        decide.PARAMETERS["F_PTS"] = 1
        decide.PARAMETERS["AREA1"] = 5
        decide.X = [0, 1, 2, 3, 4]
        decide.Y = [0, 3, 6, 3, 0]
        lic10_result = decide.LIC10()
        self.assertTrue(lic10_result)
        
    def test_LIC10_False(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["E_PTS"] = 1
        decide.PARAMETERS["F_PTS"] = 1
        decide.PARAMETERS["AREA1"] = 12
        decide.X = [0, 1, 2, 3, 4]
        decide.Y = [0, 3, 6, 3, 0]
        lic10_result = decide.LIC10()
        self.assertFalse(lic10_result)

    def test_LIC11_True(self):    
        decide.PARAMETERS["G_PTS"] = 2
        decide.NUMPOINTS = 5
        decide.X = [1, 3, 3, 3, 2]
        decide.Y = [2, 5, 1, 1, 1]
        lic11_result = decide.LIC11()
        self.assertTrue(lic11_result)

    def test_LIC11_False(self):
        decide.PARAMETERS["G_PTS"] = 2
        decide.NUMPOINTS = 5
        decide.X = [1, 3, 3, 4, 5]
        decide.Y = [2, 5, 1, 1, 1]
        lic11_result = decide.LIC11()
        self.assertFalse(lic11_result)




if __name__ == '__main__':
    unittest.main()