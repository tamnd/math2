---
tag: QZE2CYP536
kind: proof
name: Proof that a linear map multiplies volumes by the absolute value of its determinant
msc: ["15A15", "28A75"]
topics: [DTBK11SR77]
audience: grad
proves: RC5BTSG8T2
methods: [0NTF6DMVAP]
uses: [2Z2QVWZ262, WSW3B6KNW1, 0K9AAJ8G51, YSS4XNY9RC, 0NMN00FNW1, 04CPJ6AF00, 0K1KKMFHYH, 0M4SXE5WW3, 03Q7RE2HXR]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Signed volume of a parallelotope
---

## Proof

We show that $S \mapsto \lambda(A(S))$ is a constant multiple $c(A)$ of Lebesgue measure for invertible $A$, compute $c$ on generators of $\mathrm{GL}_n(\mathbb{R})$, and then treat singular $A$ separately.
Let $Q = [0, 1]^n$, so that $\lambda(Q) = 1$, and let $E_{ij}$ be the matrix with entry $1$ at $(i, j)$ and $0$ elsewhere.

*The scaling constant of an invertible matrix.*

1. Let $A$ be invertible.
   Then $A(S)$ is the preimage of $S$ under the continuous map $A^{-1}$, so $A(S)$ is Borel when $S$ is.
2. Define $\mu(S) = \lambda(A(S))$ for Borel sets $S$.
   Since $A$ is a bijection, it sends disjoint sets to disjoint sets and unions to unions, so $\mu$ is a measure.
3. Since $A(S + x) = A(S) + Ax$ and [[Lebesgue measure|2Z2QVWZ262]] is translation invariant, $\mu(S + x) = \mu(S)$ for every $x$.
4. A compact set $K$ has the compact image $A(K)$, because a [[continuous image of a compact set is compact|0K9AAJ8G51]].
   So $\mu(K) < \infty$, and $\mu$ is the image of $\lambda$ under the homeomorphism $A^{-1}$, hence a Radon measure.
5. The set $A^{-1}(Q)$ has $\mu(A^{-1}(Q)) = \lambda(Q) = 1$, so $\mu \ne 0$.
6. By the [[uniqueness of Haar measure|WSW3B6KNW1]] on the group $(\mathbb{R}^n, +)$, there is a constant $c(A) > 0$ with $\mu = c(A) \lambda$.
7. Evaluating at $Q$ gives $c(A) = \lambda(A(Q))$.
   In particular $c(I_n) = 1$.
8. For invertible $A$ and $B$ and every Borel set $S$,
$$c(AB) \lambda(S) = \lambda(A(B(S))) = c(A) \lambda(B(S)) = c(A) c(B) \lambda(S).$$
   With $S = Q$ this gives $c(AB) = c(A) c(B)$.

*The constant on diagonal matrices and on transvections.*

9. Let $D = \operatorname{diag}(d_1, \dots, d_n)$ be invertible.
   Then $D(Q)$ is a box whose sides are intervals of lengths $\lvert d_1 \rvert, \dots, \lvert d_n \rvert$.
10. So $c(D) = \lvert d_1 \cdots d_n \rvert$, and this equals $\lvert \det D \rvert$ by the [[triangular rule|0K1KKMFHYH]].
11. Let $i \ne j$, let $t \ne 0$, and let $T_{ij}(t) = I_n + t E_{ij}$ be a [[transvection|0NMN00FNW1]].
12. Let $S_t$ be the diagonal matrix with $t$ at position $i$ and $1$ elsewhere.
    Since $S_t E_{ij} S_t^{-1} = t E_{ij}$, we get $S_t T_{ij}(1) S_t^{-1} = T_{ij}(t)$.
13. By steps 8 and 7, $c(S_t) c(S_t^{-1}) = c(I_n) = 1$, so
$$c(T_{ij}(t)) = c(S_t) \, c(T_{ij}(1)) \, c(S_t^{-1}) = c(T_{ij}(1)).$$
14. Since $E_{ij}^2 = 0$ for $i \ne j$, we have $T_{ij}(1)^2 = I_n + 2 E_{ij} = T_{ij}(2)$.
15. By steps 8 and 13, $c(T_{ij}(1))^2 = c(T_{ij}(2)) = c(T_{ij}(1))$.
    Since $c(T_{ij}(1)) > 0$, it equals $1$.
16. So $c(T_{ij}(t)) = 1$ for every $t \ne 0$, and $\det T_{ij}(t) = 1$ by the triangular rule, so $c = \lvert \det \rvert$ on transvections.

*The invertible case.*

17. By the [[generation theorem|YSS4XNY9RC]], $A = T_1 \cdots T_k \, D$ with transvections $T_1, \dots, T_k$ and $D = \operatorname{diag}(1, \dots, 1, \det A)$.
18. By step 8, $c(A) = c(T_1) \cdots c(T_k) \, c(D)$.
    By steps 16 and 10 this is $\lvert \det A \rvert$, which proves part 1 for invertible $A$.

*The singular case.*

19. Now let $A$ be singular.
    Then $\det A = 0$ by the [[invertibility criterion|03Q7RE2HXR]].
20. The image $W = A(\mathbb{R}^n)$ is a subspace of dimension $r < n$.
21. [[Extend|0M4SXE5WW3]] a basis $w_1, \dots, w_r$ of $W$ to a basis $w_1, \dots, w_n$ of $\mathbb{R}^n$, and let $P$ be the invertible matrix with these columns.
22. Let $H = \{ x \in \mathbb{R}^n : x_n = 0 \}$.
    Then $P(H)$ is the span of $w_1, \dots, w_{n-1}$, and it contains $W$ because $r \le n - 1$.
23. The set $H$ is the union of the boxes $[-k, k]^{n-1} \times [0, 0]$ for $k \ge 1$, each of volume $0$, so $\lambda(H) = 0$.
24. By the invertible case applied to $P$, $\lambda(P(H)) = \lvert \det P \rvert \cdot 0 = 0$.
25. So $A(S) \subseteq W \subseteq P(H)$ lies in a null set.
    Lebesgue measure is complete, so $A(S)$ is measurable and $\lambda(A(S)) = 0$.
26. This equals $\lvert \det A \rvert \, \lambda(S) = 0 \cdot \lambda(S) = 0$, with $0 \cdot \infty = 0$, which proves part 1 for singular $A$.

*The parallelotope.*

27. The parallelotope of the columns is $P_A = A(Q)$, and $Q$ is a Borel set with $\lambda(Q) = 1$.
    So part 1 gives $\lambda(P_A) = \lvert \det A \rvert$, which is part 2.

## Idea

The measure $S \mapsto \lambda(A(S))$ is again invariant under translations, so it is Lebesgue measure times a constant $c(A)$.
That constant is multiplicative in $A$.
On a diagonal matrix it is the product of the absolute values of the diagonal entries, and on a shear it is $1$, because a shear is conjugate to its own square.
Diagonal matrices and shears generate the invertible matrices, so $c(A) = \lvert \det A \rvert$ everywhere.
A singular matrix squeezes all of space into a hyperplane, which has volume $0$.

## Variants

A proof without Haar measure checks the formula on boxes for each type of elementary matrix, and then extends it from boxes to all Borel sets.
For a shear, the image of a box has the same volume by [[Fubini's theorem|0R0T1VWH5X]], since each slice of the box is only translated.
Another route writes $A = UR$ with $U$ orthogonal and $R$ upper triangular, the QR factorization.
An orthogonal map sends balls to balls of the same radius, so its constant is $1$, and the constant of $R$ is the absolute product of its diagonal entries, as in steps 9 to 16.
