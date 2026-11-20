---
tag: 0ENVM493VK
kind: statement
role: corollary
name: Inverse via the adjugate
aliases: [inverse-in-terms-of-the-adjugate]
msc: ["15A09"]
topics: [DTBK11SR77]
audience: ug1
about: [0EB9N0S33C]
uses: [0528HKWZ1Z, 0TWTS88TWN, 0GMPYM0NSR, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Important consequence
---

## Statement

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$ such that $\det A$ is a [[unit|019NFGFPR5]] of $K$.
Then $A$ is [[invertible|0TWTS88TWN]], and
$$A^{-1} = (\det A)^{-1} \operatorname{adj}(A),$$
where $\operatorname{adj}(A)$ is the [[adjugate|0GMPYM0NSR]] of $A$.
In entries, $(A^{-1})_{ij} = C_{ji} / \det A$, where $C_{ji}$ is the $(j, i)$ cofactor.

## Remarks

### Why each hypothesis is needed

If $\det A$ is not a unit, then the formula has no meaning, and $A$ is not invertible over $K$.
For example, $A = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{Z}$ has $\det A = 2$, and its inverse over $\mathbb{Q}$ has the entry $1/2$.
The ring must be commutative, since the adjugate identity uses the Laplace expansion.

### Consequences

- For $n = 2$ and $ad - bc \ne 0$ over a field, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
- An integer matrix with $\det A = \pm 1$ has an integer inverse, $A^{-1} = \pm \operatorname{adj} A$.
- Over a field, every entry of $A^{-1}$ is a rational function of the entries of $A$, so inversion is continuous on the invertible matrices over $\mathbb{R}$.

- For large $n$, the formula needs $n^2$ determinants of size $n - 1$, so row reduction with about $n^3$ operations is much faster.

### Converse

The [[converse|03Q7RE2HXR]] holds too: if $A$ is invertible over $K$, then $\det A$ is a unit, because $\det A \det A^{-1} = 1$.

## Explanations

### L1 human

This formula gives every entry of the inverse as a quotient of two determinants.
It is useful for theory and for small matrices.
For $2 \times 2$ matrices, it is the formula that most students learn first.

### L2 human

Take $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$, with $\det A = 6 - 5 = 1$.

1. The adjugate is $\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
2. Since $\det A = 1$, $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
3. Check: $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I_2$.

The inverse has integer entries, as the special case for $\det A = \pm 1$ predicts.
A $3 \times 3$ case is in the [[adjugate example|~ef1b2481]].
A trap: the formula uses the transpose of the cofactor matrix; with the cofactor matrix itself, the product $AC$ is not $\det A \cdot I$ in general.

### L3 human

The formula shows that $A \mapsto A^{-1}$ is a regular map on $\mathrm{GL}_n$, given by polynomials divided by $\det$.
Over a ring, it shows that $\mathrm{GL}_n(K)$ is the set of matrices whose determinant lies in $K^\times$.
