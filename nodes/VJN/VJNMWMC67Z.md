---
tag: VJNMWMC67Z
kind: proof
name: Proof of the invertibility of a triangular matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
proves: 7X1B65CTG4
methods: [01XM7JEKHY, 0J0XBKG64S, 0NTF6DMVAP]
uses: [0TWTS88TWN, FMCX4D7RD4, 2ZH4X4Q99D, 0N4XY7Z3NN, 00J3KZP8Y0, 0ATFVE08MW, 073E4XC016, 09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Proof

First let $U = (u_{ij})$ be [[upper triangular|0N4XY7Z3NN]], so $u_{ij} = 0$ for $i > j$.

**A zero on the diagonal makes $U$ singular.**

1. Suppose that some $u_{kk} = 0$, and take the smallest such $k$. So $u_{ii} \ne 0$ for $i < k$.
2. Define $x \in F^n$ by $x_k = 1$ and $x_j = 0$ for $j > k$.
3. For $i = k - 1, k - 2, \dots, 1$ in turn, put $x_i = -u_{ii}^{-1} \sum_{i < j \le k} u_{ij} x_j$. This is [[back substitution|0ATFVE08MW]], and it is possible because $u_{ii} \ne 0$.
4. Row $i < k$ of $Ux$ is $u_{ii} x_i + \sum_{i < j \le k} u_{ij} x_j = 0$, by step 3.
5. Row $k$ of $Ux$ is $u_{kk} x_k + \sum_{j > k} u_{kj} x_j = 0 \cdot 1 + 0 = 0$.
6. Row $i > k$ of $Ux$ is $\sum_{j \ge i} u_{ij} x_j = 0$, since $x_j = 0$ for $j \ge i > k$.
7. So $Ux = 0$ with $x \ne 0$. If $VU = I_n$ for some $V$, then $x = VUx = 0$, by [[associativity|073E4XC016]], which is false. So $U$ is not invertible.

**A nonzero diagonal gives an upper triangular inverse.**

8. Suppose now that each $u_{ii} \ne 0$. Fix a column index $j$. We solve $Ux = e_j$ with $x_i = 0$ for $i > j$.
9. Rows $i > j$ of $Ux$ are $\sum_{l \ge i} u_{il} x_l = 0$, which matches entry $i$ of $e_j$.
10. Row $j$ is $u_{jj} x_j = 1$, so $x_j = u_{jj}^{-1}$.
11. For $i = j - 1, \dots, 1$ in turn, row $i$ gives $x_i = -u_{ii}^{-1} \sum_{i < l \le j} u_{il} x_l$.
12. Let $X$ be the matrix whose column $j$ is this solution. Then $UX = I_n$, $X$ is upper triangular by step 8, and $x_{jj} = u_{jj}^{-1} \ne 0$ by step 10.
13. Apply steps 8 to 12 to $X$ in place of $U$. They give an upper triangular $Y$ with $XY = I_n$.
14. By associativity, $U = U(XY) = (UX)Y = Y$. So $XU = XY = I_n$.
15. By steps 12 and 14 and the [[definition|0TWTS88TWN]], $U$ is invertible. Also, $U^{-1} = X$ is upper triangular with diagonal entries $u_{jj}^{-1}$, by the [[uniqueness of the inverse|FMCX4D7RD4]].

**Lower triangular matrices.**

16. Let $L$ be [[lower triangular|00J3KZP8Y0]]. Then the [[transpose|09DXWYRD43]] $L^{\mathsf{T}}$ is upper triangular with the same diagonal.
17. By part 2 of the [[rules for inverses|2ZH4X4Q99D]], $L$ is invertible exactly when $L^{\mathsf{T}}$ is invertible. By steps 7 and 15, this holds exactly when each diagonal entry is nonzero.
18. Then $L^{-1} = ((L^{\mathsf{T}})^{-1})^{\mathsf{T}}$ is the transpose of an upper triangular matrix, so it is lower triangular, with diagonal entries $l_{ii}^{-1}$.

**The subgroups.**

19. If $U$ and $V$ are upper triangular, then entry $(i, k)$ of $UV$ is $\sum_j u_{ij} v_{jk}$. A term is nonzero only if $i \le j \le k$. So $UV$ is upper triangular, and $(UV)_{ii} = u_{ii} v_{ii}$.
20. By step 19, a product of invertible upper triangular matrices is upper triangular with nonzero diagonal. By step 15, the inverse is again of this kind, and $I_n$ is of this kind. So these matrices form a subgroup of $\mathrm{GL}_n(F)$.
21. If all $u_{ii} = 1$ and all $v_{ii} = 1$, then steps 19 and 10 give diagonal entries $1$ for $UV$ and for $U^{-1}$. So the unit upper triangular matrices form a subgroup.
22. The lower triangular cases follow from steps 19 to 21 by the transpose, since $(LM)^{\mathsf{T}} = M^{\mathsf{T}} L^{\mathsf{T}}$.

## Idea

Back substitution solves an upper triangular system from the bottom up, and it divides only by diagonal entries.
If no diagonal entry is $0$, it solves $Ux = e_j$ for each $j$, and the solutions stay in the upper part.
If a diagonal entry is $0$, the same method makes a nonzero solution of $Ux = 0$.

## Variants

Over a field, part 1 also follows from the determinant: $\det U = u_{11} \cdots u_{nn}$, by the [[triangular determinant theorem|0K1KKMFHYH]].
Another proof writes $U = D(I_n + N)$ with $D$ diagonal and $N$ strictly upper triangular, hence [[nilpotent|07BSPZPSMF]] with $N^n = 0$; then $(I_n + N)^{-1} = I_n - N + N^2 - \dots + (-N)^{n-1}$.
