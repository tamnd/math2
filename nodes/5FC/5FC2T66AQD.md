---
tag: 5FC2T66AQD
kind: definition
name: Totally unimodular matrix
msc: [15B36, 90C10, 90C27]
defines: VSD67A49XC
uses: [0VD9ZSWWJG, 0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Unimodular_matrix
    locator: Total unimodularity
---

## Definition

Let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] with entries in $\Z$.
The matrix $A$ is *totally unimodular* when every [[minor|0BT9BYWVRY]] of $A$, that is, the determinant of every square submatrix, is $0$, $1$ or $-1$.

## Remarks

Example: $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ is totally unimodular.
Its $1 \times 1$ minors are entries in $\{0, 1\}$, and its $2 \times 2$ minors are $1$, $1$ and $1$.
Non-example: $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ is not totally unimodular, because its determinant is $2$.
A totally unimodular matrix has all entries in $\{0, 1, -1\}$, since the entries are its $1 \times 1$ minors.
A square totally unimodular matrix need not be [[unimodular|R6RBQHW191]], because its determinant may be $0$.
The incidence matrix of a [[bipartite graph|0ZVQKTRKVQ]] and the incidence matrix of a [[directed graph|0KFYGSHHF5]] are totally unimodular.
By a theorem of Hoffman and Kruskal, an integer matrix $A$ is totally unimodular exactly when the polyhedron $\set{x \in \R^n : Ax \le b,\ x \ge 0}$ has integral vertices for every integral vector $b$.
