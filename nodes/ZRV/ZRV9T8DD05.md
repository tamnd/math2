---
tag: ZRV9T8DD05
kind: statement
role: theorem
name: Jacobi condition
msc: [49K05]
uses: [JRQZ803Q5Y, WMPCR723MJ, 4C3BANJ8AH, FSD6S7DR8D, PS0VV149ET]
about: [FSD6S7DR8D, 4C3BANJ8AH]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_points
---

## Statement

Let $a < b$ and let $L(x, y, p)$ be a $C^3$ function on $[a, b] \times \R \times \R$.
Let $J(y) = \int_a^b L(x, y, y') \, dx$ on $C^1([a, b])$, with fixed values $y(a)$ and $y(b)$.
Let $y_0 \in C^2([a, b])$ solve the [[Euler–Lagrange equation|PS0VV149ET]] of $J$.
Assume the strengthened Legendre condition $L_{pp}(x, y_0(x), y_0'(x)) > 0$ for all $x \in [a, b]$.
A point $c \in (a, b]$ is *conjugate* to $a$ if a solution $h \ne 0$ of the [[Jacobi equation|FSD6S7DR8D]] along $y_0$ has $h(a) = h(c) = 0$.

1. (Necessary condition.) If $y_0$ is a [[weak local minimiser|WMPCR723MJ]] of $J$, then no point of the open interval $(a, b)$ is conjugate to $a$.
2. (Sufficient condition.) If no point of $(a, b]$ is conjugate to $a$, then $y_0$ is a strict weak local minimiser of $J$.

## Remarks

Write the [[second variation|4C3BANJ8AH]] as $\int_a^b (P h'^2 + Q h^2) \, dx$, as in the Jacobi equation.
Without conjugate points in $(a, b]$, there is a Jacobi solution $u > 0$ on all of $[a, b]$.
Then $w = -P u' / u$ solves $w' = w^2 / P - Q$.
Adding the zero term $\int_a^b (w h^2)' \, dx$ turns the second variation into $\int_a^b P (h' + w h / P)^2 \, dx$, which is positive for $h \ne 0$.
For the necessary part, a Jacobi solution on $[a, c]$ extended by $0$ gives zero second variation, and smoothing its corner makes the second variation negative.

Example: for $J(y) = \int_0^b (y'^2 - y^2) \, dx$ and $y_0 = 0$, the Jacobi equation is $h'' + h = 0$.
The solution with $h(0) = 0$ is $h = \sin x$, so the first conjugate point is $\pi$.
For $b < \pi$, the extremal $y_0 = 0$ is a strict weak local minimiser.
For $b > \pi$, it is not: with $\varphi(x) = \sin(\pi x / b)$ one gets $J(t\varphi) = \frac{t^2 b}{2}(\pi^2 / b^2 - 1) < 0$ for $t \ne 0$.

The strengthened Legendre condition is needed in both parts.
Conjugate points here generalise [[conjugate points|ZPXE5VSZ35]] along geodesics in Riemannian geometry.

## Explanations

### L1 human

An extremal is a curve that passes the first-derivative test for an integral functional.
Nearby extremals that start at the same point may come back and cross the extremal again; such a crossing point is a conjugate point.
The Jacobi condition says that an extremal can only be a minimiser if this does not happen before its end.
A great circle on a sphere is a good picture: it is the shortest path only until it reaches the antipodal point.

### L2 human

The Legendre condition controls the second variation for test functions that oscillate fast.
The Jacobi condition controls it for all test functions, and it reduces this question to the zeros of one solution of a linear ODE.
Together with the Euler–Lagrange equation and the strengthened Legendre condition, it gives the classical sufficient condition for a weak minimum.
For a strong minimum one adds the Weierstrass condition on the excess function, and the proof embeds the extremal in a field of extremals.
