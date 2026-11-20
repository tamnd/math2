---
tag: SXWX10HSB6
kind: statement
role: lemma
name: Change of dual basis by the inverse transpose
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
about: [0ZD2CF6ZS0]
uses: [0W6M3PSD08, 0KWXYZPJKN, 0TWTS88TWN, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Finite-dimensional case
---

## Statement

Let $V$ be a vector space of dimension $n$ over a field $F$.
Let $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_n)$ be bases of $V$, with [[dual bases|0W6M3PSD08]] $(b_i^*)$ and $(c_i^*)$.
Let $P = (p_{ij})$ be the [[change of basis matrix|0KWXYZPJKN]] with $c_j = \sum_{i=1}^n p_{ij} b_i$ for each $j$.
Then $P$ is [[invertible|0TWTS88TWN]], and
$$c_k^* = \sum_{i=1}^n q_{ik}\, b_i^* \quad (1 \le k \le n), \qquad \text{where } Q = (q_{ik}) = (P^{-1})^{\mathsf{T}}.$$
So the change of basis matrix from $(b_i^*)$ to $(c_i^*)$ is the inverse of the [[transpose|0W809K6AW0]] of $P$.
Equivalently, the coordinates of a form change by $P^{\mathsf{T}}$: if $f = \sum_i \beta_i b_i^* = \sum_k \gamma_k c_k^*$, then $\gamma = P^{\mathsf{T}} \beta$.

## Remarks

### Why each hypothesis is needed

- Finite dimension is needed: in infinite dimension the coordinate forms are not a basis of $V^*$, so there is no change of basis matrix between "dual bases".
- Both families must be bases. If $C$ is not a basis, then $P$ is not invertible and $C$ has no dual basis.

### Consequences

- Vectors and forms change in opposite ways. The coordinates of a vector change by $P^{-1}$, and the coordinates of a form change by $P^{\mathsf{T}}$. The value $f(v)$, the product of the two coordinate columns, stays the same: $\gamma^{\mathsf{T}} (P^{-1} \alpha) = \beta^{\mathsf{T}} P P^{-1} \alpha = \beta^{\mathsf{T}} \alpha$.
- The map $V \to V^*$ with $b_i \mapsto b_i^*$ depends on the basis. The map from $C$ sends $v$ with $B$-coordinates $\alpha$ to the form with $B^*$-coordinates $(P^{-1})^{\mathsf{T}} P^{-1} \alpha$. This equals $\alpha$ for all $\alpha$ only when $P^{\mathsf{T}} P = I$.
- In $F^n$ with $B$ the standard basis, the rows of $P^{-1}$ are the forms $c_k^*$.

### Converse

If $Q^{\mathsf{T}} P = I$ for an $n \times n$ matrix $Q$, then the forms $\sum_i q_{ik} b_i^*$ satisfy the defining equations of the dual basis of $C$, so they are the dual basis of $C$.

### Generalizations

The matrix of the [[dual map|0AZ5ARP287]] in dual bases is the transpose, by the theorem on the [[matrix of the dual map|0ZPB3180AY]].
The rule $\gamma = P^{\mathsf{T}} \beta$ is that theorem for the identity map of $V$, with the basis $C$ on the source and $B$ on the target.

## Explanations

### L1 human

When the basis of a space changes by a matrix $P$, the dual basis changes by the matrix $(P^{-1})^{\mathsf{T}}$.
For example, if every basis vector is doubled, then every coordinate form is halved.
Vectors and coordinate forms change in "opposite" ways, so that the value of a form at a vector stays the same.

### L2 human

We check the lemma for the basis $c_1 = (1, 1)$, $c_2 = (1, 2)$ of $\R^2$, with $B$ the standard basis.

1. The columns of $P$ are $c_1$ and $c_2$: $P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, with $\det P = 1$.
2. Then $P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, and $Q = (P^{-1})^{\mathsf{T}}$ is the same matrix.
3. Column $1$ of $Q$ gives $c_1^* = 2 e_1^* - e_2^*$, that is, $c_1^*(x, y) = 2x - y$.
4. Column $2$ of $Q$ gives $c_2^* = -e_1^* + e_2^*$, that is, $c_2^*(x, y) = -x + y$.
5. Check: $c_1^*(c_1) = 2 - 1 = 1$, $c_1^*(c_2) = 2 - 2 = 0$, $c_2^*(c_1) = 0$, $c_2^*(c_2) = -1 + 2 = 1$.

The typical use is to transform covariant quantities, such as gradients, under a change of coordinates.
A trap: using $P$ instead of $(P^{-1})^{\mathsf{T}}$ for the forms gives wrong values $f(v)$.
