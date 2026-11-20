---
tag: 8N4EE2QJ8P
kind: proof
name: Proof of the theorem on the characteristic polynomial of an endomorphism
msc: ["15A04", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: C98TZ6ZAXC
methods: [0NTF6DMVAP, 41JZ39GE3F]
uses: [0TYMASG33Y, 0MQXVZEBMT, 0J9TVTNB4K, 0M4SXE5WW3, 0YYMY95FWS, 039HF58KQ5, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Proof

Part 1.

1. Let $P$ be the change of basis matrix from $C$ to $B$. By the [[change of basis formula|0MQXVZEBMT]], $[T]_C = P^{-1} [T]_B P$, and $P$ is invertible.
2. By the theorem that the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]], $p_{P^{-1} [T]_B P} = p_{[T]_B}$.
3. So $p_{[T]_C} = p_{[T]_B}$, and $p_T$ is well defined.
4. $p_T$ is monic of degree $n$, because $[T]_B$ is $n \times n$ and the [[characteristic polynomial|039HF58KQ5]] of an $n \times n$ matrix is monic of degree $n$.

Part 2.
Let $A$ be $m \times m$ and $D$ be $k \times k$.

5. In the ring $K[t]$, $t I_{m+k} - M = \begin{pmatrix} t I_m - A & -B \\ 0 & t I_k - D \end{pmatrix}$, by the definition of $tI - M$ entry by entry.
6. This is a block upper triangular matrix over the commutative ring $K[t]$, the [[polynomial ring|0Q9EZS90GY]].
7. The theorem on [[block triangular determinants|0J9TVTNB4K]] holds over every commutative ring. Applied over $K[t]$, it gives $\det(t I - M) = \det(t I_m - A) \cdot \det(t I_k - D)$.
8. So $p_M = p_A \cdot p_D$.

Part 3.
Let $m = \dim U$, so $1 \le m < n$.

9. Choose a basis $u_1, \dots, u_m$ of $U$. It is independent in $V$, so it [[extends to a basis|0M4SXE5WW3]] $B = (u_1, \dots, u_m, w_1, \dots, w_k)$ of $V$, with $k = n - m \ge 1$.
10. For $j \le m$, $T(u_j) \in U$, because $U$ is $T$-invariant. So $T(u_j)$ is a combination of $u_1, \dots, u_m$ alone.
11. By the definition of the [[matrix of a linear map|0YYMY95FWS]], column $j$ of $[T]_B$ holds the coordinates of $T(u_j)$. By step 10, its last $k$ entries are $0$ for $j \le m$.
12. So $[T]_B = \begin{pmatrix} A & B' \\ 0 & D \end{pmatrix}$, where $A$ is the $m \times m$ matrix of the coordinates of $T(u_j)$ in $u_1, \dots, u_m$.
13. By step 10, $A$ is the matrix of $T|_U$ in the basis $u_1, \dots, u_m$. So $p_A = p_{T|_U}$, by part 1 for $T|_U$.
14. By part 2 over $K = F$, $p_T = p_{[T]_B} = p_{T|_U} \cdot p_D$. So $p_{T|_U}$ divides $p_T$.

Part 4.

15. Choose a basis $u_1, \dots, u_m$ of $U$ and a basis $w_1, \dots, w_k$ of $W$. Together they form a basis $B$ of $V$, because $V = U \oplus W$.
16. As in steps 10 to 12, $T(u_j) \in U$ gives the zero block below $A = [T|_U]$.
17. Also $T(w_j) \in W$, because $W$ is $T$-invariant. So the coordinates of $T(w_j)$ on $u_1, \dots, u_m$ are $0$, and $B' = 0$.
18. The same reasoning as in step 13 shows that $D$ is the matrix of $T|_W$ in the basis $w_1, \dots, w_k$.
19. By part 2, $p_T = p_A \cdot p_D = p_{T|_U} \cdot p_{T|_W}$.

## Idea

Choose a basis adapted to the invariant subspace.
Then the matrix of $T$ is block triangular, and the determinant of $tI - [T]$ splits as a product.
The key point is that the block determinant rule holds over the polynomial ring $K[t]$, not only over a field.

## Variants

- Part 1 can also be proved without matrices, by defining $p_T$ as the determinant of $t - T$ on $F[t] \otimes_F V$.
- Part 2 can be proved from the Leibniz formula: a permutation that sends an index of the second block into the first block meets a zero entry.
