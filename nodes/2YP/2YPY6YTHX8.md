---
tag: 2YPY6YTHX8
kind: definition
name: Relative homotopy group
msc: [55Q05]
defines: ZHHMDZWA7F
uses: [P976WYEFMB, 9YA6S6HD9V, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_group
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]], let $A \subseteq X$ be a subspace, let $x_0 \in A$, and let $n \ge 1$.
In the cube $I^n = [0, 1]^n$, let $I^{n-1}$ be the face where the last coordinate is $0$.
Let $J^{n-1}$ be the closure of $\partial I^n \setminus I^{n-1}$.
The *relative homotopy group* $\pi_n(X, A, x_0)$ is the set of [[homotopy|9YA6S6HD9V]] classes of maps $f \colon I^n \to X$ with $f(\partial I^n) \subseteq A$ and $f(J^{n-1}) = \set{x_0}$.
The homotopies must keep these two conditions at every time.
For $n \ge 2$, the sum $f + g$ is defined by the formula for absolute [[homotopy groups|P976WYEFMB]], putting $f$ and $g$ side by side in the first coordinate.

## Remarks

For $n \ge 2$ the sum makes $\pi_n(X, A, x_0)$ a group, and for $n \ge 3$ the group is abelian.
For $n = 1$ there is no group structure in general, and $\pi_1(X, A, x_0)$ is only a pointed set.

Example: when $A = \set{x_0}$, the conditions say that $f$ sends all of $\partial I^n$ to $x_0$, so $\pi_n(X, x_0, x_0) = \pi_n(X, x_0)$.

Example: for $n \ge 2$, $\pi_n(D^n, S^{n-1}, x_0) \cong \pi_{n-1}(S^{n-1}, x_0) \cong \Z$, by the long exact sequence of the pair and the contractibility of the disk $D^n$.

Non-example: a map $f$ with $f(\partial I^n) \subseteq A$ that does not send $J^{n-1}$ to $x_0$ is not a representative; the base point condition on $J^{n-1}$ is part of the definition.

Equivalently, $\pi_n(X, A, x_0)$ is the set of homotopy classes of maps of triples $(D^n, S^{n-1}, s_0) \to (X, A, x_0)$.
