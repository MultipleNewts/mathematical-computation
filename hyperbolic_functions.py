# %%
from algorithms import CORDIC_hyp_rotation


def hyper_components(value):
    return CORDIC_hyp_rotation(value, n=41)


def exp(value):
    temp = hyper_components(value)
    return (temp[0] + temp[1])


def sinh(value):
    return hyper_components(value)[1]


def cosh(value):
    return hyper_components(value)[0]


print(exp(1))
print(sinh(1))
print(cosh(1))

