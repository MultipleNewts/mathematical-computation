# %%
from algorithms import CORDIC_hyp_rotation, CORDIC_hyp_vector


def hyper_components(value):
    return CORDIC_hyp_rotation(value, n=40)


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


# range: |x|<=2.1
print(exp(1))
print(sinh(1))
print(cosh(1))
print(tanh(1))

