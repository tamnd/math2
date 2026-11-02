---
tag: DQ0TSVK7ZT
kind: definition
name: Local solvability
msc: [35A01, 35A27]
defines: P6E9RZNRBZ
uses: [6DZETZ5T9G, HS65DW0HXH, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Lewy%27s_example
---

## Definition

Let $\Omega \subseteq \R^n$ be open and let $P$ be a [[linear differential operator|6DZETZ5T9G]] on $\Omega$ with [[smooth|0V33BNKZ9S]] complex coefficients.
A distribution on an open set $U$ is a continuous linear functional on the space of [[test functions|HS65DW0HXH]] on $U$.
The operator $P$ is *locally solvable at* $x_0 \in \Omega$ if there is an open neighbourhood $U \subseteq \Omega$ of $x_0$ with the following property.
For every smooth function $f$ on $\Omega$ there is a distribution $u$ on $U$ with $P u = f$ in $U$, in the sense of distributions.
It is *locally solvable in* $\Omega$ if it is locally solvable at every point of $\Omega$.

## Remarks

Example: $P = \partial_1$ on $\R^n$ is locally solvable at every point: $u(x) = \int_0^{x_1} f(s, x_2, \dots, x_n) \, ds$ is smooth and satisfies $\partial_1 u = f$.
More generally, every nonzero operator with constant coefficients is locally solvable, by the [[Malgrange–Ehrenpreis theorem|3173Y813V7]].
Non-example: Lewy's operator $L = \partial_x + i \partial_y - 2 i (x + i y) \partial_t$ on $\R^3$ with variables $(x, y, t)$.
There is a smooth function $f$ on $\R^3$ such that $L u = f$ has no distribution solution in any open subset of $\R^3$, so $L$ is locally solvable at no point.
Some texts state the definition with slightly different classes of right-hand sides or of solutions.

## Explanations

### L1 human

An operator is locally solvable at a point when, for every smooth right-hand side, the equation can be solved on a fixed small neighbourhood of that point.
