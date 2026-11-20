---
tag: XSZEXPCWA6
kind: proof
name: Proof of Sylvester's determinant identity by the Schur complement
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
proves: 7SSKBQYFW1
methods: [0NTF6DMVAP]
uses: [0KA7A4ENVJ, 0SD528P0EK, 009CY8JXFX, 03Q7RE2HXR, 0Q9EZS90GY, 0VF11ZTTMD, FBSAPTP1PR]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_determinant_identity
---

## Proof

We prove the identity for a generic matrix, where $A_0$ is invertible, and then substitute values.

1. Let $R = \mathbb{Z}[x_{ij}]$ be the [[polynomial ring|0Q9EZS90GY]] in $n^2$ variables, and let $L$ be its [[field of fractions|0VF11ZTTMD]].
2. Let $A = (x_{ij})$ be the generic matrix, and write $A = \begin{pmatrix} A_0 & P \\ Q & D \end{pmatrix}$ with $A_0$ of size $k \times k$.
3. $\det A_0 \ne 0$, since $x_{ij} \mapsto \delta_{ij}$ sends it to $1$.
4. So $A_0$ is invertible over $L$, by the [[invertibility criterion|FBSAPTP1PR]].
5. Let $S = D - Q A_0^{-1} P$ be the Schur complement, with entries $s_{ij}$ for $k < i, j \le n$.
6. Fix $i, j > k$; the bordered submatrix for $b_{ij}$ is $\begin{pmatrix} A_0 & p_j \\ q_i & x_{ij} \end{pmatrix}$, with column $p_j$ of $P$ and row $q_i$ of $Q$.
7. By the [[Schur complement formula|0KA7A4ENVJ]] with blocks of sizes $k$ and $1$, $b_{ij} = \det A_0 \cdot (x_{ij} - q_i A_0^{-1} p_j)$.
8. The number $x_{ij} - q_i A_0^{-1} p_j$ is the entry $s_{ij}$ of $S$, so $B = (\det A_0)\, S$.
9. By the rule for [[scaling rows|009CY8JXFX]], applied to each of the $n - k$ rows, $\det B = (\det A_0)^{n-k} \det S$.
10. By the Schur complement formula for $A$, $\det A = \det A_0 \cdot \det S$.
11. By steps 9 and 10, $\det B = (\det A_0)^{n-k-1} \det A$ in $L$.
12. Both sides lie in $R$, which is a subring of $L$, so the identity holds in $R$.
13. For a matrix over any commutative ring $K$, the homomorphism $R \to K$ that sends $x_{ij}$ to the entries carries both sides to $K$.
14. By [[naturality|03Q7RE2HXR]], the identity holds over $K$.

## Idea

Each bordered minor is $\det A_0$ times one entry of the Schur complement.
So $B$ is $\det A_0$ times the Schur complement, and the Schur complement formula gives the rest.
The generic matrix removes the need for $A_0$ to be invertible.

## Variants

For $k = n - 2$, the [[proof of the Desnanot-Jacobi identity|DBJZFHD9PR]] gives a direct argument with the adjugate.
