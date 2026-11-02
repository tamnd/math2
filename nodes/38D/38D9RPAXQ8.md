---
tag: 38D9RPAXQ8
kind: statement
role: theorem
name: Bourget's hypothesis
msc: [33C10, 11J91]
uses: [CZCMRDWDYW, M324R146XH]
about: [M324R146XH]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Statement

Let $n \ge 0$ and $m \ge 1$ be integers, and let $J_n$ and $J_{n+m}$ be [[Bessel functions of the first kind|CZCMRDWDYW]].
Then $J_n$ and $J_{n+m}$ have no common zero in $\C$ other than $z = 0$.

## Remarks

Bourget stated it as a conjecture in the nineteenth century, and Siegel proved it in 1929.
The proof is number-theoretic: a common nonzero zero would be a root of a polynomial with rational coefficients, hence algebraic.
But Siegel showed that $J_n(\alpha)$ is transcendental, so nonzero, for every nonzero algebraic $\alpha$.
Example: $J_0$ and $J_1$ have no common positive zero, which also follows from $J_0' = -J_1$ and the fact that the [[zeros|M324R146XH]] of $J_0$ are simple.
The cases $m = 1$ and $m = 2$ follow from the recurrence relations and the simplicity of nonzero zeros; the general case is the hard part.

## Explanations

### L1 human

Two Bessel functions of different whole-number orders never vanish at the same nonzero point.
In terms of a drum, two different families of vibration modes never share a frequency in this way.
It sounds like a simple fact about wiggly curves, but its proof needs deep results about transcendental numbers.

### L2 human

For $m = 1$, a common zero $z_0 \ne 0$ of $J_n$ and $J_{n+1}$ would give $J_n'(z_0) = \frac{n}{z_0} J_n(z_0) - J_{n+1}(z_0) = 0$, a double zero, which is impossible.
For $m = 2$ the relation $J_n + J_{n+2} = \frac{2(n+1)}{z} J_{n+1}$ reduces it to the case $m = 1$.
For larger $m$ the recurrence writes $J_{n+m}$ as a combination of $J_n$ and $J_{n+1}$ whose coefficients are polynomials in $1/z$ with rational coefficients (the Lommel polynomials).
So a common zero must be a root of one of these polynomials, and it is algebraic.
Siegel's transcendence theorem for $J_n$ at algebraic points, a starting point of the theory of $E$-functions, then settles it.
