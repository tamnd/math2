---
tag: EEFAGXWAHA
kind: proof
name: Proof of the classification of complex quadratic forms by rescaling a diagonal form
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug1
proves: 0CEX9BRXRZ
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0PF6TM8TWT, 0Z3FEWZ8HA, 0HZNE5QZDJ, 0TX2YH2FQS, 0P24YW565F, 0SPYAGE7T0, 0KWXYZPJKN, 0EWQEYRVA8, 02FDWY55AS, 09GK5PS824, 0JP0W07Y9A, 0R8X9XA83A, 0VTQTPQGAV, 0EVHJFTG9Z, 096V7H13H9]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 6.19
---

## Proof

We show that the rank does not depend on the basis, then diagonalize and rescale, and last compare two forms of the same rank.
Let $F$ be $\mathbb{C}$, or an algebraically closed field with $2 \ne 0$, and let $V$ and $Q$ be as in the statement.
The symmetric matrix of $Q$ in a basis is the [[matrix|0P24YW565F]] of the [[associated symmetric bilinear form|0TX2YH2FQS]] $B(u, v) = \tfrac{1}{2} \bigl( Q(u + v) - Q(u) - Q(v) \bigr)$.
Recall that $B(v, v) = Q(v)$, since $Q(2v) = 4Q(v)$.

1. Let $\mathcal{B}$ and $\mathcal{B}'$ be bases of $V$, with matrices $M$ and $M'$ of $B$.
   Let $P$ be the [[change of basis matrix|0KWXYZPJKN]] from $\mathcal{B}$ to $\mathcal{B}'$, and $P'$ the one from $\mathcal{B}'$ to $\mathcal{B}$.
2. Substituting one expansion into the other and comparing coordinates in $\mathcal{B}$ gives $P P' = I$.
3. By the [[change of basis rule|0SPYAGE7T0]], $M' = P^{\mathsf{T}} M P$.
   By the [[transpose of a product|09GK5PS824]], $P'^{\mathsf{T}} P^{\mathsf{T}} = (P P')^{\mathsf{T}} = I$, so $M = P'^{\mathsf{T}} M' P'$.
4. By the [[rank of a product|02FDWY55AS]], $\operatorname{rank} M' \le \operatorname{rank} M$ and $\operatorname{rank} M \le \operatorname{rank} M'$.
   So all matrices of $Q$ have the same [[rank|0EWQEYRVA8]] $r$.
5. By the [[diagonalization of a quadratic form|0Z3FEWZ8HA]], $V$ has a basis $f_1, \dots, f_n$, and there are $a_i \in F$ with $Q(\sum_i y_i f_i) = \sum_i a_i y_i^2$.
6. Renumber the basis so that $a_i \ne 0$ for $i \le s$ and $a_i = 0$ for $i > s$, for some $s$ with $0 \le s \le n$.
7. For $i \le s$, the polynomial $t^2 - a_i$ has a root $c_i \in F$, since $F$ is [[algebraically closed|0PF6TM8TWT]].
   For $F = \mathbb{C}$ this is the [[fundamental theorem of algebra|0JP0W07Y9A]].
   Then $c_i^2 = a_i \ne 0$, so $c_i \ne 0$.
8. Let $e_i = f_i / c_i$ for $i \le s$ and $e_i = f_i$ for $i > s$.
   Rescaling basis vectors by nonzero numbers gives again a [[basis|0VTQTPQGAV]].
9. Since $\sum_i x_i e_i = \sum_{i \le s} (x_i / c_i) f_i + \sum_{i > s} x_i f_i$, step 5 gives $Q(\sum_i x_i e_i) = \sum_{i \le s} a_i (x_i / c_i)^2 = x_1^2 + \cdots + x_s^2$.
10. By step 9, $Q(e_i + e_j) = Q(e_i) + Q(e_j)$ for $i \ne j$, so $B(e_i, e_j) = 0$ for $i \ne j$.
11. Also $B(e_i, e_i) = Q(e_i)$, which is $1$ for $i \le s$ and $0$ for $i > s$.
    So the matrix of $B$ in the basis $(e_i)$ is diagonal, with $s$ ones and $n - s$ zeros.
12. The column space of this matrix is spanned by the first $s$ standard basis vectors, which are independent.
    So its rank is $s$, and $s = r$ by step 4.
13. By steps 9 and 12, $Q(x_1 e_1 + \cdots + x_n e_n) = x_1^2 + \cdots + x_r^2$, which proves the first claim.
14. Recall that $Q$ and $Q'$ are equivalent when there is an invertible linear map $T \colon V \to V$ with $Q'(v) = Q(Tv)$ for all $v$.
15. Suppose $Q$ and $Q'$ both have rank $r$.
    By step 13, there are bases $(e_i)$ and $(e'_i)$ with $Q(\sum_i x_i e_i) = \sum_{i \le r} x_i^2 = Q'(\sum_i x_i e'_i)$.
16. By [[the extension from a basis|0R8X9XA83A]], there are linear maps $T$ and $S$ with $T e'_i = e_i$ and $S e_i = e'_i$.
    Then $ST$ and $TS$ fix a basis, so they are the identity, and $T$ is invertible.
17. By step 15, $Q(T \sum_i x_i e'_i) = Q(\sum_i x_i e_i) = Q'(\sum_i x_i e'_i)$.
    So $Q' = Q \circ T$, and $Q$ and $Q'$ are equivalent.
18. Conversely, let $Q' = Q \circ T$ with $T$ invertible and linear.
    Then the form associated with $Q'$ is $B'(u, v) = B(Tu, Tv)$.
19. Let $(b_i)$ be a basis of $V$.
    The vectors $T b_i$ are [[linearly independent|0EVHJFTG9Z]], since $T$ is injective.
    There are $n$ of them, so they form a [[basis|096V7H13H9]].
20. By step 18, the matrix of $Q'$ in $(b_i)$ has entries $B(T b_i, T b_j)$, so it is the matrix of $Q$ in the basis $(T b_i)$.
21. By step 4, these two matrices have the same rank.
    So equivalent forms have the same rank, and the two conditions are equivalent.

## Idea

Diagonalize $Q$ first.
Over $\mathbb{C}$ every nonzero coefficient $a_i$ is a square $c_i^2$, so dividing $f_i$ by $c_i$ turns the coefficient into $1$.
The number of ones that remain is the rank of the matrix, which does not change under a change of basis.

## Variants

Only step 7 uses the field.
So the proof works whenever every element of $F$ is a square and $2 \ne 0$ in $F$.
Over $\mathbb{R}$ step 7 works only for the positive $a_i$, and the same rescaling with $c_i = \sqrt{\lvert a_i \rvert}$ gives the normal form of [[Sylvester's law of inertia|0WFED3K3DQ]].
