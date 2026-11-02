---
tag: ZCDCJTTG8V
kind: example
name: Hermite equation
msc: [34B30, 33C45, 34A25]
illustrates: [QK2J038VB4, 08RT9GDDPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Hermite_polynomials
---

## Example

Let $\lambda \in \C$. The *Hermite equation* is
$$y'' - 2 z\, y' + 2 \lambda\, y = 0.$$
Its coefficients $-2z$ and $2 \lambda$ are polynomials, so every point of $\C$ is an [[ordinary point|QK2J038VB4]].
A [[power series solution|08RT9GDDPQ]] $y = \sum_{k \ge 0} a_k z^k$ gives
$$(k + 2)(k + 1)\, a_{k+2} - 2 k\, a_k + 2 \lambda\, a_k = 0, \quad \text{so} \quad a_{k+2} = \frac{2 (k - \lambda)}{(k + 2)(k + 1)}\, a_k.$$
The values $a_0$ and $a_1$ are free, and every solution is an entire function.
If $\lambda = n$ is a nonnegative integer, the recurrence stops at $k = n$ for the series of the same parity as $n$.
This gives a polynomial solution of degree $n$, a multiple of the [[Hermite polynomial|MGACY98E9H]] $H_n$.

## Remarks

For $n = 2$, $H_2(z) = 4 z^2 - 2$; then $y'' = 8$ and $y' = 8 z$, and $8 - 2 z \cdot 8 z + 4 (4 z^2 - 2) = 0$.
The substitution $y = e^{z^2 / 2} u$ links the equation to the quantum harmonic oscillator $u'' + (2 \lambda + 1 - z^2) u = 0$.
The point $\infty$ is an irregular singular point.

## Explanations

### L1 human

The Hermite equation has no bad points in the finite plane, so its solutions are power series that converge everywhere.
For whole numbers $\lambda = n$ one of the series stops and becomes a polynomial.
These Hermite polynomials describe the energy states of a quantum harmonic oscillator.
