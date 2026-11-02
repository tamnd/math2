---
tag: 8KYEBXE16P
kind: definition
name: Homotopy lifting property
msc: [55R05, 55P05]
defines: G4QDM01P6J
uses: [9YA6S6HD9V, 0X3WGX95FE, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_lifting_property
---

## Definition

Let $E$, $B$ and $X$ be [[topological spaces|0CQHFPGJ45]], let $p \colon E \to B$ be a [[continuous map|0X3WGX95FE]], and let $I = [0, 1]$.
The map $p$ has the *homotopy lifting property* with respect to $X$ if the following holds.
For every continuous map $\tilde f \colon X \to E$ and every [[homotopy|9YA6S6HD9V]] $H \colon X \times I \to B$ with $H(x, 0) = p(\tilde f(x))$ for all $x \in X$, there is a homotopy $\tilde H \colon X \times I \to E$ such that:

1. $p \circ \tilde H = H$.
2. $\tilde H(x, 0) = \tilde f(x)$ for all $x \in X$.

## Remarks

Example: every [[covering map|3XZRRE165N]] has the homotopy lifting property with respect to every space, and the lift is then unique.
For $X$ a point this is the path lifting property: for $p \colon \R \to S^1$, $p(t) = e^{2\pi i t}$, the loop $H(t) = e^{2\pi i t}$ with starting point $0$ lifts to $\tilde H(t) = t$.

Non-example: let $E = \set{0, 1}$ with the discrete topology, $B = [0, 1]$ and $p$ the inclusion.
For $X$ a point, $\tilde f = 0$ and $H(t) = t$, clauses 1 and 2 would force $\tilde H$ to be a path in $E$ from $0$ to $1$, but $E$ is not path-connected.

In diagram form: every commutative square with $X \to E$ on top, $X \times \set{0} \hookrightarrow X \times I$ on the left and $p$ on the right has a diagonal $X \times I \to E$ making both triangles commute.
A map with this property for all spaces $X$ is a [[Hurewicz fibration|Y773B7EQA7]]; for all cubes $I^n$, a [[Serre fibration|PB9JXQ2KC3]].
