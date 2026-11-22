---
tag: DBJZFHD9PR
kind: proof
name: Proof of the Desnanot-Jacobi identity by the adjugate
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: KWW7519E58
methods: [0NTF6DMVAP]
uses: [0528HKWZ1Z, 0W2QAVJQ1W, 0C08BQ3M05, 04CPJ6AF00, 03Q7RE2HXR, 0Q9EZS90GY, 06DW9BAWB1, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
    locator: Desnanot–Jacobi identity and proof of correctness of the condensation algorithm
---

## Proof

We multiply $M$ by the identity matrix with its first and last columns replaced by columns of the adjugate, compute the determinant of the product in two ways, and cancel $\det M$ for the generic matrix.

1. Let $M = (m_{ij})$ be $n \times n$ with $n \ge 3$, and let $C_{ij} = (-1)^{i+j} \det M^i_j$ be its [[cofactors|0W2QAVJQ1W]].
2. Let $X$ be the [[identity matrix|06DW9BAWB1]] $I_n$ with two columns replaced.
   Column $1$ of $X$ is $(C_{11}, C_{12}, \dots, C_{1n})^{\mathsf{T}}$, and column $n$ of $X$ is $(C_{n1}, C_{n2}, \dots, C_{nn})^{\mathsf{T}}$.
   For $2 \le j \le n - 1$, column $j$ of $X$ is the unit vector $e_j$.
3. By the [[matrix product|076JGP6R3T]], entry $i$ of column $1$ of $MX$ is $\sum_j m_{ij} C_{1j}$.
   By the [[adjugate identity|0528HKWZ1Z]], this sum is $\det M$ for $i = 1$ and $0$ for $i \ne 1$.
   So column $1$ of $MX$ is $(\det M)\, e_1$.
4. In the same way, column $n$ of $MX$ is $(\det M)\, e_n$.
5. For $2 \le j \le n - 1$, column $j$ of $MX$ is $M e_j$, which is column $j$ of $M$.
6. Expand $\det(MX)$ by the [[Laplace expansion|0C08BQ3M05]] along column $1$, whose only nonzero entry is $\det M$ in position $(1, 1)$.
   Then expand the remaining matrix along its last column, whose only nonzero entry is $\det M$ in the last diagonal position.
   Both signs are $+1$, and what remains is the submatrix of $M$ without rows $1, n$ and columns $1, n$:
$$\det(MX) = (\det M)^2 \det M^{1,n}_{1,n}.$$
7. Now expand $\det X$ along the columns $2, \dots, n - 1$, one at a time.
   Each of them is a unit vector $e_j$, with its entry $1$ on the diagonal.
   So each expansion has a single term with sign $+1$, and it deletes row $j$ and column $j$.
   What remains is the $2 \times 2$ matrix on rows and columns $1$ and $n$:
$$\det X = \det \begin{pmatrix} C_{11} & C_{n1} \\ C_{1n} & C_{nn} \end{pmatrix} = C_{11} C_{nn} - C_{1n} C_{n1}.$$
8. By [[multiplicativity of the determinant|04CPJ6AF00]], $\det(MX) = \det M \cdot \det X$, so steps 6 and 7 give
$$\det M \cdot (C_{11} C_{nn} - C_{1n} C_{n1}) = (\det M)^2 \det M^{1,n}_{1,n}.$$
9. Now let $M$ be the generic matrix $(x_{ij})$ over the [[polynomial ring|0Q9EZS90GY]] $R = \mathbb{Z}[x_{ij}]$, which has no zero divisors.
   Its determinant is not $0$, since the substitution $x_{ij} \mapsto \delta_{ij}$ sends it to $\det I_n = 1$.
10. So we may cancel one factor $\det M$ in step 8, and in $R$
$$C_{11} C_{nn} - C_{1n} C_{n1} = \det M \cdot \det M^{1,n}_{1,n}.$$
11. By the definition of cofactors, $C_{11} = \det M^1_1$ and $C_{nn} = \det M^n_n$.
   Also $C_{1n} C_{n1} = (-1)^{1+n} (-1)^{n+1} \det M^1_n \det M^n_1 = \det M^1_n \det M^n_1$, because the two signs are equal.
   So the identity holds for the generic matrix.
12. For a matrix over any commutative ring $K$, the ring homomorphism $R \to K$ that sends each $x_{ij}$ to the matching entry carries every determinant to the matching determinant, by [[naturality|03Q7RE2HXR]].
   So it carries the identity of step 11 to the identity over $K$.

## Idea

Two columns of the adjugate are exactly what we need to turn two columns of $M$ into multiples of unit vectors.
After that, the product $MX$ has the determinant $(\det M)^2$ times the central minor, because the two unit columns peel off the outer rows and columns.
The factor $X$ is the identity except in two columns, so its determinant is the $2 \times 2$ determinant of four cofactors.
Comparing the two sides gives the identity with an extra factor $\det M$, and the generic matrix lets us divide by it.

## Variants

The identity also follows from [[Sylvester's determinant identity|7SSKBQYFW1]] with $k = n - 2$, after the interior rows and columns are moved to the front; see its [[proof by the Schur complement|XSZEXPCWA6]].
A third route is Jacobi's theorem on the minors of the adjugate, which gives every $2 \times 2$ minor of $\operatorname{adj} M$ as $\det M$ times a complementary minor of $M$.
