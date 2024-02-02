import unittest
import math
import sys
sys.path.append('../src')
import decide

class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)


    def test_LIC3(self):
       decide.PARAMETERS['AREA1'] = 2
       decide.POINTS = [[0, 0], [0, 0], [0, 4], [2, 5], [3, 7]]
       self.assertTrue(decide.LIC3())

    def test_LIC3_AREA1_big(self):
        decide.PARAMETERS['AREA1'] = 5
        decide.POINTS = [[0, 0], [0, 0], [0, 4], [2, 5], [3, 7]]
        self.assertFalse(decide.LIC3())

    def test_LIC4(self):
        decide.PARAMETERS['Q_PTS'] = 3
        decide.PARAMETERS['QUADS'] = 2
        decide.POINTS = [[0, 0], [-3, -5], [5, -4], [-2, 5], [3, 7]]
        self.assertTrue(decide.LIC4())

    def test_LIC5(self):
        decide.POINTS = [[0, 0], [3, -5], [5, -4], [-2, 5], [3, 7]]
        self.assertTrue(decide.LIC5())


    def test_LIC14_insufficient_points(self):
        decide.POINTS = [[0,2]]
        decide.NUMPOINTS = len(decide.POINTS)
        self.assertFalse(decide.LIC14())
    

    def test_LIC1(self):
        decide.PARAMETERS["RADIUS1"] = 1
        decide.POINTS = [[0,3],[0,-1],[1,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic1_result = decide.LIC1()
        self.assertTrue(lic1_result)
        
    def test_LIC2(self):
        decide.PARAMETERS["EPSILON"] = 0.174532925
        decide.POINTS = [[0,3],[0,0],[1,0]] # forms an angle of size pi/2 which is less than pi - epsilon
        decide.NUMPOINTS = len(decide.POINTS)
        lic2_result = decide.LIC2()
        self.assertTrue(lic2_result)

    
    def test_LIC14_no_condition_met(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA1"] = 25
        decide.PARAMETERS["AREA2"] = 5
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
    
    def test_LIC14_only_first_condition(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA1"] = 10
        decide.PARAMETERS["AREA2"] = 5
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
        
    def test_LIC14_only_second_condition(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA1"] = 20
        decide.PARAMETERS["AREA2"] = 14
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())
    
    def test_LIC14_both_conditions(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA1"] = 10
        decide.PARAMETERS["AREA2"] = 15
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertTrue(decide.LIC14())

    def test_LIC14_equal_areas(self):
        decide.POINTS = [[0, 0], [-2, 4], [7, -3], [2, -3], [6, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS["AREA1"] = 17.5
        decide.PARAMETERS["AREA2"] = 10
        decide.PARAMETERS["E_PTS"] = 0
        decide.PARAMETERS["F_PTS"] = 0
        self.assertFalse(decide.LIC14())



    def test_LIC9_True(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["C_PTS"] = 1
        decide.PARAMETERS["D_PTS"] = 1
        decide.PARAMETERS["EPSILON"] = math.pi / 2
        decide.POINTS=[[0, 0], [1,2], [0,0], [2,3], [3, 4]]
        lic9_result = decide.LIC9()
        self.assertTrue(lic9_result)

    def test_LIC9_False(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["C_PTS"] = 1
        decide.PARAMETERS["D_PTS"]= 1
        decide.PARAMETERS["EPSILON"] = math.pi * 4 / 5
        decide.POINTS = [[0,0], [1,1], [2,3], [3,1], [4,0]]
        lic9_result = decide.LIC9()
        self.assertFalse(lic9_result)
    
    def test_LIC9_low_numpoints_False(self):
        decide.NUMPOINTS = 2
        decide.PARAMETERS["C_PTS"] = 1
        decide.PARAMETERS["D_PTS"] = 1
        decide.PARAMETERS["EPSILON"] = math.pi / 2
        decide.POINTS = [[0, 0], [1,2], [0,0], [2,3], [3, 4]]
        lic9_result = decide.LIC9()
        self.assertFalse(lic9_result)
    
    def test_LIC10_True(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["E_PTS"] = 1
        decide.PARAMETERS["F_PTS"] = 1
        decide.PARAMETERS["AREA1"] = 5        
        decide.POINTS=[[0, 0], [1,3], [2,6], [3,3], [4, 0]]
        lic10_result = decide.LIC10()
        self.assertTrue(lic10_result)
        
    def test_LIC10_False(self):
        decide.NUMPOINTS = 5
        decide.PARAMETERS["E_PTS"] = 1
        decide.PARAMETERS["F_PTS"] = 1
        decide.PARAMETERS["AREA1"] = 12
        decide.POINTS = [[0, 0], [1,3], [2,6], [3,3], [4, 0]]
        lic10_result = decide.LIC10()
        self.assertFalse(lic10_result)
    
    def test_LIC10_low_numpoints_False(self):
        decide.NUMPOINTS = 4
        decide.PARAMETERS["E_PTS"] = 1
        decide.PARAMETERS["F_PTS"] = 1
        decide.PARAMETERS["AREA1"] = 5
        decide.POINTS=[[0, 0], [1,3], [2,6], [3,3], [4, 0]]
        lic10_result = decide.LIC10()
        self.assertFalse(lic10_result)


    def test_LIC11_True(self):    
        decide.PARAMETERS["G_PTS"] = 2
        decide.NUMPOINTS = 5
        decide.POINTS=[[1, 2], [3,5], [3,1], [3,1], [2, 1]]
        lic11_result = decide.LIC11()
        self.assertTrue(lic11_result)

    def test_LIC11_False(self):
        decide.PARAMETERS["G_PTS"] = 2
        decide.NUMPOINTS = 5        
        decide.POINTS=[[1,2], [3,5], [3,1], [4,1], [5, 1]]
        lic11_result = decide.LIC11()
        self.assertFalse(lic11_result)

    def test_LIC11_low_numpoints_False(self):
        decide.PARAMETERS["G_PTS"] = 2
        decide.NUMPOINTS = 2
        decide.POINTS = [[1,2], [3,5], [3,1], [3,1], [2,1]]
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
        
    def test_LIC7_num_not_error(self):
        """ failed: 1 ≤ K_PTS ≤ (NUMPOINTS − 2) """
        decide.POINTS = [[0, 0], [1, 1], [2, 2], [3, 3]]
        decide.NUMPOINTS = 4
        decide.PARAMETERS['K_PTS']  = 0
        decide.PARAMETERS['LENGTH1'] = 2
        self.assertRaises(AssertionError, decide.LIC7)

        
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
        
    def test_LIC6_DIST_error(self):
        """ failed: 0 ≤ DIST """
        decide.POINTS = [[2.0, 2.0], [1.0, 2.0], [1.0, 3.0]]
        decide.NUMPOINTS  = 3
        decide.PARAMETERS['N_PTS'] = 3
        decide.PARAMETERS['DIST'] = -1
        self.assertRaises(AssertionError, decide.LIC6)
        
    def test_LIC6_DIST_NPTS_error(self):
        """ failed: 3 ≤ N_PTS ≤ NUMPOINTS """
        decide.POINTS = [[2.0, 2.0], [1.0, 2.0], [1.0, 3.0]]
        decide.NUMPOINTS  = 3
        decide.PARAMETERS['N_PTS'] = 4
        decide.PARAMETERS['DIST'] = 3
        self.assertRaises(AssertionError, decide.LIC6)

        
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
        
        
    def test_LIC13_obtuse_triangle(self):
        decide.POINTS = [[0, 0], [0, 0], [50, 0], [0, 0], [25, 1]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 1
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 0.1
        decide.PARAMETERS['RADIUS2'] = 26
        self.assertTrue(decide.LIC13())
        
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

    
    def test_FUV_1_false(self):
        """Example 1: Test FUV[0] is False because PUV[0] is True and PUM[0,1] and PUM[0,3] are False"""
        decide.PUV = [True for _ in range(15)]
        PUM = [[False] * 15 for _ in range(15)]
        FUV_result = decide.generate_FUV(PUM)
        self.assertFalse(FUV_result[0])

    def test_FUV_2_true(self):
        """Example 2: Test FUV[1] is True because PUV[1] is False"""
        decide.PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]
        FUV_result = decide.generate_FUV(PUM)
        self.assertTrue(FUV_result[1])  # Test FUV[1] is True because PUV[1] is False

    def test_FUV_3_true(self):
        """Example 3: Test FUV[2] is True because PUV[2] is False and PUM[2,i] is True for all i != 2"""
        decide.PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]
        FUV_result = decide.generate_FUV(PUM)
        self.assertTrue(FUV_result[2])

    def testFUV_variation(self):
        """ Test: PUV[1] is False and all PUM[1][i] are False, leading to FUV[1] being True"""
        decide.PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]

        decide.PUV[1] = False
        FUV_result = decide.generate_FUV(PUM)
        self.assertTrue(FUV_result[1])

    def test_FUV_variation2(self):
        """Test: PUV[1] is True and all PUM[1][i] are False, leading to FUV[1] being False"""
        decide.PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]
        decide.PUV[1] = True
        FUV_result = decide.generate_FUV(PUM)
        self.assertFalse(FUV_result[1])

    def test_FUV_variation3(self):
        """ Test: PUV[1] is False and all PUM[1][i] are True, leading to FUV[1] being True """

        decide.PUV = [False] * 15
        PUM = [[False] * 15 for _ in range(15)]
        decide.PUV[1] = False
        for i in range(len(PUM[1])):
            PUM[1][i] = True
        FUV_result = decide.generate_FUV(PUM)
        self.assertTrue(FUV_result[1])
        

    def test_LIC8_aPTS_error(self):
        """ Assertion failed: 1 ≤ A_PTS"""
        decide.POINTS = [[1.0, 0.0],[0.0, 0.0], [3.0, 0.0],[4.0, 0.0], [0, 0]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 0
        decide.PARAMETERS['B_PTS'] = 1
        decide.PARAMETERS['RADIUS1'] = 2
        self.assertRaises(AssertionError, decide.LIC8)
        
    def test_LIC8_LEN_error(self):
        """ failed: A_PTS + B_PTS ≤ (NUMPOINTS − 3)"""
        decide.POINTS = [[1.0, 0.0],[0.0, 0.0], [3.0, 0.0],[4.0, 0.0], [0, 0]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['A_PTS'] = 2
        decide.PARAMETERS['B_PTS'] = 2
        decide.PARAMETERS['RADIUS1'] = 2
        self.assertRaises(AssertionError, decide.LIC8)


            
    def test_PUM_orr(self):
        """Test with all LCM elements as ORR and two CMV element as True."""
        cmv = [False for _ in range(15)]
        first_value = 2
        cmv[first_value] = True
        
        second_value = 8
        cmv[second_value] = True

        decide.LCM = [[2 for _ in range(len(cmv))] for _ in range(len(cmv))]

        generated_outcome = decide.generate_PUM(cmv)

        expected_outcome = [[False for _ in range(len(cmv))] for _ in range(len(cmv))]
        for i in range(len(cmv)):
            expected_outcome[i][first_value] = True
            expected_outcome[first_value][i] = True
            expected_outcome[i][second_value] = True
            expected_outcome[second_value][i] = True

        self.assertListEqual(expected_outcome, generated_outcome)


    def test_PUM_andd(self):
        """Test with all LCM elements as ANDD and two CMV elements as True."""
        cmv = [False for _ in range(15)]
        first_value = 2
        second_value = 8

        cmv[first_value] = True
        cmv[second_value] = True
      
        decide.LCM = [[1 for _ in range(len(cmv))] for _ in range(len(cmv))]

        generated_outcome = decide.generate_PUM(cmv)

        expected_outcome = [[False for _ in range(len(cmv))] for _ in range(len(cmv))]
        for i in [first_value, second_value]:
            expected_outcome[i][i] = True
        expected_outcome[first_value][second_value] = True
        expected_outcome[second_value][first_value] = True

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

    def test_launch_last_true(self):
        FUV = []
        for i in range(14):
            FUV.append(False)
        FUV.append(True)
        self.assertFalse(decide.launch(FUV))


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


  
    
    def test_CMV(self):
        decide.POINTS = [[1.0, 0.0],[0.0, 0.0], [3.0, 0.0],[4.0, 0.0], [0, 0]]
        decide.NUMPOINTS = len(decide.POINTS)
        decide.PARAMETERS['LENGTH1'] = 1
        decide.PARAMETERS['RADIUS1'] = 1
        decide.PARAMETERS['EPSILON'] = 2
        decide.PARAMETERS['AREA1']  = 2
        decide.PARAMETERS['Q_PTS']  = 4
        decide.PARAMETERS['QUADS']  = 1
        decide.PARAMETERS['DIST']   = 4
        decide.PARAMETERS['N_PTS']  = 3
        decide.PARAMETERS['K_PTS']  = 1
        decide.PARAMETERS['A_PTS']  = 1
        decide.PARAMETERS['B_PTS']  = 1
        decide.PARAMETERS['C_PTS']  = 1
        decide.PARAMETERS['D_PTS']  = 1
        decide.PARAMETERS['E_PTS']  = 1
        decide.PARAMETERS['F_PTS']  = 1
        decide.PARAMETERS['G_PTS'] = decide.NUMPOINTS-2
        decide.PARAMETERS['LENGTH2'] = 3
        decide.PARAMETERS['RADIUS2'] = 2
        decide.PARAMETERS['AREA2'] = 5
        try:
            decide.CMV()
        except Exception:
            self.fail()

        


if __name__ == '__main__':
    unittest.main()
