---
tag: NRPFJZNDZ6
kind: proof
name: Proof of the Cholesky decomposition by induction on the size
msc: [15A23, 65F05]
proves: 0WKG8CYY6A
uses: [0QQCG3JWJ4, 0EKZCX4K3P, 0EZSD6T9E0, 0MKABWDRNC, 0EX045E2BP, 09GK5PS824, 0K1KKMFHYH, FBSAPTP1PR, 068BZBXE0C]
sources:
  - url: https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/
---

## Proof

We prove existence by induction on $n$, then uniqueness, then the real case. Here $^*$ is the [[conjugate transpose|0EX045E2BP]].

1. For matrices $X$ and $Y$ with $XY$ defined, $(XY)^* = Y^* X^*$. This is the [[transpose of a product|09GK5PS824]] with all entries conjugated.
2. For $n = 1$, $A = (a)$ and $a = e_1^* A e_1 > 0$ by [[positive definiteness|0QQCG3JWJ4]]. By the [[existence of square roots|068BZBXE0C]], $L = (\sqrt a)$ works.
3. Let $n \ge 2$ and assume existence for size $n - 1$. Since $A$ is [[Hermitian|0EKZCX4K3P]], $A = \begin{pmatrix} A' & b \\ b^* & c \end{pmatrix}$ with $A'$ of size $n - 1$, $b \in \C^{n-1}$ and $c \in \C$.
4. The block $A'$ is Hermitian. For $z \in \C^{n-1}$ with $z \ne 0$, let $x = (z, 0)$. Then $z^* A' z = x^* A x > 0$. So $A'$ is positive definite.
5. By the induction hypothesis, $A' = L' L'^*$ with $L'$ [[lower triangular|0EZSD6T9E0]] and with positive diagonal entries.
6. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det L'$ is the product of these entries, so it is nonzero. So $L'$ is [[invertible|FBSAPTP1PR]], and so is $L'^*$.
7. Let $m = L'^{-1} b$ and $w = -(L'^*)^{-1} m$. Let $x \in \C^n$ be $w$ followed by the entry $1$, so $x \ne 0$.
8. We have $A' w = L' L'^* w = -L' m = -b$. Expanding in blocks gives $x^* A x = w^* A' w + w^* b + b^* w + c = b^* w + c$.
9. By step 1, $b^* = (L' m)^* = m^* L'^*$. So $b^* w = -m^* L'^* (L'^*)^{-1} m = -m^* m$.
10. By steps 7 to 9, $s = c - m^* m$ equals $x^* A x$. So $s$ is a positive real number.
11. Let $d = \sqrt s > 0$, and let $L = \begin{pmatrix} L' & 0 \\ m^* & d \end{pmatrix}$. It is lower triangular with positive diagonal entries.
12. Block multiplication gives $L L^* = \begin{pmatrix} L' L'^* & L' m \\ m^* L'^* & m^* m + d^2 \end{pmatrix}$.
13. By steps 5, 7, 9 and 10, this equals $\begin{pmatrix} A' & b \\ b^* & c \end{pmatrix} = A$. This completes the induction.
14. For uniqueness we need a lemma. Let $M$ be an invertible lower triangular matrix with entries $m_{ij}$. As in step 6, $m_{ii} \ne 0$ for all $i$.
15. Fix $j$ and let $y$ be column $j$ of $M^{-1}$, so $My = e_j$. For $i < j$, row $i$ reads $\sum_{k \le i} m_{ik} y_k = 0$.
16. For $i = 1, 2, \dots, j - 1$ in turn, this gives $m_{ii} y_i = -\sum_{k < i} m_{ik} y_k = 0$. So $y_i = 0$ for $i < j$, and row $j$ gives $y_j = 1 / m_{jj}$.
17. So $M^{-1}$ is lower triangular with diagonal entries $1/m_{jj}$.
18. If $S$ and $T$ are lower triangular, then $(ST)_{ij} = \sum_k s_{ik} t_{kj}$ has nonzero terms only for $j \le k \le i$. So $ST$ is lower triangular with diagonal entries $s_{ii} t_{ii}$.
19. The same argument shows that a product of [[upper triangular|0MKABWDRNC]] matrices is upper triangular. The conjugate transpose of a lower triangular matrix is upper triangular.
20. Now let $A = L L^* = M M^*$ with $L$ and $M$ lower triangular with positive diagonal entries. Both are invertible, as in step 6.
21. Let $D = M^{-1} L$. By steps 17 and 18, $D$ is lower triangular with positive diagonal entries $l_{ii} / m_{ii}$.
22. From $L L^* = M M^*$ we get $D L^* = M^*$, so $D = M^* (L^*)^{-1}$.
23. By step 1, $(L^{-1})^* L^* = (L L^{-1})^* = I$, so $(L^*)^{-1} = (L^{-1})^*$. By steps 17 and 19, it is upper triangular.
24. By steps 19, 22 and 23, $D$ is upper triangular. It is also lower triangular, so $D$ is diagonal with positive diagonal entries $d_{ii}$.
25. Then $L = MD$, so $M M^* = L L^* = M D D^* M^*$. Multiplying by $M^{-1}$ on the left and $(M^*)^{-1}$ on the right gives $D D^* = I$.
26. So $d_{ii}^2 = 1$, and $d_{ii} = 1$ since $d_{ii} > 0$. Hence $D = I$ and $L = M$.
27. Real case: let $A$ be real, and let $\bar L$ be the matrix of complex conjugates of the entries of $L$.
28. Then $\bar L$ is lower triangular with the same positive diagonal entries, and $\bar L\, \bar L^* = \overline{L L^*} = \bar A = A$.
29. By the uniqueness of steps 20 to 26, $\bar L = L$. So all entries of $L$ are real.

## Idea

Split off the last row and column. The top left block has a Cholesky factor by induction, and the last row of $L$ is then forced by two equations. The only delicate point is that $c - m^* m$ is positive, and it is the value $x^* A x$ at a well chosen vector $x$.
