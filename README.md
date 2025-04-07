# Mathematical Computation
This project looks into providing applications of various algorithms for computing mathematical functions in Python. 

Due to the intended application of these algorithms, these are designed without reliance on Python libraries - though, it should be noted, the algorithms could likely be improved through the use of libraries.

## Basic Functions
### Exponentiation
To avoid reliance on Python libraries, a simple exponentiation function was implemented - it simply iteratively multiplies the base. This may not be the most efficient method and other methods may be investigated at a later date.

### Square Roots - Heron's Method
A common computational solution for solving square roots is Heron's Method. This consists of iterating the formula:
$$
x_{n+1}=\frac{1}{2}(x_{n}+\frac{S}{x_{n}})
$$

where the result of the iterative computation is $\sqrt{S}$.
This is equivalent to using the Newton-Raphson method to solve $x^{2}-S=0$.

## CORDIC
The first algorithm of interest is the CORDIC algorithm.

CORDIC (which stands for COordinate Rotation DIgital Computer) has two operational modes: rotation mode and vector mode.

In general, CORDIC is will rotate a vector to a position and will extract data from certain values of the vector allowing the user to compute certain mathematical functions. The functions computed depend on how the vector is rotated. For example, if the algorithm uses circular rotation then standard trigonometric functions may be estimated; alternatively, if using hyperbolic rotation CORDIC will approximate hyperbolic/exponential functions.

> **Note:** CORDIC in its most efficient form does require a lookup table of arctan($2^{-i}$) and artanh($2^{-i}$) values to compute angle bisections

### Rotation Mode
Rotation mode takes a user specified angle as the input and will rotate a unit vector to this position.

When considering circular rotation, CORDIC rotates the unit vector $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ around the unit circle by iterations of $2^{-i}$. At each rotation, the algorithm compares its current angle to the desired angle and ensures it rotates in the direction of the desired angle. After $n$ iterations have been completed, the coordinates of the rotated unit vector are returned - as it has been rotated around the unit circle to an angle $\theta$, the $x$ position represents the value of $\cos\theta$ and the $y$ position represents the value of $\sin\theta$, and hence $\frac{y}{x}$ represents the value of $\tan\theta$. 

When considering hyperbolic rotation, CORDIC rotates the vector along the unit hyperbola and hence $x$ value of the final vector represents $\cosh\theta$, the $y$ value represents $\sinh\theta$, and hence $\frac{y}{x}$ represents $\tanh\theta$. Furthermore, as the following is true:

$$
\sinh x + \cosh x = e^x
$$

one can approximate $\exp(x)$ by summing the coordinates returned by the hyperbolic version of CORDIC.

### Vector Mode
Vector mode takes any vector as an input and attempts to rotate the vector to lie on the $x$-axis, hence obtaining the magnitude of the vector and, by keeping track of the angle rotated through, it can also compute some inverse functions.

Vector mode, using circular rotation, directly rotates a vector onto the $x$-axis, hence producing the vector's magnitude as the $x$-value. Furthermore, if provided with a value $\alpha$, by inputting the vector $\begin{bmatrix} \alpha \\ 1 \end{bmatrix}$, the angle returned by vector mode will represent the value of $\arctan\alpha$.

> Hyperbolic vector mode has not been implemented yet, I need to do more research into it.