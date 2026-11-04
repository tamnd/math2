---
tag: RDKYJR8P1R
kind: proof
name: Proof of Sylvester's law of inertia by comparing subspaces
msc: [15A63, "11E04"]
proves: 0WFED3K3DQ
uses: [0N28QN4CYA, 0TWTS88TWN, 09GK5PS824, 0EVHJFTG9Z, 0HR573CHNM, 05G2G0P224, 06HTJNCMPA, 0QW084460E, 0QK7FPE6VE]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf
    locator: Theorem 6.19
---

## Proof

We show that the number of positive entries is the same, by finding two subspaces that would have to meet.

1. Let $q(x) = x^T A x$ for $x \in \R^n$. Let $d_1, \dots, d_n$ be the diagonal entries of $D$, and $d'_1, \dots, d'_n$ those of $D'$.
2. For $y \in \R^n$, the [[transpose of a product|09GK5PS824]] gives $q(Py) = y^T P^T A P y = y^T D y = \sum_i d_i y_i^2$.
3. In the same way, $q(P' z) = \sum_j d'_j z_j^2$ for $z \in \R^n$.
4. Let $p$ be the number of $i$ with $d_i > 0$, and $p'$ the number of $j$ with $d'_j > 0$. Let $I = \set{i : d_i > 0}$ and $J = \set{j : d'_j \le 0}$.
5. Let $S$ be the [[span|0HR573CHNM]] of the columns $P e_i$ with $i \in I$. Let $T$ be the span of the columns $P' e_j$ with $j \in J$.
6. The columns of an [[invertible|0TWTS88TWN]] matrix $P$ are [[linearly independent|0EVHJFTG9Z]]: if $Pc = 0$, then $c = P^{-1} P c = 0$. The same holds for $P'$.
7. By step 6 and the definition of [[dimension|05G2G0P224]], $\dim S = p$ and $\dim T = n - p'$.
8. Let $x \in S$ with $x \ne 0$. Then $x = Py$, where $y \ne 0$ and $y_i = 0$ for $i \notin I$. By step 2, $q(x) = \sum_{i \in I} d_i y_i^2 > 0$.
9. Let $x \in T$. Then $x = P' z$, where $z_j = 0$ for $j \notin J$. By step 3, $q(x) = \sum_{j \in J} d'_j z_j^2 \le 0$.
10. By steps 8 and 9, $S \cap T = \set{0}$, so $\dim(S \cap T) = 0$.
11. By [[Grassmann's formula|06HTJNCMPA]], $\dim(S + T) = p + (n - p')$.
12. The subspace $S + T$ lies in $\R^n$, which has [[dimension $n$|0QK7FPE6VE]]. By [[the dimension of a subspace|0QW084460E]], $p + n - p' \le n$, so $p \le p'$.
13. Exchanging the roles of $(P, D)$ and $(P', D')$ gives $p' \le p$. So $p = p'$.
14. The matrix $-A$ is [[symmetric|0N28QN4CYA]], with $P^T (-A) P = -D$ and $P'^T (-A) P' = -D'$. The positive entries of $-D$ are the negative entries of $D$.
15. Applying step 13 to $-A$, the matrices $D$ and $D'$ have the same number of negative diagonal entries.
16. The number of zero diagonal entries is $n$ minus the numbers of positive and negative entries. By steps 13 and 15, it is also the same for $D$ and $D'$.

## Idea

The positive entries of $D$ give a subspace of dimension $p$ on which the form is positive. The other entries of $D'$ give a subspace of dimension $n - p'$ on which it is not positive. These subspaces meet only in $0$, so their dimensions add to at most $n$, which forces $p \le p'$.
