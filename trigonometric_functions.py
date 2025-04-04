# %%
from algorithms import CORDIC_vector, CORDIC_rotation


pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342


def sin(angle):
    return CORDIC_rotation(angle)[1]


def cos(angle):
    return CORDIC_rotation(angle)[0]


def tan(angle):
    x, y = CORDIC_rotation(angle)
    return (y/x)


def arctan(value):
    return CORDIC_vector([1, value])[0]


def sin_deg(degrees):
    return sin(degrees * pi/180)


def cos_deg(degrees):
    return cos(degrees * pi/180)


def tan_deg(degrees):
    return tan(degrees * pi/180)


def vector_magnitude(vector):
    return CORDIC_vector(vector)[1]


print(sin(1), sin(1.5))
