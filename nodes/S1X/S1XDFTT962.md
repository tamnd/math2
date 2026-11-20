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

Let $T$ be [[self-adjoint|0MB8HQW495]], let $u$ be a unit eigenvector with $T u = \lambda u$, and let $w$ be a unit vector orthogonal to $u$.
For a real number $\varepsilon$, let $v = u + \varepsilon w$, a vector at a small angle to $u$.

1. Self-adjointness gives $\ip{Tw}{u} = \ip{w}{Tu} = \lambda \ip{w}{u} = 0$. Also $\ip{Tu}{w} = \lambda \ip{u}{w} = 0$.
2. So $\ip{Tv}{v} = \ip{Tu}{u} + \varepsilon^2 \ip{Tw}{w} = \lambda + \varepsilon^2 \ip{Tw}{w}$. Also $\ip{v}{v} = 1 + \varepsilon^2$.
3. The [[Rayleigh quotient|06WHP8SE98]] is therefore
$$R(v) - \lambda = \frac{\lambda + \varepsilon^2 \ip{Tw}{w}}{1 + \varepsilon^2} - \lambda = \frac{\varepsilon^2 \big(\ip{Tw}{w} - \lambda\big)}{1 + \varepsilon^2}.$$
4. So an error of size $\varepsilon$ in the vector gives an error of size $\varepsilon^2$ in the eigenvalue.

A numerical check with the [[symmetric|0N28QN4CYA]] matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$:

5. Take $u = \tfrac{1}{\sqrt{5}}(2, 1)$ with $\lambda = 6$, and $w = \tfrac{1}{\sqrt{5}}(1, -2)$ with $\ip{Aw}{w} = 1$. Let $\varepsilon = \tfrac{1}{5}$.
6. Then $v$ is a multiple of $5 (2, 1) + (1, -2) = (11, 3)$. Directly, $R(11, 3) = \tfrac{605 + 132 + 18}{130} = \tfrac{151}{26}$.
7. Step 3 gives $R(v) - 6 = \tfrac{(1/25)(1 - 6)}{26/25} = -\tfrac{5}{26}$, and $6 - \tfrac{5}{26} = \tfrac{151}{26}$. The two computations agree.

## Remarks

- In step 7 the vector error is $\varepsilon = 0.2$, and the eigenvalue error is $\tfrac{5}{26} \approx 0.19$. With $\varepsilon = 0.02$, the formula gives an eigenvalue error of about $0.002$.
- The estimate needs self-adjointness in step 1. For a general matrix, the error in the eigenvalue is usually of size $\varepsilon$ only.
- Numerical methods such as Rayleigh quotient iteration use this accuracy.

## Explanations

### L1 human

If a test vector points almost along an eigenvector, its Rayleigh quotient is very close to the eigenvalue.
A small tilt of the vector gives a much smaller error in the number.

### L2 human

The computation in steps 1 to 3 has three parts:

1. Write the test vector as an eigenvector plus a small orthogonal error.
2. Expand the quadratic form. The cross terms vanish because $T$ is self-adjoint.
3. Only the term with $\varepsilon^2$ is left.

A trap: the vector $v$ need not be a unit vector.
The Rayleigh quotient divides by $\ip{v}{v}$, so any multiple of $v$ gives the same value.
