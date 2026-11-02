---
tag: DHC96EYCN6
kind: statement
role: theorem
name: Curry–Schoenberg theorem
msc: [41A15, 65D07]
uses: [62AFX32JGT, 84TJ8KQ926, 0KCQ9Y3QKA]
about: [62AFX32JGT, 84TJ8KQ926]
sources:
  - url: https://en.wikipedia.org/wiki/B-spline
---

## Statement

Let $k \ge 1$ be an integer, the order, so that polynomial pieces have degree at most $k - 1$.
Let $\xi_1 < \xi_2 < \cdots < \xi_{l+1}$ be breakpoints, and for $i = 2, \dots, l$ let $\nu_i$ be an integer with $0 \le \nu_i \le k$.
Let $S$ be the space of functions $s$ on $[\xi_1, \xi_{l+1})$ such that:

1. on each interval $[\xi_i, \xi_{i+1})$, $s$ agrees with a polynomial of degree at most $k - 1$;
2. at each interior breakpoint $\xi_i$, the two adjacent polynomial pieces have equal derivatives of orders $0, 1, \dots, \nu_i - 1$ at $\xi_i$.

Let $n = k + \sum_{i=2}^{l} (k - \nu_i)$.
Let $t_1 \le t_2 \le \cdots \le t_{n+k}$ be a knot sequence with $t_k = \xi_1$, $t_{n+1} = \xi_{l+1}$, $t_1 \le \dots \le t_k$, $t_{n+1} \le \dots \le t_{n+k}$, and in which each interior breakpoint $\xi_i$ occurs exactly $k - \nu_i$ times among $t_{k+1}, \dots, t_n$.
Then the [[B-splines|62AFX32JGT]] $B_{1,k}, \dots, B_{n,k}$ of order $k$ for the knots $t$, restricted to $[\xi_1, \xi_{l+1})$, form a [[basis|0KCQ9Y3QKA]] of $S$.
In particular, $\dim S = n$.

## Remarks

Each $B_{j,k}$ is a piecewise polynomial of degree at most $k - 1$, and a knot of multiplicity $m$ costs it exactly $m$ orders of smoothness, so each $B_{j,k}$ lies in $S$.
The dimension of $S$ is $n$ by counting: $l$ pieces give $kl$ coefficients, and the conditions at $\xi_i$ remove $\nu_i$ of them, which are independent.
Linear independence of the B-splines can be proved with the dual functionals of de Boor and Fix, and $n$ independent elements of an $n$-dimensional space form a basis.
Example: for $k = 4$ and $\nu_i = 3$ at every interior breakpoint, $S$ is the space of cubic [[splines|84TJ8KQ926]] of class $C^2$, and $n = l + 3$.
The end knots $t_1, \dots, t_k$ and $t_{n+1}, \dots, t_{n+k}$ can be chosen freely in the stated ranges; a common choice is to make them all equal to the endpoints.
The intervals are half-open because B-splines are right-continuous.
With the common choice of end knots, all of them vanish at $\xi_{l+1}$, and one extends a spline there by its left limit.

## Explanations

### L1 human

A spline is built from polynomial pieces glued together with some smoothness at the joints.
The theorem says that the B-splines are exactly the right building blocks: every such spline is a unique sum of multiples of them.
The number of B-splines needed equals the number of free parameters of the spline space.
The only thing to choose is how often each joint is repeated as a knot, and that encodes how smooth the spline is there.

### L2 human

The theorem turns the abstract space of piecewise polynomials into a concrete space with a well-conditioned basis of small support.
It is why spline software stores a spline as a knot vector and a list of B-spline coefficients.
Interpolation and least squares fitting with splines become banded linear systems in this basis.
Raising the multiplicity of a knot by one lowers the smoothness there by one, and multiplicity $k$ allows a jump.
