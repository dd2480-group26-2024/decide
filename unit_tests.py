import unittest
import decide
import math
import random

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
    
    def test_LIC9_low_numpoints_False(self):
        decide.NUMPOINTS = 2
        decide.PARAMETERS["C_PTS"] = 1
        decide.PARAMETERS["D_PTS"] = 1
        decide.PARAMETERS["EPSILON"] = math.pi / 2
        decide.X = [0, 1, 0, 2, 3]
        decide.Y = [0, 2, 0, 3, 4]
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
    
    def test_LIC10_low_numpoints_False(self):
        decide.NUMPOINTS = 4
        decide.PARAMETERS["E_PTS"] = 1
        decide.PARAMETERS["F_PTS"] = 1
        decide.PARAMETERS["AREA1"] = 5
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

    def test_LIC11_low_numpoints_False(self):
        decide.PARAMETERS["G_PTS"] = 2
        decide.NUMPOINTS = 2
        decide.X = [1, 3, 3, 3, 2]
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
            
            
    def test_PUM_orr(self):
        """Test with all LCM elements as ORR and two random CMV element as True."""
        cmv = [False for _ in range(15)]
        random_number_1 = random.randint(0, 6)
        cmv[random_number_1] = True
        
        random_number_2 = random.randint(7, 14)
        cmv[random_number_2] = True

        decide.LCM = [[2 for _ in range(len(cmv))] for _ in range(len(cmv))]

        generated_outcome = decide.generate_PUM(cmv)

        expected_outcome = [[False for _ in range(len(cmv))] for _ in range(len(cmv))]
        for i in range(len(cmv)):
            expected_outcome[i][random_number_1] = True
            expected_outcome[random_number_1][i] = True
            expected_outcome[i][random_number_2] = True
            expected_outcome[random_number_2][i] = True

        self.assertListEqual(expected_outcome, generated_outcome)


    def test_PUM_andd(self):
        """Test with all LCM elements as ANDD and two random CMV elements as True."""
        cmv = [False for _ in range(15)]
        random_number_1 = random.randint(0, 6)
        random_number_2 = random.randint(7, 14)

        cmv[random_number_1] = True
        cmv[random_number_2] = True
      
        decide.LCM = [[1 for _ in range(len(cmv))] for _ in range(len(cmv))]

        generated_outcome = decide.generate_PUM(cmv)

        expected_outcome = [[False for _ in range(len(cmv))] for _ in range(len(cmv))]
        for i in [random_number_1, random_number_2]:
            expected_outcome[i][i] = True
        expected_outcome[random_number_1][random_number_2] = True
        expected_outcome[random_number_2][random_number_1] = True

        self.assertListEqual(expected_outcome, generated_outcome)

    def test_PUM_notused(self):
        """Test with all LCM elements as NOTUSED."""
        cmv = [False for _ in range(15)]
        decide.LCM = [[0 for _ in range(len(cmv))] for _ in range(len(cmv))]

        generated_outcome = decide.generate_PUM(cmv)
        expected_outcome = [[True for _ in range(len(cmv))] for _ in range(len(cmv))]

        self.assertListEqual(expected_outcome, generated_outcome)

    def test_launch_all_false(self):
        FUV = []
        for i in range(15):
            FUV.append(False)
        self.assertFalse(decide.launch(FUV))

    def test_launch_last_true(self):
        FUV = []
        for i in range(14):
            FUV.append(False)
        FUV.append(True)
        self.assertFalse(decide.launch(FUV))


    def test_launch_first_true(self):
        FUV = []
        FUV.append(True)
        for i in range(14):
            FUV.append(False)
        self.assertFalse(decide.launch(FUV))

    def test_launch_all_true(self):
        FUV = []
        for i in range(15):
            FUV.append(True)
        self.assertTrue(decide.launch(FUV))


if __name__ == '__main__':
    unittest.main()
