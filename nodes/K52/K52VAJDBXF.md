---
tag: K52VAJDBXF
kind: definition
name: Linear matrix inequality
msc: [15A39, 90C22, 93D05]
defines: XHN4C927S6
uses: [0VR671PHE5, 01MMVW8CKC, 9G9S92T1VJ, 92GVPZH9FT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_matrix_inequality
---

## Definition

Let $n, m \ge 1$, and let $F_0, F_1, \dots, F_m$ be real [[symmetric|0VR671PHE5]] $n \times n$ matrices.
For $x = (x_1, \dots, x_m) \in \R^m$ put $F(x) = F_0 + x_1 F_1 + \cdots + x_m F_m$.
The *linear matrix inequality* (LMI) defined by $F_0, \dots, F_m$ is the condition
$$F(x) \succeq 0,$$
which means that $F(x)$ is [[positive semidefinite|01MMVW8CKC]].
A point $x \in \R^m$ is *feasible* for the LMI if $F(x) \succeq 0$.
The *strict* LMI is the condition $F(x) \succ 0$, which means that $F(x)$ is positive definite.

## Remarks

Example: take $m = 2$, $F_0 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $F_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $F_2 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
Then $F(x) = \begin{pmatrix} x_1 & 1 \\ 1 & x_2 \end{pmatrix}$.
The point $x = (1, 1)$ is feasible: $F(1, 1)$ has eigenvalues $0$ and $2$.
The point $x = (1, 1/2)$ is not feasible: $\det F(1, 1/2) = -1/2 < 0$, so $F$ has a negative eigenvalue.
The feasible set $\set{x : F(x) \succeq 0}$ is convex, because $F$ is affine and the positive semidefinite matrices form a convex cone.
In control theory the unknown is often a matrix.
For a real $n \times n$ matrix $A$, the condition $P \succ 0$, $A^T P + P A \prec 0$ on a symmetric matrix $P$ is an LMI in the entries of $P$.
It is feasible if and only if all eigenvalues of $A$ have negative real part, by the theory of the [[Lyapunov equation|92GVPZH9FT]].
The symbols $\succeq$ and $\succ$ denote the [[Loewner order|9G9S92T1VJ]] against the zero matrix.
