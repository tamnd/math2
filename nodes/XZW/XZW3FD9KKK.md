---
tag: XZW3FD9KKK
kind: definition
name: Stabilizability
msc: [93D15, 93B05, 93C05]
defines: C2KM20J9DZ
uses: [0BQAA2BK3Q, 7NYES2D0Z4, A9WFM77Z4P, 1ZD7GE643S]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability
---

## Definition

Let $n, m \ge 1$, let $A$ be a real $n \times n$ matrix and let $B$ be a real $n \times m$ matrix.
Consider the system $x' = Ax + Bu$.
The pair $(A, B)$ is *stabilizable* if some real $m \times n$ matrix $K$ makes every [[eigenvalue|0BQAA2BK3Q]] of $A + BK$ have negative real part.

## Remarks

Then the state [[feedback|7NYES2D0Z4]] $u = Kx$ gives the closed loop $x' = (A + BK) x$, whose solutions all tend to $0$.
Every [[controllable|A9WFM77Z4P]] pair is stabilizable, since for a controllable pair the eigenvalues of $A + BK$ can be placed anywhere.
By the [[Hautus lemma|1ZD7GE643S]] argument, $(A, B)$ is stabilizable if and only if $\begin{pmatrix} \lambda I - A & B \end{pmatrix}$ has rank $n$ for every $\lambda \in \C$ with $\operatorname{Re} \lambda \ge 0$.
Example: $A = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$; the pair is not controllable, but $K = \begin{pmatrix} 0 & -2 \end{pmatrix}$ gives $A + BK = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$, so it is stabilizable.
Non-example: $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and the same $B$; for every $K = \begin{pmatrix} k_1 & k_2 \end{pmatrix}$ the matrix $A + BK = \begin{pmatrix} 1 & 0 \\ k_1 & -1 + k_2 \end{pmatrix}$ is lower triangular with the eigenvalue $1$, so no $K$ works.
For discrete-time systems $x_{k+1} = A x_k + B u_k$, one asks instead that all eigenvalues of $A + BK$ have absolute value less than $1$.
