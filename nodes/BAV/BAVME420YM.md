---
tag: BAVME420YM
kind: definition
name: Rademacher functions
msc: [42C10, 60G50]
defines: 51GRFQ4WY6
uses: [SASP14MA1Z, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Rademacher_system
---

## Definition

Let $k \ge 1$ be an integer.
The *$k$-th Rademacher function* $r_k \colon [0, 1) \to \set{1, -1}$ is given by
$$r_k(t) = \sgn\big(\sin(2^k \pi t)\big)$$
where $\sin(2^k \pi t) \ne 0$.
At the finitely many other points of $[0,1)$, its value is fixed so that $r_k$ is right-continuous.
Equivalently, $r_k(t) = (-1)^{t_k}$, where $t = \sum_{i \ge 1} t_i 2^{-i}$ is the binary expansion of $t$ that does not end in an infinite run of $1$s.
The family $(r_k)_{k \ge 1}$ is the *Rademacher system*.

## Remarks

The Rademacher system is orthonormal in $L^2([0, 1))$ (see [[Lp space|SASP14MA1Z]]).
It is not complete: the product $r_1 r_2$ has norm $1$ and is orthogonal to every $r_k$.
Under [[Lebesgue measure|2Z2QVWZ262]] on $[0, 1)$, the $r_k$ are independent random variables, each equal to $1$ or $-1$ with probability $\tfrac12$.

Example: $r_2$ equals $1$ on $[0, \tfrac14)$ and $[\tfrac12, \tfrac34)$ and $-1$ on $[\tfrac14, \tfrac12)$ and $[\tfrac34, 1)$.
Check: $\sin(4 \pi t) > 0$ exactly for $t \in (0, \tfrac14) \cup (\tfrac12, \tfrac34)$.

Non-example: the function $\sgn(\sin(3 \pi t))$ is a $\pm 1$ square wave on $[0, 1)$.
Its sign changes are at $\tfrac13$ and $\tfrac23$, not at dyadic points, so it is not a Rademacher function.
