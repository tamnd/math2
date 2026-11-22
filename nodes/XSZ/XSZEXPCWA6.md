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

We prove the identity for the generic matrix, where the corner block is invertible over a field of fractions, and then we substitute values.

1. Let $R = \mathbb{Z}[x_{ij} : 1 \le i, j \le n]$ be the [[polynomial ring|0Q9EZS90GY]] in $n^2$ variables, and let $L$ be its [[field of fractions|0VF11ZTTMD]].
   Let $A = (x_{ij})$ be the generic matrix over $R$.
2. Write $A$ in blocks as
$$A = \begin{pmatrix} A_0 & P \\ Q & D \end{pmatrix},$$
   where $A_0$ is $k \times k$, $P$ is $k \times (n - k)$, $Q$ is $(n - k) \times k$ and $D$ is $(n - k) \times (n - k)$.
3. The polynomial $\det A_0$ is not zero.
   The substitution $x_{ij} \mapsto \delta_{ij}$ sends it to $\det I_k = 1$, and the zero polynomial would go to $0$.
4. So $\det A_0$ is invertible in the field $L$, and $A_0$ is invertible over $L$ by the [[invertibility criterion|FBSAPTP1PR]].
5. Let $S = D - Q A_0^{-1} P$ be the Schur complement of $A_0$, with entries $s_{ij}$ for $k < i, j \le n$.
   Its entry is $s_{ij} = x_{ij} - q_i A_0^{-1} p_j$, where $q_i$ is the row of $Q$ that belongs to row $i$ of $A$ and $p_j$ is the column of $P$ that belongs to column $j$ of $A$.
6. Fix $i, j > k$.
   The submatrix of $A$ with rows $1, \dots, k, i$ and columns $1, \dots, k, j$ is
$$\begin{pmatrix} A_0 & p_j \\ q_i & x_{ij} \end{pmatrix}.$$
7. The [[Schur complement formula|0KA7A4ENVJ]] for this matrix, with blocks of sizes $k$ and $1$, gives its determinant:
$$b_{ij} = \det A_0 \cdot (x_{ij} - q_i A_0^{-1} p_j) = \det A_0 \cdot s_{ij}.$$
8. By step 7, $B = (\det A_0)\, S$ as matrices over $L$.
9. Each of the $n - k$ rows of $B$ is $\det A_0$ times a row of $S$.
   By the rule for [[scaling a row|009CY8JXFX]], applied once to each row, $\det B = (\det A_0)^{n-k} \det S$.
10. The Schur complement formula for $A$ itself gives $\det A = \det A_0 \cdot \det S$.
11. Steps 9 and 10 give, in $L$,
$$\det B = (\det A_0)^{n-k-1} \cdot \det A_0 \cdot \det S = (\det A_0)^{n-k-1} \det A.$$
12. Both sides are polynomials, so they lie in $R$, and $R$ is a subring of $L$.
   So the identity holds in $R$.
13. Let $K$ be any commutative ring and let $M$ be an $n \times n$ matrix over $K$.
   The ring homomorphism $R \to K$ that sends $x_{ij}$ to the entry $m_{ij}$ sends $\det A$ to $\det M$ and each $b_{ij}$ to the matching bordered minor of $M$.
14. Determinants commute with ring homomorphisms by [[naturality|03Q7RE2HXR]], so applying the homomorphism to the identity of step 12 gives the identity for $M$ over $K$.

## Idea

Each bordered minor is a block determinant with the corner $A_0$ and one extra row and column, so the Schur complement formula writes it as $\det A_0$ times one entry of the Schur complement of $A_0$ in $A$.
So $B$ is $\det A_0$ times that Schur complement, and its determinant picks up the factor $(\det A_0)^{n-k}$.
The Schur complement formula for the whole matrix supplies $\det A$ and uses up one of the factors.
The generic matrix is the device that removes the need for $A_0$ to be invertible.

## Variants

For $k = n - 2$, the [[proof of the Desnanot-Jacobi identity|DBJZFHD9PR]] gives a direct argument with two columns of the adjugate.
Another classical proof uses the adjugate of $A$ and Jacobi's theorem on the minors of the adjugate, which writes each minor of $\operatorname{adj} A$ through a complementary minor of $A$.
