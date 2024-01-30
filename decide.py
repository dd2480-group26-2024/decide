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
    """    Calculates the radius of the circumcircle of a triangle defined by three points.     """
    a = math.dist(p1, p2)
    b = math.dist(p2, p3)
    c = math.dist(p3, p1)
    area = math.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))
    if area == 0:
        return max(a,b,c)/2
    radius = a * b * c / area
    return radius


def can_fit_in_circle(p1, p2, p3, radius):
    """    Checks if the triangle formed by three points can fit inside a circle of a given radius.     """
    calculated_radius = circumradius(p1, p2, p3)
    return calculated_radius <= radius  

  
def LIC0():
    assert PARAMETERS["LENGTH1"] >= 0, "LENGTH1 is < 0"
    for i in range(NUMPOINTS-1):
        if calculate_distance(POINTS[i], POINTS[i+1]) > PARAMETERS["LENGTH1"]:
            return True
    return False

def LIC1():
    for i in range(NUMPOINTS-2):
        distances = [calculate_distance(point1, point2) for (point1, point2) in itertools.combinations([POINTS[i],POINTS[i+1],POINTS[i+2]], 2)]
        if any(distance > 2 * PARAMETERS["RADIUS1"] for distance in distances):
           return True # If any of the pairwise distances are more than 2*RADIUS1, they cannot be contained in the circle
    return False

def LIC2():
    for i in range(NUMPOINTS-2):
        if POINTS[i] == POINTS[i+1] or POINTS[i+2] == POINTS[i+1]:
            continue
        angle = calculate_angle(POINTS[i], POINTS[i+1], POINTS[i+2])
        if angle > math.pi + PARAMETERS["EPSILON"] or angle < math.pi - PARAMETERS["EPSILON"]:
            return True
    return False
    
def LIC14():
    if NUMPOINTS < 5:
        return False
    assert PARAMETERS["AREA2"] >= 0, "AREA2 must be non-negative"
    
    condition_area1 = False
    condition_area2 = False
    # Check area of triangle formed by points with index (i, i+E_PTS+1, i+ E_PTS+1 + F_PTS+1)
    for i in range(NUMPOINTS - PARAMETERS["E_PTS"] - PARAMETERS["F_PTS"] - 2):
        area = calculate_triangle_area(POINTS[i], POINTS[i + PARAMETERS["E_PTS"] + 1], POINTS[i + PARAMETERS["E_PTS"] + PARAMETERS["F_PTS"] + 2])
        if PARAMETERS["AREA"] < area:
            condition_area1 = True
        if area < PARAMETERS["AREA2"]:
            condition_area2 = True            
        if condition_area1 and condition_area2:
            return True
    return False      

X = []
Y = []
def triangle_area_vs_area1(x1, y1, x2, y2, x3, y3, a1):
    return abs(x1 * (y2-y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5 > a1

def LIC9():
    if NUMPOINTS < 5:
        return False
    assert 1 <= PARAMETERS["C_PTS"], "Assertion failed: 1 ≤ C_PTS"
    assert 1 <= PARAMETERS["D_PTS"], "Assertion failed: 1 ≤ D_PTS"
    assert PARAMETERS["C_PTS"] + PARAMETERS["D_PTS"] <= NUMPOINTS - 3, "Assertion failed: C_PTS + D_PTS ≤ NUMPOINTS − 3"

    for i in range(NUMPOINTS - PARAMETERS["C_PTS"] - PARAMETERS["D_PTS"] - 2):
        first_point_x = X[i]
        first_point_y = Y[i]
        second_point_x = X[i + PARAMETERS["C_PTS"] + 1]
        second_point_y = Y[i + PARAMETERS["C_PTS"] + 1]
        third_point_x = X[i + PARAMETERS["C_PTS"] + PARAMETERS["D_PTS"] + 2]
        third_point_y = Y[i + PARAMETERS["C_PTS"] + PARAMETERS["D_PTS"] + 2]

        angle = (math.degrees((math.atan2(first_point_y - second_point_y, first_point_x - second_point_x) - math.atan2(third_point_y - second_point_y, third_point_x - second_point_x))) + 360) % 360

        if angle < math.degrees(math.pi - PARAMETERS["EPSILON"]) or angle > math.degrees(math.pi + PARAMETERS["EPSILON"]):
            return True
        
    return False
        
def LIC10():
    if NUMPOINTS < 5:
        return False
    assert 1 <= PARAMETERS["E_PTS"], "Assertion failed: 1 ≤ E_PTS"
    assert 1 <= PARAMETERS["F_PTS"], "Assertion failed: 1 ≤ F_PTS"
    assert PARAMETERS["E_PTS"] + PARAMETERS["F_PTS"] <= NUMPOINTS - 3, "Assertion failed: E_PTS + F_PTS ≤ NUMPOINTS − 3"

    for i in range(NUMPOINTS - PARAMETERS["E_PTS"] - PARAMETERS["F_PTS"] - 2):
        first_point = i
        second_point = i + PARAMETERS["E_PTS"] + 1
        third_point = second_point + PARAMETERS["F_PTS"] + 1

        if(not triangle_area_vs_area1(X[first_point], Y[first_point], X[second_point], Y[second_point], X[third_point], Y[third_point], PARAMETERS["AREA1"])):
            return False
    return True

def LIC11():
    if NUMPOINTS < 3:
        return False
    assert 1 <= PARAMETERS["G_PTS"] <= NUMPOINTS - 2, "Assertion failed: 1 ≤ G_PTS ≤ NUMPOINTS−2"

    for i in range(NUMPOINTS - PARAMETERS["G_PTS"] - 1):
        if X[i + PARAMETERS["G_PTS"] + 1] - X[i] < 0:
            return True
    return False

  
def LIC6():
    if NUMPOINTS < 3 or PARAMETERS['N_PTS'] < 3 or PARAMETERS['N_PTS'] > NUMPOINTS:
        return False

    for i in range(NUMPOINTS - PARAMETERS['N_PTS'] + 1):
        subset = POINTS[i:i + PARAMETERS['N_PTS']]
        line_start, line_end = subset[0], subset[-1]

        for point in subset:
            if distance_point_to_line(point, line_start, line_end) > PARAMETERS['DIST']:
                return True
    return False

def LIC7():
  if NUMPOINTS < 3 or not (1 <= PARAMETERS["K_PTS"] <= NUMPOINTS - 2):
      return False

  for i in range(NUMPOINTS - PARAMETERS["K_PTS"] - 1):
      p1 = POINTS[i]
      p2 = POINTS[i + PARAMETERS["K_PTS"] + 1]
      distance = calculate_distance(p1,p2)
      if distance > PARAMETERS['LENGTH1']:
          return True

  return False

def LIC8():
    
    if NUMPOINTS < 5 or PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] > NUMPOINTS - 3 or PARAMETERS["A_PTS"]<1 or PARAMETERS["B_PTS"]<1:
        return False
    for i in range(NUMPOINTS - (PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2)):
        p1 = POINTS[i]
        p2 = POINTS[i + PARAMETERS["A_PTS"] + 1]
        p3 = POINTS[i + PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2]
        if not can_fit_in_circle(p1, p2, p3, PARAMETERS["RADIUS1"]):
            return True

    return False


# 0 = NOTUSED 
# 1 = ANDD 
# 2 = ORR
def generate_PUM(cmv):
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
    for i in FUV:
        if i == False:
            return False
    return True

