---
tag: NXAVS73SDP
kind: proof
name: Proof that the trace of a projection equals its rank
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
proves: BJTJ41YW55
uses: [0RH4E3CAV9, 0JGB7A6GTS, 0QW084460E, 0KCQ9Y3QKA, 0YQSGNYE3K, 0WCPH5Z7FA, 07PTPSZPME]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Properties and classification
---

## Proof

We find a basis in which $P$ is diagonal with entries $1$ and $0$, and then add the diagonal entries.

1. Let $n = \dim V$ and let $r = \rank P = \dim \operatorname{im} P$, by the [[definition of the rank|0JGB7A6GTS]].
2. The map $P$ fixes its image.
   Let $v \in \operatorname{im} P$, so $v = P(w)$ for some $w \in V$.
   By the [[definition of a projection|0RH4E3CAV9]], $P(v) = P(P(w)) = P(w) = v$.
3. The image and the kernel of $P$ are subspaces of $V$.
   By the [[theorem on the dimension of a subspace|0QW084460E]], they are finite-dimensional and have bases.
4. Let $u_1, \dots, u_r$ be a [[basis|0KCQ9Y3QKA]] of $\operatorname{im} P$ and let $w_1, \dots, w_k$ be a basis of $\ker P$.
5. Spanning.
   Let $v \in V$ and write $v = P(v) + (v - P(v))$.
   The first term lies in $\operatorname{im} P$.
6. By linearity and $P \circ P = P$, $P(v - P(v)) = P(v) - P(P(v)) = P(v) - P(v) = 0$.
   So the second term lies in $\ker P$.
7. By steps 4 to 6, $v$ is a linear combination of $u_1, \dots, u_r, w_1, \dots, w_k$, so these vectors span $V$.
8. Independence.
   Assume $\sum_i a_i u_i + \sum_j b_j w_j = 0$, and apply $P$.
   By step 2, $P(u_i) = u_i$, and $P(w_j) = 0$ since $w_j \in \ker P$, so $\sum_i a_i u_i = 0$.
9. The $u_i$ are linearly independent, so every $a_i = 0$.
   Then $\sum_j b_j w_j = 0$, and every $b_j = 0$, since the $w_j$ are linearly independent.
10. By steps 7 to 9, $B = (u_1, \dots, u_r, w_1, \dots, w_k)$ is a basis of $V$, and in particular $r + k = n$.
11. Since $P(u_i) = u_i$ and $P(w_j) = 0$, the [[matrix|0YQSGNYE3K]] of $P$ in $B$ is
    $$[P]_B = \operatorname{diag}(1, \dots, 1, 0, \dots, 0),$$
    with $r$ entries $1$ and $k$ entries $0$.
12. By the [[theorem on the trace of a linear map|0WCPH5Z7FA]], $\tr P = \tr [P]_B$.
    By the definition of the [[trace of a matrix|07PTPSZPME]], this is the sum $1 + \dots + 1 = r \cdot 1_F$ of $r$ terms.
13. So $\tr P = (\rank P) \cdot 1_F$.
14. If $F$ has characteristic $0$, then the map $\mathbb{Z} \to F$, $m \mapsto m \cdot 1_F$, is injective.
    So the element $\tr P$ determines the integer $r$, and $\tr P = \rank P$ under this identification.

## Idea

A projection is the identity on its image and zero on its kernel.
Bases of the image and of the kernel together give a basis of $V$.
In that basis the matrix is diagonal with $r$ ones, so the trace counts the ones.

## Variants

A proof with eigenvalues: $P^2 - P = 0$, so the minimal polynomial divides $x(x - 1)$, which has distinct roots.
So $P$ is diagonalizable with eigenvalues among $0$ and $1$, and the multiplicity of $1$ is $\dim \operatorname{im} P$.

A proof with a rank factorization, for an $n \times n$ matrix $A$ with $A^2 = A$ and rank $r$.
Write $A = CR$ with $C$ of size $n \times r$ and $R$ of size $r \times n$, both of rank $r$.
Then $C$ has a left inverse $L$ and $R$ has a right inverse $S$.
From $A^2 = A$ we get $RC = (LC)(RC)(RS) = L(CRCR)S = L(CR)S = I_r$.
So $\tr A = \tr(CR) = \tr(RC) = \tr I_r = r \cdot 1_F$.
