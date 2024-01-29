import unittest
import decide



class TestDecide(unittest.TestCase):
    def test_LIC0(self):
        decide.PARAMETERS["LENGTH1"] = 1
        decide.POINTS = [[0,2], [2,0]]
        decide.NUMPOINTS = len(decide.POINTS)
        lic0_result = decide.LIC0()
        self.assertTrue(lic0_result)
    
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

if __name__ == '__main__':
    unittest.main()