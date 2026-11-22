---
tag: RDKYJR8P1R
kind: proof
name: Proof of Sylvester's law of inertia by comparing subspaces
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
proves: 0WFED3K3DQ
methods: [0NTF6DMVAP]
uses: [0Z3FEWZ8HA, 0SPYAGE7T0, 0N28QN4CYA, 0TWTS88TWN, 09GK5PS824, 0EVHJFTG9Z, 0HR573CHNM, 05G2G0P224, 06HTJNCMPA, 0QW084460E, 0QK7FPE6VE]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 6.19
---

## Proof

We prove part 1 by finding two subspaces that would have to meet if the counts were different, and then we deduce parts 2 and 3.

1. Let $q(x) = x^{\mathsf{T}} A x$ for $x \in \mathbb{R}^n$.
   Let $d_1, \dots, d_n$ be the diagonal entries of $D$, and $d'_1, \dots, d'_n$ those of $D'$.
2. For $y \in \mathbb{R}^n$, the [[transpose of a product|09GK5PS824]] gives $q(Py) = y^{\mathsf{T}} P^{\mathsf{T}} A P y = y^{\mathsf{T}} D y = \sum_i d_i y_i^2$.
3. In the same way, $q(P' z) = \sum_j d'_j z_j^2$ for $z \in \mathbb{R}^n$.
4. Let $p$ be the number of indices $i$ with $d_i > 0$, and $p'$ the number of indices $j$ with $d'_j > 0$.
   Let $I = \{ i : d_i > 0 \}$ and $J = \{ j : d'_j \le 0 \}$.
5. Let $S$ be the [[span|0HR573CHNM]] of the columns $P e_i$ with $i \in I$.
   Let $T$ be the span of the columns $P' e_j$ with $j \in J$.
6. The columns of an [[invertible|0TWTS88TWN]] matrix $P$ are [[linearly independent|0EVHJFTG9Z]]: if $Pc = 0$, then $c = P^{-1} P c = 0$.
   The same holds for $P'$.
7. By step 6 and the definition of [[dimension|05G2G0P224]], $\dim S = p$ and $\dim T = n - p'$.
8. Let $x \in S$ with $x \ne 0$.
   Then $x = Py$, where $y \ne 0$ and $y_i = 0$ for $i \notin I$.
   By step 2, $q(x) = \sum_{i \in I} d_i y_i^2 > 0$, since every term is at least $0$ and some $y_i$ with $i \in I$ is not $0$.
9. Let $x \in T$.
   Then $x = P' z$, where $z_j = 0$ for $j \notin J$.
   By step 3, $q(x) = \sum_{j \in J} d'_j z_j^2 \le 0$.
10. By steps 8 and 9, no nonzero vector lies in both $S$ and $T$, so $S \cap T = \{ 0 \}$ and $\dim(S \cap T) = 0$.
11. By [[Grassmann's formula|06HTJNCMPA]], $\dim(S + T) = \dim S + \dim T - \dim(S \cap T) = p + (n - p')$.
12. The subspace $S + T$ lies in $\mathbb{R}^n$, which has [[dimension $n$|0QK7FPE6VE]].
    By [[the dimension of a subspace|0QW084460E]], $p + n - p' \le n$, so $p \le p'$.
13. Exchanging the roles of $(P, D)$ and $(P', D')$ gives $p' \le p$.
    So $p = p'$.
14. The matrix $-A$ is [[symmetric|0N28QN4CYA]], with $P^{\mathsf{T}} (-A) P = -D$ and $P'^{\mathsf{T}} (-A) P' = -D'$.
    The positive entries of $-D$ are the negative entries of $D$, and the same holds for $D'$.
15. Applying steps 1 to 13 to $-A$ shows that $D$ and $D'$ have the same number of negative diagonal entries.
16. The number of zero diagonal entries is $n$ minus the numbers of positive and negative entries.
    By steps 13 and 15, it is also the same for $D$ and $D'$, which proves part 1.
17. For part 2, let $A$ be the matrix of $Q$ in some basis.
    By [[the diagonalization theorem|0Z3FEWZ8HA]], there is a basis $(f_1, \dots, f_n)$, orthogonal for $Q$, with $Q(\sum_i y_i f_i) = \sum_i d_i y_i^2$.
18. Let $g_i = f_i / \sqrt{\lvert d_i \rvert}$ when $d_i \ne 0$, and $g_i = f_i$ when $d_i = 0$.
    Then $Q(g_i) = d_i / \lvert d_i \rvert = \pm 1$ when $d_i \ne 0$, and $Q(g_i) = 0$ otherwise.
19. The basis $(g_i)$ is still orthogonal, since each $g_i$ is a multiple of $f_i$.
    Order it with the vectors of value $1$ first, then those of value $-1$, then those of value $0$.
20. In this basis $Q$ has the form of part 2.
    The matrix of $Q$ in this basis is congruent to $A$ by the [[change of basis rule|0SPYAGE7T0]], so by part 1 the numbers of entries $1$ and $-1$ are the $p$ and $q$ of $A$.
21. For part 3, let $A$ and $A'$ be real symmetric matrices with $A' = S^{\mathsf{T}} A S$ for an invertible $S$.
    Let $P'$ be invertible with $P'^{\mathsf{T}} A' P' = D'$ diagonal.
22. Then $(S P')^{\mathsf{T}} A (S P') = D'$, and $S P'$ is invertible.
    By part 1 for $A$, the matrix $D'$ has the same $p$ and $q$ as every diagonal matrix congruent to $A$, so $A$ and $A'$ have the same $p$ and $q$.
23. Conversely, let $A$ and $A'$ have the same $p$ and $q$.
    By part 2 in matrix form, both are congruent to $\operatorname{diag}(I_p, -I_q, 0)$.
24. Congruence is symmetric: if $A_1 = S^{\mathsf{T}} A_2 S$, then $A_2 = (S^{-1})^{\mathsf{T}} A_1 S^{-1}$.
    It is transitive, because $(S_1 S_2)^{\mathsf{T}} A (S_1 S_2) = S_2^{\mathsf{T}} (S_1^{\mathsf{T}} A S_1) S_2$.
    So $A$ and $A'$ are congruent.

## Idea

The positive entries of $D$ give a subspace of dimension $p$ on which the form is positive.
The other entries of $D'$ give a subspace of dimension $n - p'$ on which the form is never positive.
These two subspaces meet only in $0$, so their dimensions add up to at most $n$, and this forces $p \le p'$.
The same argument shows that $p$ is the largest dimension of a subspace on which the form is positive definite, a number that does not depend on any basis.

## Variants

A proof by continuity works for invertible $A$.
If $\det P < 0$, first change the sign of one column of $P$, which does not change $D$.
Then join $I$ to $P$ by a path $P_t$ of invertible matrices.
The matrices $P_t^{\mathsf{T}} A P_t$ stay invertible, so no eigenvalue crosses $0$, and the number of positive eigenvalues stays the same along the path.
So $D$ has as many positive entries as $A$ has positive eigenvalues.
This proof needs the continuity of eigenvalues and the fact that the invertible matrices of positive determinant form a connected set.

With [[the principal axis theorem|0PR5P9Z4KM]], one can also compare each diagonal form with the eigenvalues of $A$.
This gives part 1 too, but it uses the spectral theorem.
