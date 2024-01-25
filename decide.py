import math



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



def LIC8(points, NUMPOINTS, A_PTS, B_PTS, RADIUS1):
    if NUMPOINTS < 5 or A_PTS + B_PTS > NUMPOINTS - 3 or A_PTS<1 or B_PTS<1:
        return False

    for i in range(NUMPOINTS - (A_PTS + B_PTS + 2)):
        p1 = points[i]
        p2 = points[i + A_PTS + 1]
        p3 = points[i + A_PTS + B_PTS + 2]

        if not can_fit_in_circle(p1, p2, p3, RADIUS1):
            return True

    return False