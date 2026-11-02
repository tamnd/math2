---
tag: 928JSGQT9C
kind: definition
name: Lax pair
msc: [37K10, 35Q53, 37K15]
defines: G3A4S7CSB3
uses: [KRJX5RA0PW, 0BQAA2BK3Q, KTT75QC72Z]
sources:
  - url: https://en.wikipedia.org/wiki/Lax_pair
---

## Definition

Consider an evolution equation for an unknown $u(t)$.
Let $L(t)$ and $P(t)$ be families of linear operators on a common space, depending on $u(t)$.
They form a *Lax pair* for the equation if the equation holds if and only if
$$\frac{dL}{dt} = [P, L] = PL - LP.$$
The equation $\frac{dL}{dt} = [P, L]$ is the *Lax equation*.

## Remarks

Example: for $u(x, t)$ smooth, put $L = -\partial_x^2 + u$ and $P = -4\partial_x^3 + 6u\partial_x + 3u_x$, operators acting on functions of $x$.
A direct computation gives $[P, L] = 6 u u_x - u_{xxx}$, as a multiplication operator, while $\frac{dL}{dt} = u_t$.
So $(L, P)$ is a Lax pair for the [[Korteweg–De Vries equation|KTT75QC72Z]] $u_t - 6 u u_x + u_{xxx} = 0$.

Non-example: if $P = 0$, the Lax equation says that $L$ is constant in $t$.
When $L$ determines $u$, as $L = -\partial_x^2 + u$ does, a pair $(L, 0)$ is a Lax pair only for the trivial equation $u_t = 0$.

If $P(t)$ is skew-adjoint and $U(t)$ solves $U' = P U$ with $U(0) = I$, then $L(t) = U(t) L(0) U(t)^{-1}$.
So the [[eigenvalues|0BQAA2BK3Q]] of $L(t)$ do not depend on $t$: the flow is *isospectral*.
For matrices, $\tr L(t)^k$ is then constant for each $k$.

## Explanations

### L1 human

A Lax pair rewrites an equation as the statement that an operator $L$ changes only by conjugation.
Conjugation does not change eigenvalues, so the equation has the eigenvalues of $L$ as conserved quantities.
