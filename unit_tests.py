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
    
    def test_FUV_1_false(self):
        """Example 1: Test FUV[0] is False because PUV[0] is True and PUM[0,1] and PUM[0,3] are False"""
        PUM = [[False] * 15 for _ in range(15)]
        FUV_result = decide.generate_FUV(PUM, decide.PUV)
        self.assertFalse(FUV_result[0])

    def test_FUV_2_true(self):
        """Example 2: Test FUV[1] is True because PUV[1] is False"""
        PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]
        FUV_result = decide.generate_FUV(PUM, PUV)
        self.assertTrue(FUV_result[1])  # Test FUV[1] is True because PUV[1] is False

    def test_FUV_3_true(self):
        """Example 3: Test FUV[2] is True because PUV[2] is False and PUM[2,i] is True for all i != 2"""
        PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]
        FUV_result = decide.generate_FUV(PUM, PUV)
        self.assertTrue(FUV_result[2])

    def test_FUV_variations(self):
        """Test different variations of FUV based on PUV and PUM settings"""
        PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]

        # Test case 1: PUV[1] is False and all PUM[1][i] are False, leading to FUV[1] being True
        PUV[1] = False
        FUV_result = decide.generate_FUV(PUM, PUV)
        self.assertTrue(FUV_result[1])

        # Test case 2: PUV[1] is True and all PUM[1][i] are False, leading to FUV[1] being False
        PUV[1] = True
        FUV_result = decide.generate_FUV(PUM, PUV)
        self.assertFalse(FUV_result[1])

        # Test case 3: PUV[1] is False and all PUM[1][i] are True, leading to FUV[1] being True
        PUV[1] = False
        for i in range(len(PUM[1])):
            PUM[1][i] = True

        FUV_result = decide.generate_FUV(PUM, PUV)
        self.assertTrue(FUV_result[1])

if __name__ == '__main__':
    unittest.main()