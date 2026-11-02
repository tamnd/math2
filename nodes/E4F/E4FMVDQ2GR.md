---
tag: E4FMVDQ2GR
kind: statement
role: theorem
name: Muller's method
msc: [65H05, 65H04]
uses: [SS1YMS2NPC, 9ZC177PVPC, YWZQC5E54B, 09FTAET5Z4]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Muller%27s_method
same_as:
  wikidata: Q2090477
  wikipedia: Muller's method
---

## Statement

Let $f$ be a complex function that is holomorphic near a simple zero $r$, so $f(r) = 0$ and $f'(r) \ne 0$.
Given three distinct points $x_{k-2}, x_{k-1}, x_k$, write $f[x_i, x_j] = \dfrac{f(x_i) - f(x_j)}{x_i - x_j}$ and $f[x_k, x_{k-1}, x_{k-2}] = \dfrac{f[x_k, x_{k-1}] - f[x_{k-1}, x_{k-2}]}{x_k - x_{k-2}}$, and put
$$w = f[x_k, x_{k-1}] + f[x_k, x_{k-2}] - f[x_{k-1}, x_{k-2}].$$
*Muller's method* defines
$$x_{k+1} = x_k - \frac{2 f(x_k)}{w \pm \sqrt{w^2 - 4 f(x_k) \, f[x_k, x_{k-1}, x_{k-2}]}},$$
where the sign is chosen so that the denominator has the larger absolute value.
Then there is $\delta > 0$ with the following property.
For all starting points within $\delta$ of $r$ for which the iteration is defined, the iterates [[converge|YWZQC5E54B]] to $r$ with order $q \approx 1.839$.
Here $q$ is the real root of $q^3 = q^2 + q + 1$.

## Remarks

The point $x_{k+1}$ is the zero, closest to $x_k$, of the [[interpolating polynomial|SS1YMS2NPC]] of degree at most $2$ through $(x_{k-2}, f(x_{k-2}))$, $(x_{k-1}, f(x_{k-1}))$ and $(x_k, f(x_k))$.
The formula is the quadratic formula written in the stable form that avoids cancellation.
The errors $e_k = x_k - r$ satisfy $e_{k+1} \approx C e_k e_{k-1} e_{k-2}$, which gives the stated order.
Because of the square root, the iterates can leave the real line, so the method finds [[complex|09FTAET5Z4]] zeros even from real starting points.
This makes it useful for zeros of real polynomials that are not real.
With a line through two points instead of a parabola through three, the same idea gives the [[secant method|9ZC177PVPC]].

## Explanations

### L1 human

The secant method draws a line through two points of the graph and takes its crossing with the axis.
Muller's method draws a parabola through three points and takes its crossing nearest to the last point.
A parabola can miss the real axis, and then the method moves into the complex numbers, which lets it find complex roots.

### L2 human

The method needs no derivatives and one new function value per step.
Its order is about $1.84$, between the secant method and Newton's method.
It is a common choice for finding all roots of a polynomial one at a time, combined with deflation.
