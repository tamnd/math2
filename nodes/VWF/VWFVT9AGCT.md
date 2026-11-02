---
tag: VWFVT9AGCT
kind: definition
name: Convenient vector space
msc: [46A17, 58C20, 46T20]
defines: 46MSX1FXZT
uses: [BW9BBF244W, 3BAJ8ZTVPX, 0BDTTM24DP]
sources:
  - url: https://en.wikipedia.org/wiki/Convenient_vector_space
---

## Definition

Let $E$ be a real Hausdorff [[locally convex space|BW9BBF244W]].
A sequence $(x_n)$ in $E$ is *Mackey–Cauchy* if there are an absolutely convex [[bounded set|3BAJ8ZTVPX]] $B \subseteq E$ and real numbers $\mu_{n,m}$ with this property.
One has $\mu_{n,m} \to 0$ as $n, m \to \infty$, and $x_n - x_m \in \mu_{n,m} B$ for all $n, m$.
The space $E$ is *convenient*, or *$c^\infty$-complete*, if every Mackey–Cauchy sequence in $E$ converges in $E$.

## Remarks

Kriegl and Michor give equivalent conditions.
One is that a curve $c \colon \R \to E$ is smooth as soon as $\ell \circ c$ is smooth for every continuous linear functional $\ell$.
Another is that the Riemann integral $\int_0^1 c(t) \, dt$ exists in $E$ for every smooth curve $c$.


Example: every Fréchet space is convenient.
A Mackey–Cauchy sequence is Cauchy, because $\mu_{n,m} B$ is eventually inside any given neighbourhood of $0$ when $B$ is bounded, and a Fréchet space is complete.
More generally every sequentially complete locally convex space is convenient.

Non-example: the space $P$ of real polynomials on $[0, 1]$ with the supremum norm is not convenient.
In a normed space, a sequence is Mackey–Cauchy if and only if it is Cauchy, since the unit ball is bounded.
The Taylor polynomials of $e^x$ form a Cauchy sequence in $P$ whose uniform limit $e^x$ is not a polynomial, so the sequence does not converge in $P$.

A normed space is therefore convenient exactly when it is a [[Banach space|0BDTTM24DP]].
