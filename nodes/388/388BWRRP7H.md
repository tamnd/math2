---
tag: 388BWRRP7H
kind: proof
name: Proof of the classification of alternating bilinear forms
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
proves: V8KKHKXXB3
methods: [0ASJVEFA9J, 01XM7JEKHY]
uses: [08ZQAKBKHF, SX9CD5NEPD, M2JH84VEY9, 3ND2FNJ38Y, 0P24YW565F, 0SPYAGE7T0, D3E2Y85S6H, NZJDNC6EP6, 0KAN330PAH]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Standard symplectic space
  - book: isbn:9780387728285
    locator: Chapter 11
  - book: isbn:9780135367971
    locator: Chapter 10
---

## Proof

We split off one plane with the matrix $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, apply induction to its orthogonal complement, and then read parts 3 to 6 from the block matrix.

Parts 1 and 2, by induction on $n = \dim V$.

1. If $B = 0$, which includes the case $n = 0$, we take $m = 0$ and any basis $(w_1, \dots, w_n)$. Every pair of basis vectors gives $0$, and the matrix is $0_n$.
2. Let $B \neq 0$, and pick $u, z \in V$ with $B(u, z) \neq 0$. Put $u_1 = u$ and $v_1 = z / B(u, z)$. Then $B(u_1, v_1) = 1$, by linearity in the second slot.
3. An [[alternating form|08ZQAKBKHF]] is skew-symmetric in every characteristic, by the [[relation between alternating and skew-symmetric forms|SX9CD5NEPD]]. So $B(v_1, u_1) = -1$. Also $B(u_1, u_1) = B(v_1, v_1) = 0$, because $B$ is alternating.
4. The vectors $u_1, v_1$ are independent. If $v_1 = c u_1$, then $B(u_1, v_1) = c B(u_1, u_1) = 0$, which contradicts $B(u_1, v_1) = 1$; and $u_1 \neq 0$, since $B(u_1, v_1) \neq 0$.
5. So $H = \operatorname{span}(u_1, v_1)$ has dimension $2$, and by step 3 the matrix of $B$ on $H$ in the basis $(u_1, v_1)$ is $J$.
6. Since $\det J = 1 \neq 0$, the restriction of $B$ to $H$ is nondegenerate, by the [[criteria for nondegeneracy|3ND2FNJ38Y]].
7. By part 3 of the [[dimension statement for orthogonal complements|M2JH84VEY9]], $V = H \oplus H^\perp$ and $\dim H^\perp = n - 2$, where $H^\perp = \{ y : B(x, y) = 0 \text{ for all } x \in H \}$.
8. The restriction of $B$ to $H^\perp$ is alternating. By the induction hypothesis, $H^\perp$ has a basis $(u_2, v_2, \dots, u_m, v_m, w_1, \dots, w_k)$ with the properties of part 1.
9. For $x \in H$ and $y \in H^\perp$ we have $B(x, y) = 0$ by the definition of $H^\perp$, and $B(y, x) = -B(x, y) = 0$ by skew-symmetry.
10. Since $V = H \oplus H^\perp$, the list $(u_1, v_1, u_2, v_2, \dots, w_k)$ is a basis of $V$. By steps 3, 8 and 9 it has the properties of part 1.
11. In this basis the [[matrix|0P24YW565F]] has one block $J$ for each pair $(u_i, v_i)$ and zeros elsewhere, which is part 2.

Part 3.

12. The matrix $J \oplus \dots \oplus J \oplus 0_k$ has exactly $2m$ nonzero rows, and they are independent, because each has its single nonzero entry in a different column. So its rank is $2m$.
13. The rank of a form does not depend on the basis, by the [[change of basis rule|0SPYAGE7T0]]. So $\operatorname{rank} B = 2m$, which is even.
14. Each $w_j$ pairs to zero with every basis vector, so it lies in the radical. The radical has dimension $n - \operatorname{rank} B = k$, by the criteria for nondegeneracy, so $(w_1, \dots, w_k)$ is a basis of it.

Part 4.

15. Let $A$ be an alternating $n \times n$ matrix of rank $2m$. The form $x^{\mathsf{T}} A y$ on $F^n$ is alternating, by the matrix criterion in the relation between the two notions.
16. Parts 2 and 3 give an invertible $P$, whose columns are the new basis, with $P^{\mathsf{T}} A P = S$, where $S = J \oplus \dots \oplus J \oplus 0$ has $m$ blocks. So $A$ is [[congruent|NZJDNC6EP6]] to $S$.
17. Two alternating matrices of the same rank $2m$ are congruent to the same $S$. [[Congruence is an equivalence relation|D3E2Y85S6H]], so they are congruent to each other.
18. Conversely, congruent matrices have the same rank, by the same statement on congruence.

Part 5.

19. If $B$ is [[nondegenerate|0KAN330PAH]], then $\operatorname{rank} B = n$, by the criteria for nondegeneracy. By part 3, $n = 2m$ is even.

Part 6.

20. Let $A$ be alternating with $P^{\mathsf{T}} A P = S$ as in step 16. The product rule for determinants gives $\det S = (\det P)^2 \det A$.
21. If $\operatorname{rank} A < n$, then $\det A = 0 = 0^2$.
22. If $\operatorname{rank} A = n$, then $S = J \oplus \dots \oplus J$ and $\det S = (\det J)^m = 1$. So $\det A = (\det P)^{-2} = \bigl( (\det P)^{-1} \bigr)^2$, a square. This proves all six parts. $\blacksquare$

## Idea

A nonzero alternating form has a pair $u, v$ with $B(u, v) = 1$.
On the plane of this pair the matrix is $J$, which is invertible, so the plane splits off together with its orthogonal complement.
The form on the complement is again alternating, and induction finishes the basis.
Then the block shape of the matrix shows the rank, the radical and the determinant at a glance.

## Variants

The same proof can be run as an algorithm on the matrix.
Use a nonzero entry $a_{ij}$ to clear row $i$, column $i$, row $j$ and column $j$ by symmetric row and column operations, move the pair to the top left, and repeat on the rest.
This is the alternating version of Gaussian elimination, and the [[example of a 4 by 4 matrix|C8S4RH68S0]] follows it.
A second proof of part 6 uses the [[Pfaffian|C9JJD2AVJR]] and the identity $\operatorname{pf}(A)^2 = \det A$.
