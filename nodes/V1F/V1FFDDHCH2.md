---
tag: V1FFDDHCH2
kind: definition
name: Fredholm equation of the first kind
msc: [45B05, 45A05]
defines: 2RMWAVR1HV
uses: [GSMBXT7FPK, 526TCVMSHP]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Definition

Let $a < b$ be real numbers.
Let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], for example continuous or square-integrable, and let $f \colon [a, b] \to \C$ be a given function.
Let $\varphi$ denote an unknown function on $[a, b]$.
The *Fredholm equation of the first kind* with kernel $K$ and right-hand side $f$ is
$$\int_a^b K(x, y) \, \varphi(y) \, dy = f(x), \qquad x \in [a, b].$$
A solution is a function $\varphi$ in the chosen function space for which the integral exists and the equality holds.
In $L^2$ the equality is required for almost every $x$, and otherwise for every $x$.

## Remarks

Example: on $[0, 1]$, take $K(x, y) = xy$ and $f(x) = x / 2$.
The constant function $\varphi = 1$ is a solution, because $\int_0^1 x y \, dy = x/2$ for every $x$.
It is not the only one: $\varphi(y) = 1 + (2 - 3y)$ also works, since $\int_0^1 y (2 - 3y) \, dy = 1 - 1 = 0$.
With the same kernel and $f(x) = 1$, there is no solution, since the left side is always a multiple of $x$ and vanishes at $x = 0$.

Non-example: the equation $\varphi(x) - \int_a^b K(x, y) \varphi(y) \, dy = f(x)$ is not of the first kind, because $\varphi$ also appears outside the integral; it is a Fredholm equation of the second kind.

The equation is a special [[Fredholm integral equation|526TCVMSHP]]: the limits of integration are the fixed numbers $a$ and $b$.
In operator notation it reads $T_K \varphi = f$, where $(T_K \varphi)(x) = \int_a^b K(x, y) \varphi(y) \, dy$.
