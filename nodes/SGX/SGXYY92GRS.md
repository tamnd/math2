---
tag: SGXYY92GRS
kind: definition
name: Walsh function
msc: [42C10]
defines: F12A5QKW8Z
uses: [51GRFQ4WY6, SASP14MA1Z, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Walsh_function
---

## Definition

For $k \ge 1$, let $r_k$ be the $k$-th [[Rademacher function|51GRFQ4WY6]] on $[0, 1)$.
Thus $r_k(t) = (-1)^{t_k}$, where $t_k$ is the $k$-th binary digit of $t$, taken from the expansion that does not end in an infinite run of $1$s.
Let $n \ge 0$ be an integer with binary expansion $n = \sum_{k \ge 0} b_k 2^k$, $b_k \in \set{0, 1}$.
The *Walsh function* of index $n$ (in Paley order) is
$$w_n = \prod_{k \ge 0} r_{k+1}^{\,b_k},$$
a finite product, with $w_0 = 1$.

## Remarks

The family $(w_n)_{n \ge 0}$ is the *Walsh system*.
It is an [[orthonormal basis|0S9GGTR0EX]] of $L^2([0, 1))$ (see [[Lp space|SASP14MA1Z]]).
Other orderings of the same functions are in use, such as the Walsh order by number of sign changes.

Example: $n = 3 = 1 + 2$, so $w_3 = r_1 r_2$.
Here $r_1 = 1$ on $[0, \tfrac12)$ and $-1$ on $[\tfrac12, 1)$, while $r_2 = 1$ on $[0, \tfrac14) \cup [\tfrac12, \tfrac34)$ and $-1$ elsewhere.
So $w_3$ is $1, -1, -1, 1$ on the four quarters of $[0, 1)$, and $\int_0^1 w_3 = 0$, as orthogonality to $w_0$ requires.

Non-example: the function $\cos(2\pi t)$ is orthogonal to many Walsh functions, but it is not a Walsh function, since it takes values other than $\pm 1$.
