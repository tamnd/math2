---
tag: ~deeee143
kind: proof
name: Proof of the adjugate of a product by the Cauchy-Binet formula
msc: ["15A09", "15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: ~92a05c79
methods: [XP5SDYKJX0, DX2H7AD66G]
uses: [08WE2W7DYS, 0GMPYM0NSR, 0SD528P0EK, 0ZZQ2E1MTE, 0PPG793642, 0528HKWZ1Z, 04CPJ6AF00, 03Q7RE2HXR]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Binet_formula
    locator: Statement
---

## Proof

For a matrix $X$, write $X^{(j)}_{(i)}$ for $X$ with row $j$ and column $i$ deleted, so the cofactor is $C_{ji}(X) = (-1)^{i+j} \det X^{(j)}_{(i)}$.

1. Part 1. By the [[definition of the adjugate|0GMPYM0NSR]], $\operatorname{adj}(AB)_{ij} = (-1)^{i+j} \det (AB)^{(j)}_{(i)}$.
2. Deleting row $j$ of a product deletes row $j$ of the left factor, and deleting column $i$ deletes column $i$ of the right factor. So $(AB)^{(j)}_{(i)} = A^{(j)} B_{(i)}$.
3. Here $A^{(j)}$ is $(n-1) \times n$ and $B_{(i)}$ is $n \times (n-1)$. The sets of $n - 1$ columns of $A^{(j)}$ are the complements of single indices $k$.
4. By the [[Cauchy-Binet formula|08WE2W7DYS]], $\det (A^{(j)} B_{(i)}) = \sum_{k=1}^{n} \det A^{(j)}_{(k)} \det B^{(k)}_{(i)}$.
5. So $\operatorname{adj}(AB)_{ij} = \sum_k (-1)^{j+k} \det A^{(j)}_{(k)} \cdot (-1)^{k+i} \det B^{(k)}_{(i)}$, since $(-1)^{2k} = 1$.
6. The two factors are the cofactors $C_{jk}(A) = \operatorname{adj}(A)_{kj}$ and $C_{ki}(B) = \operatorname{adj}(B)_{ik}$.
7. So $\operatorname{adj}(AB)_{ij} = \sum_k \operatorname{adj}(B)_{ik} \operatorname{adj}(A)_{kj} = (\operatorname{adj} B \operatorname{adj} A)_{ij}$.
8. Part 2. Deleting row $j$ and column $i$ of $A^{T}$ gives the transpose of $A^{(i)}_{(j)}$. By the [[transpose rule|0ZZQ2E1MTE]], the cofactors satisfy $C_{ji}(A^{T}) = C_{ij}(A)$.
9. So $\operatorname{adj}(A^{T})_{ij} = C_{ij}(A) = \operatorname{adj}(A)_{ji}$.
10. Part 3. Each [[minor|0SD528P0EK]] of order $n - 1$ of $cA$ has $n - 1$ rows scaled by $c$. By [[multilinearity|0PPG793642]], it is $c^{n-1}$ times the minor of $A$.
11. Part 4. By the [[adjugate identity|0528HKWZ1Z]] and the [[product rule|04CPJ6AF00]], $\det A \det(\operatorname{adj} A) = \det((\det A) I_n) = (\det A)^n$.
12. Let $X = (x_{ij})$ be the generic matrix over $R = \mathbb{Z}[x_{ij}]$. The polynomial $\det X$ is nonzero, since $\det I_n = 1$, and $R$ has no zero divisors.
13. So step 11 for $X$ can be divided by $\det X$, and $\det(\operatorname{adj} X) = (\det X)^{n-1}$ in $R$.
14. For any $A$ over $K$, the ring homomorphism $R \to K$ with $x_{ij} \mapsto a_{ij}$ sends $X$ to $A$. By [[naturality of det|03Q7RE2HXR]] (part 2), it sends $\det X$ to $\det A$ and each minor of $X$ to the same minor of $A$. So it sends step 13 to part 4.

## Idea

Each entry of $\operatorname{adj}(AB)$ is a minor of order $n - 1$ of a product, and Cauchy-Binet splits it into a sum of products of minors of $A$ and of $B$.
The signs pair up into cofactors, and the sum is an entry of $\operatorname{adj} B \operatorname{adj} A$.
Part 4 is the determinant of the adjugate identity, with $\det A$ cancelled in the generic case.

## Variants

For invertible $A$ and $B$ over a field, part 1 follows from $\operatorname{adj} A = (\det A) A^{-1}$ and $(AB)^{-1} = B^{-1} A^{-1}$.
The general case then follows by the generic matrix argument of steps 12 to 14, applied to two generic matrices.
