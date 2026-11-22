---
tag: S1XDFTT962
kind: example
name: The Rayleigh quotient gives a quadratically accurate eigenvalue estimate
msc: ["15A18", "65F15"]
topics: [3YM9EK6VMB]
audience: ug2
instance_of: [06WHP8SE98]
illustrates: [T7MFPSY009]
uses: [06WHP8SE98, 0MB8HQW495, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Example

A test vector that is off from an eigenvector by a small amount $\varepsilon$ gives a [[Rayleigh quotient|06WHP8SE98]] that is off from the eigenvalue by only about $\varepsilon^2$.
Let $T$ be [[self-adjoint|0MB8HQW495]] on a real inner product space, let $u$ be a unit eigenvector with $Tu = \lambda u$, and let $w$ be a unit vector orthogonal to $u$.
For a real number $\varepsilon$, let $v = u + \varepsilon w$.

1. The cross terms vanish. Self-adjointness gives $\ip{Tw}{u} = \ip{w}{Tu} = \lambda \ip{w}{u} = 0$, and $\ip{Tu}{w} = \lambda \ip{u}{w} = 0$.
2. So only two terms of the quadratic form survive, and Pythagoras gives the norm:
$$\ip{Tv}{v} = \ip{Tu}{u} + \varepsilon^2 \ip{Tw}{w} = \lambda + \varepsilon^2 \ip{Tw}{w}, \qquad \ip{v}{v} = 1 + \varepsilon^2.$$
3. The error of the quotient is therefore
$$R(v) - \lambda = \frac{\lambda + \varepsilon^2 \ip{Tw}{w}}{1 + \varepsilon^2} - \lambda = \frac{\varepsilon^2 \big(\ip{Tw}{w} - \lambda\big)}{1 + \varepsilon^2}.$$
4. So an error of size $\varepsilon$ in the vector gives an error of size $\varepsilon^2$ in the eigenvalue.

Now a numerical check with the [[symmetric|0N28QN4CYA]] matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ and the dot product.

5. Take $u = \tfrac{1}{\sqrt{5}}(2, 1)$ with $\lambda = 6$, and $w = \tfrac{1}{\sqrt{5}}(1, -2)$, an eigenvector for $1$, so $\ip{Aw}{w} = 1$. Let $\varepsilon = \tfrac{1}{5}$.
6. Then $v = u + \tfrac{1}{5} w$ is a multiple of $5(2, 1) + (1, -2) = (11, 3)$. Directly,
$$R(11, 3) = \frac{5 \cdot 121 + 4 \cdot 33 + 2 \cdot 9}{121 + 9} = \frac{755}{130} = \frac{151}{26}.$$
7. Step 3 gives $R(v) - 6 = \dfrac{\tfrac{1}{25}(1 - 6)}{\tfrac{26}{25}} = -\tfrac{5}{26}$, and $6 - \tfrac{5}{26} = \tfrac{151}{26}$. The two computations agree.

## Remarks

In step 7 the tilt of the vector is $\varepsilon = 0.2$, and the error of the eigenvalue is $\tfrac{5}{26} \approx 0.19$.
With $\varepsilon = 0.02$, step 3 gives an error of $\tfrac{0.0004 \cdot 5}{1.0004} \approx 0.002$, so a tenfold better vector gives a hundredfold better eigenvalue.

The estimate needs self-adjointness in step 1.
For a matrix that is not normal, the cross terms do not cancel, and the error of the quotient is usually of size $\varepsilon$ only.
Over $\mathbb{C}$ the same computation works with $\abs{\varepsilon}^2$ in place of $\varepsilon^2$.
Numerical methods such as Rayleigh quotient iteration rely on this accuracy.

## Explanations

### L1 human

If a test vector points almost along an eigenvector, its Rayleigh quotient is very close to the eigenvalue.
A small tilt of the vector gives a much smaller error in the number.
For the matrix with rows $(5, 2)$ and $(2, 2)$, the direction $(11, 3)$ is tilted a little away from $(2, 1)$, and its quotient $5.81$ is close to the eigenvalue $6$.

### L2 human

The computation in steps 1 to 3 has three parts.
First, write the test vector as an eigenvector plus a small orthogonal error $\varepsilon w$.
Second, expand the quadratic form; the cross terms vanish because $T$ is self-adjoint.
Third, only terms with $\varepsilon^2$ are left, both in the numerator and in the denominator.
Watch out: the test vector need not be a unit vector, because the quotient divides by $\ip{v}{v}$ and any multiple of $v$ gives the same value.
