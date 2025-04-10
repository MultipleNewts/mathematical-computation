# %%
# this is termporarily being used in place of a lookup table
from math import atan2, atan, atanh
# from atan_lookup import atan_table as lookup


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
    # Start with the x unit vector
    v_cur = [1, 0]
    # define correction coefficient
    K = 1
    # define direction coefficient
    sigma = 1
    for i in range(n):
        # determine direction of rotation
        if (angle-atan2(v_cur[1], v_cur[0])) > 0:
            sigma = 1
        else:
            sigma = -1
        # adjust correction constant
        # NOTE: if python supported floating point bitshifts,
        # bitshifts could used in place of exponents here
        K *= 1/SqRoot_Heron(1+exponent(2, (-2*i)))
        # calculate new vector positions
        x2 = v_cur[0]+(-sigma*exponent(2, (-i)))*v_cur[1]
        y2 = (sigma*exponent(2, (-i))*v_cur[0])+v_cur[1]
        # update vector
        v_cur = [x2, y2]
    # apply correction constant
    v_cur = [K*v_cur[0], K*v_cur[1]]
    # return vector
    return v_cur


# Method for various function: finds side lengths of a triangle from a unit hyperbola
# Returns x=cosh(value) and y=sinh(value) of the point where it meets the hyperbola at a given angle
def CORDIC_hyp_rotation(value, n=40):
    # Start with the x unit vector
    v_cur = [1, 0]
    # define correction coefficient
    K = 1
    # define direction coefficient
    sigma = 1
    for i in range(1, n):
        for j in range(2):
            # find the bisection / next rotation
            z = atanh(exponent(2, (-i)))
            # determine direction of rotation
            if value - z > 0:
                sigma = 1
            else:
                sigma = -1
            # adjust correction constant
            # NOTE: if python supported floating point bitshifts,
            # bitshifts could used in place of exponents here
            K *= 1/SqRoot_Heron(1-exponent(2, (-2*i)))
            # calculate new vector positions
            x2 = v_cur[0]+(sigma*exponent(2, (-i)))*v_cur[1]
            y2 = (sigma*exponent(2, (-i))*v_cur[0])+v_cur[1]
            # update vector
            v_cur = [x2, y2]
            value -= sigma*z
    # apply correction constant
    v_cur = [K*v_cur[0], K*v_cur[1]]
    # return vector
    return v_cur


# finds the phase and magnitude of a vector [x,y]
# Returns the approximate value of atan(y/x)
def CORDIC_vector(vector, n=40):
    # define current vector
    v_cur = vector
    # define correction coefficient
    K = 1
    # define vars
    sigma = 1
    angle_estimate = 0
    # iterate
    for i in range(n):
        # we wish to nullify y, we modify rotation direction (sigma)
        # depending on if y is -ve or +ve
        if v_cur[1] > 0:
            sigma = -1
        else:
            sigma = 1
        # calculate new vals of K, x, and y
        K *= 1/SqRoot_Heron(1+exponent(2, (-2*i)))
        x2 = v_cur[0]+(-sigma*exponent(2, (-i)))*v_cur[1]
        y2 = (sigma*exponent(2, (-i))*v_cur[0])+v_cur[1]
        # define new vector
        v_cur = [x2, y2]
        # calculate angle change
        angle_estimate += -sigma*atan(exponent(2, (-i)))
    v_cur = [K*v_cur[0], K*v_cur[1]]
    return angle_estimate, v_cur[0]


# finds the phase and magnitude of a vector [x,y]
# Returns the approximate value of atan(y/x)
def CORDIC_hyp_vector(vector, n=40):
    # define current vector
    v_cur = vector
    # define correction coefficient
    K = 1
    # define vars
    sigma = 1
    angle_estimate = 0
    # iterate
    for i in range(1, n):
        for j in range(2):
            # we wish to nullify y, we modify rotation direction (sigma)
            # depending on if y is -ve or +ve
            if v_cur[1] > 0:
                sigma = -1
            else:
                sigma = 1
            # calculate new vals of K, x, and y
            K *= 1/SqRoot_Heron(1-exponent(2, (-2*i)))
            x2 = v_cur[0]+(sigma*exponent(2, (-i)))*v_cur[1]
            y2 = (sigma*exponent(2, (-i))*v_cur[0])+v_cur[1]
            # define new vector
            v_cur = [x2, y2]
            # calculate angle change
            angle_estimate -= sigma*atanh(exponent(2, (-i)))
    v_cur = [K*v_cur[0], K*v_cur[1]]
    return angle_estimate, v_cur[0]

# %%
