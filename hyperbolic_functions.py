# %%
from algorithms import CORDIC_hyp_rotation, CORDIC_hyp_vector


# range: |x|<=2.1
def hyper_components(value):
    return CORDIC_hyp_rotation(value, n=40)


def hyper_flatten(vector):
    return CORDIC_hyp_vector(vector, n=100)


def exp(value):
    temp = hyper_components(value)
    return (temp[0] + temp[1])


def sinh(value):
    return hyper_components(value)[1]


def cosh(value):
    return hyper_components(value)[0]


def tanh(value):
    temp = hyper_components(value)
    return (temp[1]/temp[0])


# range:
# high resolution: |x| < 0.97
# low resolution: |x| <= 0.97
def artanh(value):
    return hyper_flatten([1, value])[0]


def ln(value):
    return 2*artanh((value-1)/(value+1))


print(exp(1))
print(sinh(1))
print(cosh(1))
print(tanh(1))
print(artanh(0.5))
print(ln(0.5))
