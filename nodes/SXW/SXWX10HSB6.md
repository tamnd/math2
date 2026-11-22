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

When the basis of a space changes by a matrix $P$, the dual basis changes by the inverse transpose of $P$.
Let $V$ be a vector space of dimension $n$ over a field $F$.
Let $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_n)$ be bases of $V$, with [[dual bases|0W6M3PSD08]] $(b_i^*)$ and $(c_i^*)$.
Let $P = (p_{ij})$ be the [[change of basis matrix|0KWXYZPJKN]] with $c_j = \sum_{i=1}^n p_{ij} b_i$ for each $j$.
Then $P$ is [[invertible|0TWTS88TWN]], and
$$c_k^* = \sum_{i=1}^n q_{ik}\, b_i^* \quad (1 \le k \le n), \qquad \text{where } Q = (q_{ik}) = (P^{-1})^{\mathsf{T}}.$$
So the change of basis matrix from $(b_i^*)$ to $(c_i^*)$ is the inverse of the [[transpose|0W809K6AW0]] of $P$.
Equivalently, the coordinates of a form change by $P^{\mathsf{T}}$: if $f = \sum_i \beta_i b_i^* = \sum_k \gamma_k c_k^*$, then $\gamma = P^{\mathsf{T}} \beta$.

## Remarks

### A first check in the plane

Take $B$ the standard basis of $\R^2$ and $C$ the basis $c_1 = (1, 1)$, $c_2 = (1, 2)$.
The columns of $P$ are $c_1$ and $c_2$, and
$$P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} = (P^{-1})^{\mathsf{T}}.$$
Column $1$ of $Q$ gives $c_1^* = 2e_1^* - e_2^*$, the form $2x - y$, and column $2$ gives $c_2^* = -e_1^* + e_2^*$, the form $-x + y$.
Check: $c_1^*(c_1) = 2 - 1 = 1$, $c_1^*(c_2) = 2 - 2 = 0$, $c_2^*(c_1) = -1 + 1 = 0$ and $c_2^*(c_2) = -1 + 2 = 1$.
The [[worked example|YMRSMANN2E]] finds the same forms as the rows of $P^{-1}$, which is the same thing, since the rows of $P^{-1}$ are the columns of $(P^{-1})^{\mathsf{T}}$.

### Why each hypothesis is needed

Finite dimension is needed, because in infinite dimension the coordinate forms of a basis are not a basis of $V^*$, so there is no change of basis matrix between dual bases.
Both families must be bases.
If $C$ is not a basis, then $P$ is not invertible, and $C$ has no dual basis to compare with.

### What it gives you

Vectors and forms change in opposite ways, so that the value of a form at a vector stays the same.
If $v$ has $B$-coordinates $\alpha$, then its $C$-coordinates are $P^{-1} \alpha$.
The form $f$ has $C^*$-coordinates $\gamma = P^{\mathsf{T}} \beta$, and the value is
$$f(v) = \gamma^{\mathsf{T}} (P^{-1} \alpha) = \beta^{\mathsf{T}} P P^{-1} \alpha = \beta^{\mathsf{T}} \alpha.$$

The lemma also measures how much the isomorphism $b_i \mapsto b_i^*$ depends on the basis.
The isomorphism that $C$ gives sends $v$ to the form with $B^*$-coordinates $Q P^{-1} \alpha = (P^{-1})^{\mathsf{T}} P^{-1} \alpha$.
This equals $\alpha$ for every $\alpha$ only when $P^{\mathsf{T}} P = I$, so two bases give the same isomorphism exactly when the change of basis matrix is orthogonal.

### The converse

If $Q$ is an $n \times n$ matrix with $Q^{\mathsf{T}} P = I$, then the forms $\sum_i q_{ik} b_i^*$ take the values $\delta_{kj}$ at the vectors $c_j$, by step 4 of the [[proof|85TB46MDWE]].
So they are the dual basis of $C$, and $Q = (P^{-1})^{\mathsf{T}}$ is the only matrix with this property.

### Generalizations

The lemma is a case of the theorem on the [[matrix of the dual map|0ZPB3180AY]], which says that in dual bases the [[dual map|0AZ5ARP287]] has the transpose matrix.
The rule $\gamma = P^{\mathsf{T}} \beta$ is that theorem for the identity map of $V$, with the basis $C$ on the source and $B$ on the target.

## Explanations

### L1 human

When the basis of a space changes, the rules that read off coordinates change too, but in the opposite way.
For example, if every basis vector is doubled, then every coordinate is halved, so every coordinate form is halved.
This opposite change is what keeps the value of a form at a vector the same.

### L2 human

Here is a typical use: the coordinates of a form in a new basis.
Let $f(x, y) = 3x + y$ on $\R^2$, so $\beta = (3, 1)$ in the standard dual basis, and take $c_1 = (1, 1)$, $c_2 = (1, 2)$ as above.
The rule $\gamma = P^{\mathsf{T}} \beta$ gives
$$\gamma = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 5 \end{pmatrix},$$
so $f = 4c_1^* + 5c_2^*$.
Check: $4(2x - y) + 5(-x + y) = 3x + y$.
The new coordinates are just the values $f(c_1) = 4$ and $f(c_2) = 5$, and this is why the rule uses $P^{\mathsf{T}}$, whose rows are the vectors $c_j$.
This is how covariant quantities, such as gradients, transform under a change of coordinates.
Watch out: using $P^{-1}$ in place of $P^{\mathsf{T}}$ for the form coordinates gives wrong values of $f(v)$.
