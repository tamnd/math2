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

We reduce part 1 to similar matrices, part 2 to the block rule for determinants over $K[t]$, and parts 3 and 4 to part 2 with a basis adapted to the invariant subspaces.

*Part 1.*

1. Let $P$ be the change of basis matrix from $C$ to $B$.
   By the [[change of basis formula|0MQXVZEBMT]], $[T]_C = P^{-1} [T]_B P$, and $P$ is invertible.
2. Similar matrices have the same characteristic polynomial, by the theorem that the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]].
   So $p_{[T]_C} = p_{[T]_B}$, and $p_T$ is well defined.
3. The matrix $[T]_B$ is $n \times n$, and the [[characteristic polynomial|039HF58KQ5]] of an $n \times n$ matrix is monic of degree $n$.
   So $p_T$ is monic of degree $n$.

*Part 2.* Let $A$ be $m \times m$ and let $D$ be $k \times k$.

4. Subtract $M$ from $t I_{m+k}$ entry by entry:
$$t I_{m+k} - M = \begin{pmatrix} t I_m - A & -B \\ 0 & t I_k - D \end{pmatrix}.$$
5. This is a block upper triangular matrix over the [[polynomial ring|0Q9EZS90GY]] $K[t]$, which is a commutative ring.
6. The rule for [[block triangular determinants|0J9TVTNB4K]] holds over every commutative ring, so over $K[t]$ it gives
$$\det(t I_{m+k} - M) = \det(t I_m - A) \det(t I_k - D).$$
   That is, $p_M = p_A \, p_D$.

*Part 3.* Let $m = \dim U$, so that $1 \le m < n$, and let $k = n - m$.

7. Choose a basis $u_1, \dots, u_m$ of $U$.
   It is independent in $V$, so it [[extends to a basis|0M4SXE5WW3]] $E = (u_1, \dots, u_m, w_1, \dots, w_k)$ of $V$.
8. For $j \le m$, the vector $T(u_j)$ lies in $U$, because $U$ is $T$-invariant.
   So $T(u_j)$ is a combination of $u_1, \dots, u_m$ alone.
9. Column $j$ of $[T]_E$ holds the coordinates of $T(u_j)$, by the definition of the [[matrix of a linear map|0YYMY95FWS]].
   By step 8, its last $k$ entries are $0$ for $j \le m$.
10. So $[T]_E = \begin{pmatrix} A & B' \\ 0 & D \end{pmatrix}$, where $A$ is $m \times m$ and holds the coordinates of $T(u_1), \dots, T(u_m)$ in $u_1, \dots, u_m$.
11. By step 8, $A$ is the matrix of $T|_U$ in the basis $u_1, \dots, u_m$, so $p_A = p_{T|_U}$ by part 1 for $T|_U$.
12. Part 2 with $K = F$ gives $p_T = p_{[T]_E} = p_{T|_U} \, p_D$.
    So $p_{T|_U}$ divides $p_T$.

*Part 4.*

13. Choose a basis $u_1, \dots, u_m$ of $U$ and a basis $w_1, \dots, w_k$ of $W$.
    Together they form a basis $E$ of $V$, because $V = U \oplus W$.
14. Steps 8 to 11 apply to $U$ without change, so $[T]_E$ has the form of step 10 with $A = [T|_U]$.
15. Each $T(w_j)$ lies in $W$, because $W$ is $T$-invariant.
    So its coordinates on $u_1, \dots, u_m$ are $0$, which means $B' = 0$.
16. Then $D$ holds the coordinates of $T(w_j)$ in $w_1, \dots, w_k$, so $D$ is the matrix of $T|_W$, and $p_D = p_{T|_W}$ by part 1.
17. Part 2 gives $p_T = p_A \, p_D = p_{T|_U} \, p_{T|_W}$.

## Idea

Everything comes from one picture.
Choose a basis that starts with a basis of the invariant subspace.
Then the matrix of $T$ has a zero block in the lower left corner, and the determinant of $tI - [T]$ splits as a product of two smaller determinants.
The one point to check is that the block rule for determinants holds over the polynomial ring $K[t]$, and it does, because that rule holds over every commutative ring.

## Variants

Part 1 can be proved without matrices, by defining $p_T$ as the determinant of $t - T$ on $F[t] \otimes_F V$, a definition that uses no basis.
Part 2 also follows from the Leibniz formula.
A permutation that sends some index of the second block to a column of the first block picks an entry of the zero block, so its term is $0$.
The permutations that survive keep each block, and each of them splits into a permutation of the first block and a permutation of the second.
