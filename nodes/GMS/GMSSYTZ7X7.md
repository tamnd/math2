---
tag: GMSSYTZ7X7
kind: proof
name: Proof of the adjugate of a product by the Cauchy-Binet formula
msc: ["15A09", "15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: 3KDKBZ0WK2
methods: [XP5SDYKJX0, DX2H7AD66G]
uses: [08WE2W7DYS, 0GMPYM0NSR, 0SD528P0EK, 0ZZQ2E1MTE, 0PPG793642, 0528HKWZ1Z, 04CPJ6AF00, 03Q7RE2HXR]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Binet_formula
    locator: Statement
---

## Proof

We prove part 1 by applying Cauchy-Binet to each entry, parts 2 and 3 directly from the minors, and part 4 for the generic matrix first.
For a matrix $X$, write $X^{(j)}$ for $X$ with row $j$ deleted, $X_{(i)}$ for $X$ with column $i$ deleted, and $X^{(j)}_{(i)}$ when both are deleted.
So the cofactor of $X$ at $(j, i)$ is $C_{ji}(X) = (-1)^{i+j} \det X^{(j)}_{(i)}$.

*Part 1.*

1. By the [[definition of the adjugate|0GMPYM0NSR]], $\operatorname{adj}(AB)_{ij} = C_{ji}(AB) = (-1)^{i+j} \det (AB)^{(j)}_{(i)}$.
2. Row $j$ of $AB$ uses only row $j$ of $A$, and column $i$ of $AB$ uses only column $i$ of $B$.
   So $(AB)^{(j)}_{(i)} = A^{(j)} B_{(i)}$.
3. Here $A^{(j)}$ has size $(n-1) \times n$ and $B_{(i)}$ has size $n \times (n-1)$.
   A set of $n - 1$ columns of $A^{(j)}$ is the complement of a single index $k$.
4. By the [[Cauchy-Binet formula|08WE2W7DYS]],
$$\det \big( A^{(j)} B_{(i)} \big) = \sum_{k=1}^{n} \det A^{(j)}_{(k)} \det B^{(k)}_{(i)}.$$
5. Since $(-1)^{i+j} = (-1)^{j+k} (-1)^{k+i}$, steps 1 and 4 give
$$\operatorname{adj}(AB)_{ij} = \sum_{k=1}^{n} (-1)^{j+k} \det A^{(j)}_{(k)} \cdot (-1)^{k+i} \det B^{(k)}_{(i)}.$$
6. The two factors are the cofactors $C_{jk}(A) = \operatorname{adj}(A)_{kj}$ and $C_{ki}(B) = \operatorname{adj}(B)_{ik}$.
7. So $\operatorname{adj}(AB)_{ij} = \sum_k \operatorname{adj}(B)_{ik} \operatorname{adj}(A)_{kj} = (\operatorname{adj} B \operatorname{adj} A)_{ij}$.

*Part 2.*

8. Row $j$ of $A^{\mathsf{T}}$ is column $j$ of $A$, and column $i$ of $A^{\mathsf{T}}$ is row $i$ of $A$.
   So deleting row $j$ and column $i$ of $A^{\mathsf{T}}$ gives the transpose of $A^{(i)}_{(j)}$.
9. By the [[transpose rule|0ZZQ2E1MTE]], these two matrices have the same determinant, so $C_{ji}(A^{\mathsf{T}}) = C_{ij}(A)$.
10. Hence $\operatorname{adj}(A^{\mathsf{T}})_{ij} = C_{ji}(A^{\mathsf{T}}) = C_{ij}(A) = \operatorname{adj}(A)_{ji}$.

*Part 3.*

11. Each [[minor|0SD528P0EK]] of size $n - 1$ of $cA$ is the determinant of a matrix with $n - 1$ rows, each scaled by $c$.
    By [[multilinearity|0PPG793642]], it is $c^{n-1}$ times the same minor of $A$, and the signs of the cofactors do not change.

*Part 4.*

12. By the [[adjugate identity|0528HKWZ1Z]] and the [[product rule|04CPJ6AF00]],
$$\det A \cdot \det(\operatorname{adj} A) = \det \big( (\det A) I_n \big) = (\det A)^n.$$
13. We cannot divide by $\det A$ in general, so we first treat the generic matrix.
    Let $X = (x_{ij})$ have entries in $R = \mathbb{Z}[x_{ij}]$, the polynomial ring in $n^2$ variables.
14. The polynomial $\det X$ is not zero, because substituting $I_n$ gives $1$, and $R$ has no zero divisors.
    So step 12 for $X$ can be cancelled by $\det X$, and $\det(\operatorname{adj} X) = (\det X)^{n-1}$ in $R$.
15. For a matrix $A$ over $K$, the ring homomorphism $R \to K$ with $x_{ij} \mapsto a_{ij}$ sends $X$ to $A$.
    By [[naturality of the determinant|03Q7RE2HXR]], it sends $\det X$ to $\det A$ and each minor of $X$ to the same minor of $A$.
    So it sends the identity of step 14 to $\det(\operatorname{adj} A) = (\det A)^{n-1}$.

## Idea

Each entry of $\operatorname{adj}(AB)$ is a minor of size $n - 1$ of a product, and Cauchy-Binet splits such a minor into a sum of products of minors of $A$ and of $B$.
The signs pair up into cofactors, and the sum becomes an entry of $\operatorname{adj} B \operatorname{adj} A$, with the order reversed by the transpose in the definition.
Part 4 is the determinant of the adjugate identity.
The factor $\det A$ cancels for the generic matrix, and substitution carries the result to every matrix.

## Variants

For invertible $A$ and $B$ over a field, part 1 follows from $\operatorname{adj} A = (\det A) A^{-1}$ and $(AB)^{-1} = B^{-1} A^{-1}$.
The general case then follows by the generic matrix argument of steps 13 to 15, with two generic matrices $X$ and $Y$ over $\mathbb{Z}[x_{ij}, y_{ij}]$, which are invertible over its field of fractions.
Over $\mathbb{R}$ or $\mathbb{C}$ one can argue by continuity instead: both sides of each identity are polynomial in the entries, and the invertible matrices are dense.
