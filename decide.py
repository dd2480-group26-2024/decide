import math
PUV = [True for _ in range(15)]

# 0 = NOTUSED 
# 1 = ANDD 
# 2 = ORR
LCM = []
for row in range(14):    
    a = []
    for column in range(14):   
        a.append(int(0))
    LCM.append(a)

PARAMETERS = {
    "LENGTH1" : 0.0, # Length in LICs 0 , 7 , 12
    "RADIUS1" : 0.0, # Radius in LICs 1 , 8 , 13
    "EPSILON" : 0.0, # Deviation from PI in LICs 2, 9
    "AREA" : 0.0,    # Area in LICs 3, 10, 14
    "Q_PTS" : 0,     # No. of consecutive points in LIC 4
    "QUADS" : 0,     # No. of quadrants in LIC 4
    "DIST" : 0.0,    # Distance in LIC 6
    "N_PTS" : 0,     # No. of consecutive pts. in LIC 6
    "K_PTS" : 0,     # No. of  int. pts. in LICs 7 , 12
    "A_PTS" : 0,     # No. of int. pts. in L ICs 8 , 13
    "B_PTS" : 0,     # No. of int. pts. in L ICs 8 , 13
    "C_PTS" : 0,     # No. of int. pts. i n LIC 9
    "D_PTS" : 0,     # No. of int. pts. i n LIC 9
    "E_PTS" : 0,     # No. of int. pts. in LICs 10 , 14
    "F_PTS" : 0,     # No. of int. pts. in LICs 10 , 14
    "G_PTS" : 0,     # No. of int. pts. in LICs 11
    "LENGTH2" : 0.0, # Maximum length in LIC 12
    "RADIUS2" : 0.0, # Maximum radius in LIC 13
    "AREA2" : 0.0    # Maximum area in LIC 14
}

POINTS = []



NUMPOINTS = len(POINTS)


def circumradius(p1, p2, p3):
    """    Calculates the radius of the circumcircle of a triangle defined by three points.     """
    a = math.dist(p1, p2)
    b = math.dist(p2, p3)
    c = math.dist(p3, p1)
    area = math.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))
    radius = a * b * c / area
    return radius


def can_fit_in_circle(p1, p2, p3, radius):
    """    Checks if the triangle formed by three points can fit inside a circle of a given radius.     """
    calculated_radius = circumradius(p1, p2, p3)
    return calculated_radius <= radius



def LIC8(points=POINTS, NUMPOINTS=NUMPOINTS, A_PTS=PARAMETERS["A_PTS"], B_PTS=PARAMETERS["B_PTS"], RADIUS1=PARAMETERS["RADIUS1"]):
    if NUMPOINTS < 5 or A_PTS + B_PTS > NUMPOINTS - 3 or A_PTS<1 or B_PTS<1:
        return False

    for i in range(NUMPOINTS - (A_PTS + B_PTS + 2)):
        p1 = points[i]
        p2 = points[i + A_PTS + 1]
        p3 = points[i + A_PTS + B_PTS + 2]

        if not can_fit_in_circle(p1, p2, p3, RADIUS1):
            return True

    return False