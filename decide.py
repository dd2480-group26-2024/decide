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

def LIC3():
    ps = POINTS
    while len(pointsRef) >= 3:
        # Setup the x_i and y_i coordinates of three consequtive points
        point1 = ps[0]; x1=point1[0]; y1=point1[1]
        point2 = ps[1]; x2=point2[0]; y2=point2[1]
        point3 = ps[2]; x3=point3[0]; y3=point3[1]
        # If the area of the three points is larger than AREA then we're done
        if (0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) > PARAMETERS["AREA"]:
            return True
        # Iterate by removing the head of points
        ps = ps[1:]
    return False

def LIC4():
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
    ps=POINTS
    while len(ps) >= 2:
        xi=ps[0][0];
        xj=ps[1][0];
        if xj - xi < 0:
            return True
        ps = ps[1:] # iterate by removing the head of points
    return False

def can_fit_in_circle(p1, p2, p3, radius):
    """    Checks if the triangle formed by three points can fit inside a circle of a given radius.     """
    calculated_radius = circumradius(p1, p2, p3)
    return calculated_radius <= radius


def LIC8():
   
    
    if PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] > NUMPOINTS - 3 or PARAMETERS["A_PTS"]<1 or PARAMETERS["B_PTS"]<1:
        return False
    for i in range(NUMPOINTS - (PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2)):
        p1 = POINTS[i]
        p2 = POINTS[i + PARAMETERS["A_PTS"] + 1]
        p3 = POINTS[i + PARAMETERS["A_PTS"] + PARAMETERS["B_PTS"] + 2]
        if not can_fit_in_circle(p1, p2, p3, PARAMETERS["RADIUS1"]):
            return True

    return False
