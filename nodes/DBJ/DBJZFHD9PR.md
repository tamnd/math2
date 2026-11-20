---
tag: DBJZFHD9PR
kind: proof
name: Proof of the Desnanot–Jacobi identity by the adjugate
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

We multiply $M$ by the identity matrix with two columns replaced by cofactors, and we cancel $\det M$ for a generic matrix.

1. Let $M$ be $n \times n$ with $n \ge 3$, and let $C_{ij}$ be its [[cofactors|0W2QAVJQ1W]].
2. Let $X$ be the [[identity matrix|06DW9BAWB1]] $I_n$ with two columns replaced.
3. Column $1$ of $X$ is $(C_{11}, C_{12}, \dots, C_{1n})^T$, and column $n$ is $(C_{n1}, C_{n2}, \dots, C_{nn})^T$.
4. Entry $i$ of $M$ times column $1$ of $X$ is $\sum_j m_{ij} C_{1j}$.
5. By the [[adjugate identity|0528HKWZ1Z]], this is $\det M$ for $i = 1$ and $0$ for $i \ne 1$.
6. In the same way, $M$ times column $n$ of $X$ is $(\det M) e_n$.
7. For $2 \le j \le n - 1$, column $j$ of $MX$ is $M e_j$, which is column $j$ of $M$, by the [[matrix product|076JGP6R3T]].
8. So column $1$ of $MX$ is $(\det M) e_1$, column $n$ is $(\det M) e_n$, and the other columns are those of $M$.
9. By the [[Laplace expansion|0C08BQ3M05]] along column $1$ and then along the last column, $\det(MX) = (\det M)^2 \det M^{1,n}_{1,n}$.
10. For $2 \le j \le n - 1$, column $j$ of $X$ is $e_j$.
11. Laplace expansion along these $n - 2$ columns, one at a time, leaves the rows and columns $1$ and $n$.
12. So $\det X = \det \begin{pmatrix} C_{11} & C_{n1} \\ C_{1n} & C_{nn} \end{pmatrix} = C_{11} C_{nn} - C_{1n} C_{n1}$.
13. By [[multiplicativity|04CPJ6AF00]], $\det M \cdot (C_{11} C_{nn} - C_{1n} C_{n1}) = (\det M)^2 \det M^{1,n}_{1,n}$.
14. Now let $M$ be the generic matrix $(x_{ij})$ over the [[polynomial ring|0Q9EZS90GY]] $R = \mathbb{Z}[x_{ij}]$, which has no zero divisors.
15. Its determinant is not $0$, since $x_{ij} \mapsto \delta_{ij}$ sends it to $\det I_n = 1$.
16. So we can cancel $\det M$ in step 13, and $C_{11} C_{nn} - C_{1n} C_{n1} = \det M \cdot \det M^{1,n}_{1,n}$ in $R$.
17. By definition, $C_{11} = \det M^1_1$ and $C_{nn} = \det M^n_n$.
18. Also $C_{1n} C_{n1} = (-1)^{1+n} (-1)^{n+1} \det M^1_n \det M^n_1 = \det M^1_n \det M^n_1$.
19. So the identity holds in $R$.
20. For a matrix over any commutative ring $K$, the homomorphism $R \to K$ that sends $x_{ij}$ to the entries carries the identity to $K$, by [[naturality|03Q7RE2HXR]].

## Idea

Two columns of the adjugate turn two columns of $M$ into multiples of unit vectors.
The determinant of the product is $(\det M)^2$ times the interior minor, and the determinant of the factor is a $2 \times 2$ determinant of cofactors.
Dividing by $\det M$ is allowed for the generic matrix.

## Variants

The identity also follows from [[Sylvester's determinant identity|7SSKBQYFW1]] with $k = n - 2$; see its [[proof|XSZEXPCWA6]].
