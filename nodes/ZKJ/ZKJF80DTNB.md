---
tag: ZKJF80DTNB
kind: statement
role: theorem
name: Holomorphy of the gamma function
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0NAHXR1FRH, 0M3YQJ81NB]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $U = \C \setminus \set{0, -1, -2, \ldots}$.
There is exactly one [[holomorphic function|0NAHXR1FRH]] $\Gamma \colon U \to \C$ that agrees with the [[gamma function|0V3FZMVB4K]] on $(0, \infty)$.

## Remarks

On the half-plane $\operatorname{Re} z > 0$, Euler's integral $\int_0^\infty t^{z-1} e^{-t}\,dt$ is holomorphic, see [[Euler integral for the gamma function|Z8D1CZFTWP]].
On $\operatorname{Re} z > -n$, with $z \notin \set{0, \ldots, -n+1}$, the formula $\Gamma(z + n)/\big(z (z + 1) \cdots (z + n - 1)\big)$ is holomorphic and agrees with the previous one on the overlap; these pieces glue to a holomorphic function on $U$.
Uniqueness follows from the identity theorem, because $U$ is open and connected and $(0, \infty) \subset U$ has accumulation points.
The function cannot be extended holomorphically to any point of $\set{0, -1, -2, \ldots}$, since it has [[poles|QFPFF15PXC]] there.
In Mathlib the statement is `Complex.differentiableAt_Gamma`.

## Explanations

### L1 human

The gamma function, first defined for positive real numbers, extends in a smooth complex way to all complex numbers except $0, -1, -2, \ldots$.
This [[analytic continuation|0M3YQJ81NB]] is unique: there is only one way to do it.

### L2 human

Holomorphy is what lets one prove identities for $\Gamma$ on the real line and then transfer them to complex arguments, by the identity theorem.
The reflection and duplication formulas are usually proved in this way.
Together with the description of the poles, it says that $\Gamma$ is a meromorphic function on $\C$.
