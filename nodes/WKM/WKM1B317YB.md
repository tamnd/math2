---
tag: WKM1B317YB
kind: definition
name: Fredholm minors
msc: [45B05]
defines: HP5VJ9EBST
uses: [ZM5G144PZG, 00KDZRW4C0, PPX0AK81QV]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_theory
---

## Definition

Let $a < b$ and let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]].
For points $z_1, \dots, z_m$ and $w_1, \dots, w_m$ of $[a, b]$, write
$$K\begin{pmatrix} z_1, \dots, z_m \\ w_1, \dots, w_m \end{pmatrix} = \det[K(z_i, w_j)]_{i,j=1}^{m},$$
the [[determinant|00KDZRW4C0]] of the $m \times m$ matrix with entries $K(z_i, w_j)$.
Let $n \ge 1$, and let $x_1, \dots, x_n, y_1, \dots, y_n \in [a, b]$.
The *Fredholm minor of order $n$* of $K$ is the function
$$D_n\begin{pmatrix} x_1, \dots, x_n \\ y_1, \dots, y_n \end{pmatrix}(\lambda) = \sum_{k=0}^{\infty} \frac{(-\lambda)^k}{k!} \int_a^b \cdots \int_a^b K\begin{pmatrix} x_1, \dots, x_n, t_1, \dots, t_k \\ y_1, \dots, y_n, t_1, \dots, t_k \end{pmatrix} dt_1 \cdots dt_k$$
of $\lambda \in \C$, where the term with $k = 0$ is $K\begin{pmatrix} x_1, \dots, x_n \\ y_1, \dots, y_n \end{pmatrix}$.
The minor of order $1$ is the *first minor*, written $D(x, y; \lambda)$.

## Remarks

The series converges for every $\lambda$, uniformly in the points, by Hadamard's bound on determinants.
So each minor is an entire function of $\lambda$ and a continuous function of the points.
With $n = 0$ the same formula gives the [[Fredholm determinant|PPX0AK81QV]] $D(\lambda)$.

Example: for $K(x, y) = xy$ on $[0, 1]$, every matrix $[z_i w_j]$ of size at least $2$ has rank $1$, so its determinant is $0$.
Hence $D(x, y; \lambda) = xy$, and all minors of order $n \ge 2$ vanish identically.

Non-example: the series $\sum_k \frac{(-\lambda)^k}{k!} \int K\begin{pmatrix} t_1, \dots, t_k \\ t_1, \dots, t_k \end{pmatrix} dt$, with no fixed points, is not a minor of order $n \ge 1$; it is the determinant $D(\lambda)$ itself.

Some authors put an extra factor $\lambda^n$ in front of the minor of order $n$; the formulas that involve the minors change accordingly.
