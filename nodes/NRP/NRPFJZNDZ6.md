---
tag: NRPFJZNDZ6
kind: proof
name: Proof of the Cholesky decomposition by induction on the size
msc: [15A23, 65F05]
topics: [SS4EVPKT3A]
audience: ug1
proves: 0WKG8CYY6A
methods: [0ASJVEFA9J, GQHHNV79PA, 01XM7JEKHY]
uses: [0QQCG3JWJ4, 0EKZCX4K3P, 0EZSD6T9E0, 0MKABWDRNC, 0EX045E2BP, 09GK5PS824, 0K1KKMFHYH, FBSAPTP1PR, 068BZBXE0C, 0AM050KCAW]
sources:
  - url: https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/
  - url: https://en.wikipedia.org/wiki/Cholesky_decomposition
    locator: Statement
---

## Proof

We prove existence by induction on $n$, then uniqueness by comparing two factors, then the real case and the converse.
Here $^*$ is the [[conjugate transpose|0EX045E2BP]], and $(XY)^* = Y^* X^*$ whenever $XY$ is defined, by the [[transpose of a product|09GK5PS824]] with all entries conjugated.

*Existence.*

1. For $n = 1$ we have $A = (a)$, and $a = e_1^* A e_1 > 0$ by [[positive definiteness|0QQCG3JWJ4]]. By the [[existence of square roots|068BZBXE0C]], $L = (\sqrt a)$ works.
2. Let $n \ge 2$ and assume existence for size $n - 1$. Since $A$ is [[Hermitian|0EKZCX4K3P]], we can write $A = \begin{pmatrix} A' & b \\ b^* & c \end{pmatrix}$ with $A'$ of size $n - 1$, $b \in \C^{n-1}$ and $c \in \C$.
3. The block $A'$ is Hermitian, and it is positive definite. Indeed, for $z \ne 0$ in $\C^{n-1}$ the vector $x = (z, 0)$ is nonzero, and $z^* A' z = x^* A x > 0$.
4. By the induction hypothesis, $A' = L' L'^*$ with $L'$ [[lower triangular|0EZSD6T9E0]] with positive diagonal entries. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det L'$ is the product of these entries, so $L'$ and $L'^*$ are [[invertible|FBSAPTP1PR]].
5. Let $m = L'^{-1} b$, so that $L' m = b$ and, by the product rule for $^*$, $m^* L'^* = b^*$.
6. Let $w = -(L'^*)^{-1} m$, and let $x \in \C^n$ be $w$ followed by the entry $1$, so $x \ne 0$. Then $A' w = L' L'^* w = -L' m = -b$.
7. Expanding $x^* A x$ in blocks and using $w^* A' w = -w^* b$ from step 6 gives
$$x^* A x = w^* A' w + w^* b + b^* w + c = b^* w + c.$$
8. By step 5, $b^* w = -m^* L'^* (L'^*)^{-1} m = -m^* m$. So $s = c - m^* m$ equals $x^* A x$, and it is a positive real number.
9. Let $d = \sqrt s > 0$ and $L = \begin{pmatrix} L' & 0 \\ m^* & d \end{pmatrix}$. This matrix is lower triangular with positive diagonal entries.
10. Block multiplication gives $L L^* = \begin{pmatrix} L' L'^* & L' m \\ m^* L'^* & m^* m + d^2 \end{pmatrix}$. By steps 4, 5 and 8 this is $\begin{pmatrix} A' & b \\ b^* & c \end{pmatrix} = A$, which completes the induction.

*Two facts about triangular matrices.*

11. If $S$ and $T$ are lower triangular, then $(ST)_{ij} = \sum_k s_{ik} t_{kj}$ has nonzero terms only for $j \le k \le i$. So $ST$ is lower triangular with diagonal entries $s_{ii} t_{ii}$, and in the same way a product of [[upper triangular|0MKABWDRNC]] matrices is upper triangular.
12. Let $M$ be lower triangular with nonzero diagonal entries, and let $y$ be column $j$ of $M^{-1}$, so $My = e_j$. Row $i$ of this system reads $\sum_{k \le i} m_{ik} y_k = \delta_{ij}$.
13. Solving rows $1, 2, \dots, j - 1$ in turn gives $y_1 = \dots = y_{j-1} = 0$, and row $j$ then gives $y_j = 1/m_{jj}$. So $M^{-1}$ is lower triangular with diagonal entries $1/m_{jj}$.
14. The conjugate transpose of a lower triangular matrix is upper triangular. Also $(L^*)^{-1} = (L^{-1})^*$, because $(L^{-1})^* L^* = (L L^{-1})^* = I$.

*Uniqueness.*

15. Let $A = L L^* = M M^*$ with $L$ and $M$ lower triangular with positive diagonal entries. Both are invertible, as in step 4.
16. Let $D = M^{-1} L$. By steps 11 and 13, $D$ is lower triangular with positive diagonal entries $l_{ii} / m_{ii}$.
17. From $L L^* = M M^*$ we get $D L^* = M^*$, so $D = M^* (L^*)^{-1} = M^* (L^{-1})^*$. By steps 11, 13 and 14 this is upper triangular.
18. So $D$ is both lower and upper triangular, hence diagonal, with positive entries $d_{ii}$.
19. Now $L = MD$, so $M M^* = M D D^* M^*$. Multiplying by $M^{-1}$ on the left and by $(M^*)^{-1}$ on the right gives $D D^* = I$, so $d_{ii}^2 = 1$.
20. Since $d_{ii} > 0$, every $d_{ii} = 1$. Hence $D = I$ and $L = M$.

*The real case and the converse.*

21. Let $A$ be real, and let $\bar L$ be the matrix of complex conjugates of the entries of $L$. Then $\bar L$ is lower triangular with the same positive diagonal, and $\bar L \, \bar L^* = \overline{L L^*} = \bar A = A$.
22. By the uniqueness of steps 15 to 20, $\bar L = L$, so every entry of $L$ is real.
23. Let $A = L L^*$ with $L$ lower triangular with positive diagonal entries. As in step 4, $L$ is invertible, so the columns of $B = L^*$ are linearly independent.
24. Then $A = B^* B$, and [[the Gram matrix theorem|0AM050KCAW]] shows that $A$ is positive definite.

## Idea

Cut off the last row and the last column of $A$.
The block that remains is positive definite, so it has a Cholesky factor by induction.
The last row of $L$ is then forced: the off-diagonal part must be $m^* = (L'^{-1} b)^*$, and the corner must be the square root of $c - m^* m$.
The one point that needs thought is that $c - m^* m$ is positive, and the proof finds a vector $x$ with $x^* A x = c - m^* m$.
Uniqueness comes from a short trick: the quotient of two factors is triangular in both directions, so it is diagonal, and a positive diagonal unitary matrix is $I$.

## Variants

Existence also follows from [[Sylvester's criterion|0WKEF78PMV]].
The leading principal minors $\Delta_k$ are positive, so Gaussian elimination needs no row exchanges and has the positive pivots $\Delta_k / \Delta_{k-1}$.
That gives $A = L_1 U$ with $L_1$ unit lower triangular, and symmetry turns this into $A = L_1 D L_1^*$ with $D$ the diagonal of pivots, so $L = L_1 D^{1/2}$.

A second route uses the [[QR decomposition|0ERWG4NXQ9]].
By the Gram matrix theorem, a positive definite $A$ equals $B^* B$ for an invertible $B$, for example $B = A^{1/2}$.
If $B = QR$ with $R$ upper triangular with a positive diagonal, then $A = R^* Q^* Q R = R^* R$, and $L = R^*$.
