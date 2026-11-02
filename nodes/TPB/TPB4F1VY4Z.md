---
tag: TPB4F1VY4Z
kind: statement
role: theorem
name: Bürmann–Lagrange series
msc: [30B10, 41A58]
uses: [0NAHXR1FRH, 0Z49YH6ZWY, BANY9YR82A]
about: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_inversion_theorem
    locator: Lagrange–Bürmann formula
---

## Statement

Let $g$ be a [[holomorphic function|0NAHXR1FRH]] on a neighbourhood of a point $a \in \C$ with $g'(a) \ne 0$, and let $b = g(a)$.
Let $H$ be holomorphic on a neighbourhood of $a$.
Put $\varphi(z) = \dfrac{z - a}{g(z) - b}$ for $z \ne a$ and $\varphi(a) = 1/g'(a)$, which is holomorphic near $a$.
Then there is a neighbourhood $U$ of $a$ such that for all $z \in U$
$$H(z) = H(a) + \sum_{n=1}^{\infty} \frac{c_n}{n!} \big( g(z) - b \big)^n, \qquad c_n = \frac{d^{\,n-1}}{dz^{\,n-1}} \Big[ H'(z)\, \varphi(z)^n \Big]_{z = a},$$
and the series converges absolutely on $U$.

## Remarks

Proof idea: since $g'(a) \ne 0$, the function $g$ has a holomorphic inverse $g^{-1}$ near $b$.
The series is the [[Taylor series|0Z49YH6ZWY]] of $w \mapsto H(g^{-1}(w))$ at $w = b$, evaluated at $w = g(z)$.
Its coefficients are found by Cauchy's integral formula for derivatives, followed by the change of variable $w = g(z)$.
An integration by parts then turns the integral into a residue at $z = a$.

With $H(z) = z$ the series is the classical Lagrange inversion formula for $g^{-1}$.
Example: $g(z) = z e^{-z}$ and $a = 0$, so $\varphi(z) = e^{z}$ and $c_n = \frac{d^{\,n-1}}{dz^{\,n-1}} e^{nz} \big|_{z=0} = n^{n-1}$.
So the inverse of $z e^{-z}$ near $0$ is $\sum_{n \ge 1} \frac{n^{n-1}}{n!} w^n$, which is $-W(-w)$ for the [[Lambert W function|FW2JKAN14B]].

The hypothesis $g'(a) \ne 0$ is needed: for $g(z) = z^2$ and $a = 0$ the function $H(z) = z$ is not a power series in $g(z) = z^2$, since $z$ is odd.
The formal version for power series over a field of characteristic $0$ is the [[Lagrange inversion theorem|BANY9YR82A]].

## Explanations

### L1 human

A Taylor series writes a function as a sum of powers of $z - a$.
The Bürmann–Lagrange series instead writes it as a sum of powers of another function $g(z) - g(a)$.
This works whenever $g$ is locally one-to-one at $a$.
The coefficients come from derivatives at the single point $a$, so one never has to invert $g$ explicitly.

### L2 human

The series is the analytic form of Lagrange inversion.
It gives the Taylor coefficients of an inverse function, for example of the solution $w(z)$ of Kepler's equation or of the Lambert $W$ function.
In asymptotic analysis it is used to change variables near a critical point.
For instance, it reduces an integral in [[Laplace's method|9G7K8DBT9Y]] to a Gaussian form with an explicit series of corrections.
The combinatorial version, for formal power series, is the [[Lagrange inversion theorem|BANY9YR82A]], which counts trees.
