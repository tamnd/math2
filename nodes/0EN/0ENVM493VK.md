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

When the determinant of a square matrix can be divided by, the inverse is the adjugate divided by the determinant.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$ such that $\det A$ is a [[unit|019NFGFPR5]] of $K$.
Then $A$ is [[invertible|0TWTS88TWN]], and
$$A^{-1} = (\det A)^{-1} \operatorname{adj}(A),$$
where $\operatorname{adj}(A)$ is the [[adjugate|0GMPYM0NSR]] of $A$.
In entries, $(A^{-1})_{ij} = (\det A)^{-1} C_{ji}$, where $C_{ji}$ is the cofactor of $A$ at position $(j, i)$.

## Remarks

### A $3 \times 3$ inverse

The matrix
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$$
has $\det A = -3$, and the [[worked example|BDHT6DBGC9]] finds its adjugate.
The adjugate and, after dividing by $-3$, the inverse are
$$\operatorname{adj} A = \begin{pmatrix} 2 & 4 & -3 \\ 2 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}, \qquad A^{-1} = \frac{1}{3} \begin{pmatrix} -2 & -4 & 3 \\ -2 & 11 & -6 \\ 3 & -6 & 3 \end{pmatrix}.$$
Row $1$ of $A$ times column $1$ of $A^{-1}$ is $\frac{1}{3}(-2 - 4 + 9) = 1$, and row $1$ times column $2$ is $\frac{1}{3}(-4 + 22 - 18) = 0$.
Note the transpose: entry $(2, 3)$ of $A^{-1}$ is $-2$, which is the cofactor $C_{32} = -(1 \cdot 6 - 3 \cdot 4) = 6$ divided by $-3$.

### Why each hypothesis is needed

The determinant must be a unit, not only nonzero.
Over $\mathbb{Z}$, the matrix $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has $\det A = 2$, and its inverse over $\mathbb{Q}$ has the entry $\frac{1}{2}$, so it has no inverse over $\mathbb{Z}$.
Over a field every nonzero element is a unit, and the condition becomes $\det A \neq 0$.
The ring must be commutative, because the determinant and the adjugate identity need it; the [[statement over rings|03Q7RE2HXR]] gives a quaternion matrix that is invertible although its Leibniz sum is $0$.

### What it gives you

For $n = 2$ and $ad - bc$ a unit,
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.$$
An integer matrix with $\det A = \pm 1$ has an integer inverse, namely $A^{-1} = \pm \operatorname{adj} A$.
Over $\mathbb{R}$, every entry of $A^{-1}$ is a polynomial in the entries of $A$ divided by $\det A$, so inversion is continuous on the invertible matrices.
A single entry of $A^{-1}$ costs only one determinant of size $n - 1$ and one of size $n$.

### The cost

The whole inverse needs $n^2$ cofactors of size $n - 1$.
Even if each of them is computed by elimination, this takes on the order of $n^5$ operations, while [[Gaussian elimination|0JVJ2WCXZH]] on $(A \mid I_n)$ takes on the order of $n^3$.
So the formula is a tool for theory and for small matrices, not for numerical work.

### The converse

The converse holds as well: if $A$ is invertible over $K$, then $\det A \cdot \det(A^{-1}) = \det I_n = 1$, so $\det A$ is a unit.
This is part 1 of the [[statement over rings|03Q7RE2HXR]].

### Generalizations

Applied to a vector $b$, the formula gives the solution $x = (\det A)^{-1} \operatorname{adj}(A) b$ of $Ax = b$.
Entry $i$ of $\operatorname{adj}(A) b$ is the determinant of $A$ with column $i$ replaced by $b$, which gives [[Cramer's rule|0977KZ6PQB]].

## Explanations

### L1 human

This formula gives every entry of the inverse as a cofactor divided by the determinant.
For a $2 \times 2$ matrix it says: swap the two diagonal entries, negate the other two, and divide by $ad - bc$.
It is the formula most students learn first for $2 \times 2$ inverses.
It is useful for small matrices and for proofs, but slow for large ones.

### L2 human

Here is a typical problem: invert $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ over $\mathbb{Z}$.

1. The determinant is $2 \cdot 3 - 1 \cdot 5 = 1$, a unit of $\mathbb{Z}$.
2. The adjugate is $\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
3. Since $\det A = 1$, the inverse is the adjugate itself.
4. Check:
$$\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I_2.$$

The inverse has integer entries, as the case $\det A = \pm 1$ predicts.
Watch out: the formula uses the transpose of the cofactor matrix, and with the cofactor matrix itself the product with $A$ is not $(\det A) I_n$ in general, as the [[non-example|2BJC4DHCMK]] shows.

### L3 human

The formula shows that $A \mapsto A^{-1}$ is a regular map on $\mathrm{GL}_n$: its entries are polynomials in the entries of $A$ divided by $\det A$.
Together with the converse, it shows that $\mathrm{GL}_n(K)$ is the set of matrices whose determinant lies in the unit group $K^{\times}$, for every commutative ring $K$.
In the language of algebraic groups, $\mathrm{GL}_n$ has the coordinate ring $\mathbb{Z}[x_{ij}][1/\det]$, and the formula writes the inverse in these coordinates.
