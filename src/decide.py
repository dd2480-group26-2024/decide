import math
import itertools

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
    "AREA1" : 0.0,   # Area in LICs 3, 10, 14
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

def distance_point_to_line(point, line_start, line_end):
    """Calculates the distance from a point to a line defined by two points."""
    
    if line_start == line_end:
        return math.sqrt((point[0] - line_start[0])**2 + (point[1] - line_start[1])**2)
    
    num = abs((line_end[1] - line_start[1]) * point[0] - (line_end[0] - line_start[0]) * point[1] + line_end[0] * line_start[1] - line_end[1] * line_start[0])
    den = math.sqrt((line_end[0] - line_start[0])**2 + (line_end[1] - line_start[1])**2)
    return num / den
  
def calculate_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def calculate_angle(point1, point2, point3):
    # create the vectors whose angle we want
    vector1 = (point1[0] - point2[0], point1[1] - point2[1]) 
    vector2 = (point3[0] - point2[0], point3[1] - point2[1])
    
    # The dot product formula says v1 dot v2 = |v1||v2|*cos(theta), where theta is the angle and v1 and v2 are the vectors
    # So cos(theta) = v1 dot v2 / (|v1||v2|) and theta = arccos (v1 dot v2 / (|v1||v2|))
    dot_product = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    magnitude_v1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
    magnitude_v2 = math.sqrt(vector2[0]**2 + vector2[1]**2)
    angle = math.acos(dot_product/(magnitude_v1*magnitude_v2)) # angle in radians
        
    return angle

def calculate_triangle_area(point1, point2, point3):
    assert 2 == len(point1) == len(point2) == len(point3), "Incorrect format for a point. A point must have 2 coordinates."
    # Area of a triangle:  |(x2 - x1)(y3 - y1) - (x3 - x1)*(y2 - y1)| / 2
    return abs((point2[0] - point1[0])*(point3[1] - point1[1]) - (point3[0] - point1[0])*(point2[1] - point1[1])) / 2

def circumradius(p1, p2, p3):
    a = math.dist(p1, p2)
    b = math.dist(p2, p3)
    c = math.dist(p3, p1)
    
    largest_angle = max([calculate_angle(p1,p2,p3), calculate_angle(p2,p3,p1), calculate_angle(p3,p1,p2)])
    if largest_angle >= math.pi/2:
        return max([a, b, c])/2
    """    Calculates the radius of the circumcircle of a triangle defined by three points.     """
    area = math.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))
    if area == 0:
        return max(a,b,c)/2
    radius = a * b * c / area
    return radius

def can_fit_in_circle(p1, p2, p3, radius):
    """    Checks if the triangle formed by three points can fit inside a circle of a given radius.     """
    calculated_radius = circumradius(p1, p2, p3)

    return calculated_radius <= radius

def distance(p1, p2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def distance_point_to_line(point, line_start, line_end):
    """Calculates the distance from a point to a line defined by two points."""
    
    if line_start == line_end:
        return math.sqrt((point[0] - line_start[0])**2 + (point[1] - line_start[1])**2)
    
    num = abs((line_end[1] - line_start[1]) * point[0] - (line_end[0] - line_start[0]) * point[1] + line_end[0] * line_start[1] - line_end[1] * line_start[0])
    den = math.sqrt((line_end[0] - line_start[0])**2 + (line_end[1] - line_start[1])**2)
    return num / den

def triangle_area_vs_area1(x1, y1, x2, y2, x3, y3, a1):
    """Calculates the triangle area with coordinates and compares it with AREA1 in PARAMETERS"""
    return abs(x1 * (y2-y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5 > a1


def LIC0():
    """There exists at least one set of two consecutive data points that are a distance greater than the length, LENGTH1, apart."""
    assert PARAMETERS["LENGTH1"] >= 0, "LENGTH1 is < 0"
    
    for i in range(NUMPOINTS-1):
        if calculate_distance(POINTS[i], POINTS[i+1]) > PARAMETERS["LENGTH1"]:
            return True
    return False

def LIC1():
    """There exists at least one set of three consecutive data points that cannot all be contained
       within or on a circle of radius RADIUS1."""
    assert PARAMETERS["RADIUS1"] >= 0, "RADIUS1 < 0"    
    for i in range(NUMPOINTS-2):
        if not can_fit_in_circle(POINTS[i],POINTS[i+1], POINTS[i+2], PARAMETERS["RADIUS1"]):
            return True
    return False

def LIC2():
    """Three consecutive points create an angle satisfying either angle < (π - EPSILON) or angle > (π + EPSILON),
       with the middle point as the vertex. If the first or last point coincides with the vertex."""
    assert 0 <= PARAMETERS["EPSILON"] and PARAMETERS["EPSILON"] < math.pi, "EPSILON less than 0 or >= pi"
    for i in range(NUMPOINTS-2):
        if POINTS[i] == POINTS[i+1] or POINTS[i+2] == POINTS[i+1]:
            continue
        angle = calculate_angle(POINTS[i], POINTS[i+1], POINTS[i+2])
        if angle > math.pi + PARAMETERS["EPSILON"] or angle < math.pi - PARAMETERS["EPSILON"]:
            return True
    return False

def LIC3():
    """Checks that there exists one set of three consecutive data points that are the vertices of a triangle
       with area greater than AREA1."""
    ps = POINTS
    while len(ps) >= 3:
        # Setup the x_i and y_i coordinates of three consequtive points
        point1 = ps[0]; x1=point1[0]; y1=point1[1]
        point2 = ps[1]; x2=point2[0]; y2=point2[1]
        point3 = ps[2]; x3=point3[0]; y3=point3[1]
        # If the area of the three points is larger than AREA1 then we're done
        if (0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) > PARAMETERS["AREA1"]:
            return True
        # Iterate by removing the head of points
        ps = ps[1:]
    return False

def LIC4():
    """Checks that there is at least one set of Q_PTS nr of consequtive data points that 
       are inside more than QUADS nr of quadrants."""
    # Setup variables
    ps = POINTS
    quadrant=[False,False,False,False]
    # Inner helper functions
    def reset_quadrant():
        for i in quadrant:
            i = False
    # Count how many quadrants have points
    def count_quads():
        q = 0
        for i in quadrant:
            if i == True:
                q +=1
        return q
   # Main calculation
    while len(ps) >= PARAMETERS["Q_PTS"]:
        for p in ps[:PARAMETERS["Q_PTS"]]: # Reduce array to the first Q_PTS elements
            x=p[0];y=p[1]
            if x>=0 and y>=0: quadrant[0]=True    # lies in quadrant I
            elif x<0 and y>=0: quadrant[1]=True   # lies in quadrant II
            elif x<=0 and y<0: quadrant[2]=True   # lies in quadrant III
            else: quadrant[3]=True                # lies in quadrant IV
        if count_quads() > PARAMETERS["QUADS"]:
            return True
        reset_quadrant()
        # Iterate by removing the head of points
        ps = ps[1:]
    return False

def LIC5():
    """There exists at least one set of two consecutive data points, 
        (X[i],Y[i]) and (X[j],Y[j]), such that X[j] - X[i] < 0"""
    ps=POINTS
    while len(ps) >= 2:
        xi=ps[0][0];
        xj=ps[1][0];
        if xj - xi < 0:
            return True
        ps = ps[1:] # iterate by removing the head of points
    return False
  
def LIC6():
    """For at least three data points, some consecutive points, 
       defined by N PTS, include at least one point lying a distance greater than DIST from the line joining the first and last points. 
       If the first and last points coincide, the distance is measured from that point to all others in the set."""
    if NUMPOINTS < 3:
        return False
    
    assert 3 <= PARAMETERS["N_PTS"] <= NUMPOINTS, "Assertion failed: 3 ≤ N_PTS ≤ NUMPOINTS"
    assert  0 <= PARAMETERS["DIST"], "Assertion failed: 0 ≤ DIST"
    for i in range(NUMPOINTS - PARAMETERS['N_PTS'] + 1):
        subset = POINTS[i:i + PARAMETERS['N_PTS']]
        line_start, line_end = subset[0], subset[-1]

        for point in subset:
            if distance_point_to_line(point, line_start, line_end) > PARAMETERS['DIST']:
                return True
    return False

def LIC7():
    """For a given set of at least three data points, there exists a condition where two points, 
       separated by exactly K_PTS consecutive intervening points, 
       are a distance greater than LENGTH1 apart"""
    if NUMPOINTS < 3:
        return False
  
    assert 1 <= PARAMETERS["K_PTS"] <= (NUMPOINTS - 2), "Assertion failed: 1 ≤ K_PTS ≤ (NUMPOINTS − 2)"

    for i in range(NUMPOINTS - PARAMETERS["K_PTS"] - 1):
        p1 = POINTS[i]
        p2 = POINTS[i + PARAMETERS["K_PTS"] + 1]
        distance = calculate_distance(p1,p2)
        if distance > PARAMETERS['LENGTH1']:
            return True

    return False

def LIC8():
    """There exists at least one set of three data points separated by exactly A_PTS and B_PTS
       consecutive intervening points, respectively, that cannot be contained within or on a circle of
       radius RADIUS1. The condition is not met when NUMPOINTS < 5."""
    if NUMPOINTS < 5:
        return False
    assert 1 <= PARAMETERS["A_PTS"], "Assertion failed: 1 ≤ A_PTS"
    assert 1 <= PARAMETERS["B_PTS"], "Assertion failed: 1 ≤ B_PTS"
    assert PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] <= (NUMPOINTS - 3), "Assertion failed: A_PTS + B_PTS ≤ (NUMPOINTS − 3)"
    for i in range(NUMPOINTS - (PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2)):
        p1 = POINTS[i]
        p2 = POINTS[i + PARAMETERS["A_PTS"] + 1]
        p3 = POINTS[i + PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2]
        if not can_fit_in_circle(p1, p2, p3, PARAMETERS["RADIUS1"]):
            return True
    return False

def LIC9():
    """For a given set of at least five data points, 
       there exists a condition where three points, with the second point as the vertex, 
       form an angle such that it is either less than (π - EPSILON) or greater than (π + EPSILON)."""
    if NUMPOINTS < 5:
        return False
    assert 1 <= PARAMETERS["C_PTS"], "Assertion failed: 1 ≤ C_PTS"
    assert 1 <= PARAMETERS["D_PTS"], "Assertion failed: 1 ≤ D_PTS"
    assert PARAMETERS["C_PTS"] + PARAMETERS["D_PTS"] <= NUMPOINTS - 3, "Assertion failed: C_PTS + D_PTS ≤ NUMPOINTS − 3"

    for i in range(NUMPOINTS - PARAMETERS["C_PTS"] - PARAMETERS["D_PTS"] - 2):
        first_point_x = POINTS[i][0]
        first_point_y = POINTS[i][1]
        second_point_x = POINTS[i + PARAMETERS["C_PTS"] + 1][0]
        second_point_y = POINTS[i + PARAMETERS["C_PTS"] + 1][1]
        third_point_x = POINTS[i + PARAMETERS["C_PTS"] + PARAMETERS["D_PTS"] + 2][0]
        third_point_y = POINTS[i + PARAMETERS["C_PTS"] + PARAMETERS["D_PTS"] + 2][1]

        angle = (math.degrees((math.atan2(first_point_y - second_point_y, first_point_x - second_point_x) - math.atan2(third_point_y - second_point_y, third_point_x - second_point_x))) + 360) % 360

        if angle < math.degrees(math.pi - PARAMETERS["EPSILON"]) or angle > math.degrees(math.pi + PARAMETERS["EPSILON"]):
            return True
        
    return False
        
def LIC10():
    """For a given set of at least five data points, 
       there exists a condition where three points form a triangle with an area greater than AREA1"""
    if NUMPOINTS < 5:
        return False
    assert 1 <= PARAMETERS["E_PTS"], "Assertion failed: 1 ≤ E_PTS"
    assert 1 <= PARAMETERS["F_PTS"], "Assertion failed: 1 ≤ F_PTS"
    assert PARAMETERS["E_PTS"] + PARAMETERS["F_PTS"] <= NUMPOINTS - 3, "Assertion failed: E_PTS + F_PTS ≤ NUMPOINTS − 3"

    for i in range(NUMPOINTS - PARAMETERS["E_PTS"] - PARAMETERS["F_PTS"] - 2):
        first_point = i
        second_point = i + PARAMETERS["E_PTS"] + 1
        third_point = second_point + PARAMETERS["F_PTS"] + 1

        if(not triangle_area_vs_area1(POINTS[first_point][0], POINTS[first_point][1], POINTS[second_point][0], POINTS[second_point][1], POINTS[third_point][0], POINTS[third_point][1], PARAMETERS["AREA1"])):
            return False
    return True

def LIC11():
    """For a given set of at least three data points, 
       there exists a condition where two points separated by exactly G_PTS consecutive intervening points 
       satisfy X[j] - X[i] < 0."""
    if NUMPOINTS < 3:
        return False
    assert 1 <= PARAMETERS["G_PTS"] <= NUMPOINTS - 2, "Assertion failed: 1 ≤ G_PTS ≤ NUMPOINTS−2"

    for i in range(NUMPOINTS - PARAMETERS["G_PTS"] - 1):
        if POINTS[i + PARAMETERS["G_PTS"] + 1][0] - POINTS[i][0] < 0:
            return True
    return False
    
def LIC12():
    """For at least three data points, there's a condition where two points, 
       separated by K_PTS, are either greater than LENGTH1 apart and less than LENGTH2 apart, satisfying 0 ≤ LENGTH2."""
    if(NUMPOINTS < 3):
        return False
    assert PARAMETERS["LENGTH2"] >= 0, "LENGTH2 is < 0"
    
    condition_length1 = False
    condition_length2 = False
    # Check the distance between every couple (POINTS[i] , POINTS[i + K_PTS + 1])
    for i in range(NUMPOINTS - PARAMETERS["K_PTS"] - 1):
        distance = calculate_distance(POINTS[i], POINTS[i + PARAMETERS["K_PTS"] + 1])
        if PARAMETERS["LENGTH1"] < distance:
            condition_length1 = True
        if distance < PARAMETERS["LENGTH2"]:
            condition_length2 = True
        if condition_length1 and condition_length2:
            return True
    return False        
   
def LIC13():
    """For at least five data points, there's a condition where two sets of three points, 
       separated by A_PTS and B_PTS, respectively, 
       satisfy being outside a circle of radius RADIUS1 and inside or on a circle of radius RADIUS2, with 0 ≤ RADIUS2."""
    if(NUMPOINTS < 5):
        return False
    assert PARAMETERS["RADIUS2"] >= 0, "RADIUS2 is < 0"
    
    condition_radius1 = False
    condition_radius2 = False
    
    # Check circumcircle of triangle formed by points with index (i, i+A_PTS+1, i+ A_PTS+1 + B_PTS+1)
    for i in range(NUMPOINTS - PARAMETERS["A_PTS"] - PARAMETERS["B_PTS"] - 2):
        radius = circumradius(POINTS[i], POINTS[i + PARAMETERS["A_PTS"] + 1], POINTS[i + PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2])
        if PARAMETERS["RADIUS1"] < radius:
            condition_radius1 = True
        if radius <= PARAMETERS["RADIUS2"]:
            condition_radius2 = True            
        if condition_radius1 and condition_radius2:
            return True
    return False      
      
def LIC14():
    """For at least five data points, there's a condition where two sets of three points, 
       separated by E_PTS and F_PTS, form triangles with areas greater than AREA1 and less than AREA2, 
       respectively, with 0 ≤ AREA2."""
    if NUMPOINTS < 5:
        return False
    assert PARAMETERS["AREA2"] >= 0, "AREA2 must be non-negative"
    
    condition_area1 = False
    condition_area2 = False
    # Check area of triangle formed by points with index (i, i+E_PTS+1, i+ E_PTS+1 + F_PTS+1)
    for i in range(NUMPOINTS - PARAMETERS["E_PTS"] - PARAMETERS["F_PTS"] - 2):
        area = calculate_triangle_area(POINTS[i], POINTS[i + PARAMETERS["E_PTS"] + 1], POINTS[i + PARAMETERS["E_PTS"] + PARAMETERS["F_PTS"] + 2])
        if PARAMETERS["AREA1"] < area:
            condition_area1 = True
        if area < PARAMETERS["AREA2"]:
            condition_area2 = True            
        if condition_area1 and condition_area2:
            return True
    return False      


def generate_FUV(PUM):
    """The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix.
       The input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling interceptor launch."""
    FUV = []
    for i in range(len(PUM)):
        true_rows = all(PUM[i][j] for j in range(len(PUM)) if j != i)
        if not PUV[i] or true_rows:
            FUV.append(True)
        else:
            FUV.append(False)
    return FUV

# 0 = NOTUSED 
# 1 = ANDD 
# 2 = ORR
def generate_PUM(cmv):
    """The Conditions Met Vector (CMV) can now be used in conjunction with the Logical Connector
       Matrix (LCM) to form the Preliminary Unlocking Matrix (PUM)."""
    pum = [[False for _ in range(len(cmv))] for _ in range(len(cmv))]

    for i in range(len(cmv)):
        for j in range(len(cmv)):
            if LCM[i][j] == 0:
                pum[i][j] = True
            elif LCM[i][j] == 1:
                pum[i][j] = cmv[i] and cmv[j]
            elif LCM[i][j] == 2:
                pum[i][j] = cmv[i] or cmv[j]

    return pum

# temporarily takes in FUV as a variable, will be removed once FUV is merged into main
def launch(FUV):
    """The final launch/no launch decision is based on the FUV. The decision to launch requires that all
       elements in the FUV be true"""
    for i in FUV:
        if i == False:
            return False
    return True

def CMV():
    """The Conditions Met Vector (CMV) should be set according to the results of these calculations, i.e.
       the global array element CMV[i] should be set to true if and only if the ith LIC is met."""
    cmv = []
    cmv.append(LIC0())
    cmv.append(LIC1())
    cmv.append(LIC2())
    cmv.append(LIC3())
    cmv.append(LIC4())
    cmv.append(LIC5())
    cmv.append(LIC6())
    cmv.append(LIC7())
    cmv.append(LIC8())
    cmv.append(LIC9())
    cmv.append(LIC10())
    cmv.append(LIC11())
    cmv.append(LIC12())
    cmv.append(LIC13())
    cmv.append(LIC14())
    return cmv

def DECIDE():
    """The main function that runs the program"""
    cmv = CMV()
    pum = generate_PUM(cmv)
    fuv = generate_FUV(pum)
    return launch(fuv)