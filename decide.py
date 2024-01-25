import math


def distance(p1, p2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def can_fit_in_circle(p1, p2, p3, radius):
    """ Check if three points can fit in a circle of given radius. """

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