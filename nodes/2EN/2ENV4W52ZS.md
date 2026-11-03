---
tag: 2ENV4W52ZS
kind: statement
name: Fredholm alternative for the Dirichlet problem of x'' + λx = f
role: theorem
msc:
  - 34B05
  - 34B27
  - 47A53
about:
  - TM8VQJWGHZ
uses:
  - TM8VQJWGHZ
  - 0P97V20RW7
  - 4HH8C9V8JQ
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-fourier-and-pde.tex#L454
    locator: ch-fourier-and-pde.tex:454
---

## Statement

Let $a < b$ and let $\lambda$ be a constant.
Consider the [[boundary value problem|TM8VQJWGHZ]] for the [[ordinary differential equation|0P97V20RW7]] $x'' + \lambda x = 0$ on $[a,b]$ with the conditions $x(a) = 0$ and $x(b) = 0$.
Then exactly one of these two cases holds.

1. This homogeneous problem has a solution $x$ that is not identically zero.
2. For every continuous function $f$ on $[a,b]$, the problem $x'' + \lambda x = f(t)$ with $x(a) = 0$ and $x(b) = 0$ has one and only one solution.

## Remarks

The result is an analogue of the [[Fredholm alternative|4HH8C9V8JQ]] for square linear systems.
Uniqueness for the homogeneous problem is equivalent to existence for every continuous right-hand side.

Example: take $a = 0$, $b = \pi$ and $\lambda = 1$. Then $x = \sin t$ solves the homogeneous problem, so case 1 holds.
For $\lambda = 2$ the homogeneous problem has only the zero solution, so case 2 holds.
