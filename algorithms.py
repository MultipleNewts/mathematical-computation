# %%
# this is termporarily being used in place of a lookup table
from math import atan2

pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342


# Method for exponentiation: iteratively multiply to obtain value
def exponent(base, power):
    total = 1
    for i in range(abs(power)):
        total *= base
    if power < 0:
        total = 1/total
    return total


# Method for square roots: uses an iterative method known as Heron's Method
def SqRoot_Heron(base, n=100):
    x = 1
    for i in range(n):
        x = 0.5*(x+(base/x))
    return x


# Method for various function: finds side lengths of a traingle within a unit circle
# Returns x and y of the point where the hypotenuse meets the circumference at an angle
def CORDIC_rotation(angle, n=40):
    v_cur = [1, 0]
    K = 1
    sigma = 1
    for i in range(n):
        if (angle-atan2(v_cur[1], v_cur[0])) > 0:
            sigma = 1
        else:
            sigma = -1
        K *= 1/SqRoot_Heron(1+exponent(2, (-2*i)))
        x2 = v_cur[0]+(-sigma*exponent(2, (-i)))*v_cur[1]
        y2 = (sigma*exponent(2, (-i))*v_cur[0])+v_cur[1]
        v_cur = [x2, y2]
    v_cur = [K*v_cur[0], K*v_cur[1]]
    return v_cur


def sin(angle):
    return CORDIC_rotation(angle)[1]


def cos(angle):
    return CORDIC_rotation(angle)[0]


def tan(angle):
    x, y = CORDIC_rotation(angle)
    return (y/x)


def sin_deg(degrees):
    return sin(degrees * pi/180)


def cos_deg(degrees):
    return cos(degrees * pi/180)


def tan_deg(degrees):
    return tan(degrees * pi/180)


# %%
