---
tag: FTGTM3JB1F
kind: example
name: Laguerre equation
msc: [34B30, 33C45, 34M03]
illustrates: [H96HXG6CA0, 6EZ400WM94]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre_polynomials
---

## Example

Let $\lambda \in \C$. The *Laguerre equation* is
$$z\, y'' + (1 - z)\, y' + \lambda\, y = 0.$$
In normalised form, $p(z) = \frac{1 - z}{z}$ and $q(z) = \frac{\lambda}{z}$.
Then $z p(z) = 1 - z$ and $z^2 q(z) = \lambda z$ are analytic at $0$, so $0$ is a [[regular singular point|H96HXG6CA0]].
The indicial equation is $r (r - 1) + r = r^2 = 0$, a double root $r = 0$.
By [[Fuchs' theorem|6EZ400WM94]], there is one solution $y_1 = \sum_{k \ge 0} a_k z^k$, analytic at $0$, and a second solution containing $y_1 \log z$.
Inserting the series gives $(k + 1)^2 a_{k+1} = (k - \lambda)\, a_k$.
If $\lambda = n$ is a nonnegative integer, the series stops and $y_1$ is a multiple of the Laguerre polynomial $L_n$ of degree $n$.

## Remarks

For $n = 1$, $L_1(z) = 1 - z$: then $y' = -1$ and $y'' = 0$, and $z \cdot 0 + (1 - z)(-1) + (1 - z) = 0$.
At $\infty$, the function $z^2 q(z) = \lambda z$ is unbounded, so $\infty$ is an irregular singular point and the equation is not Fuchsian.
The generalized Laguerre polynomials $L_n^{(\alpha)}$, solutions of $z y'' + (\alpha + 1 - z) y' + n y = 0$, appear in the radial part of the wave functions of the hydrogen atom.

## Explanations

### L1 human

The Laguerre equation has one tame bad point at $0$, where both exponents are equal to $0$.
So one solution is an ordinary power series, and the other one needs a logarithm.
For whole numbers $\lambda = n$, the series solution is a polynomial, the Laguerre polynomial.
