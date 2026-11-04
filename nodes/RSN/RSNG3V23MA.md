---
tag: RSNG3V23MA
kind: proof
name: Proof of the Cayley–Hamilton theorem for linear maps
msc: [15A04, 15A18]
proves: 0QEM68Y0DE
uses: [0BZ81AJNWF, 0BNEXSKNRV, 0YYMY95FWS, 05Q1B7MH0M, 059THXBRBB, 0F765KFC2J]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley–Hamilton_theorem
    locator: lead section
---

## Proof

We reduce the statement to the Cayley–Hamilton theorem for matrices.

1. If $V = 0$, then every endomorphism of $V$ is the zero map, so $p_T(T) = 0$. From now on let $n = \dim V \ge 1$.
2. Choose a basis $B = (b_1, \dots, b_n)$ of $V$. For an endomorphism $S$ of $V$, let $[S]_B$ be its [[matrix in $B$|0YYMY95FWS]]. Let $M = [T]_B$.
3. Column $j$ of $[S]_B$ is the coordinate vector $[S(b_j)]_B$. The coordinate map is linear by the [[isomorphism with the coordinate space|059THXBRBB]]. So $[S + S']_B = [S]_B + [S']_B$ and $[c S]_B = c [S]_B$ for $c \in F$.
4. By the [[matrix of a composition|05Q1B7MH0M]], $[S \circ S']_B = [S]_B [S']_B$. Also $[\id_V]_B = I_n$, since $\id_V(b_j) = b_j$.
5. By step 4 and induction on $k$, $[T^k]_B = M^k$ for all $k \ge 0$.
6. Let $p(x) = \sum_k c_k x^k \in F[x]$. By the definition of the [[value at $T$|0BNEXSKNRV]] and steps 3 and 5, $[p(T)]_B = \sum_k c_k M^k = p(M)$.
7. By the [[definition of $p_T$|0BZ81AJNWF]], $p_T = p_M$, the characteristic polynomial of $M$.
8. By the [[Cayley–Hamilton theorem for matrices|0F765KFC2J]], applied over the field $F$, $p_M(M) = 0$.
9. By steps 6, 7 and 8, $[p_T(T)]_B = p_M(M) = 0$.
10. So every column of $[p_T(T)]_B$ is zero, that is, $p_T(T)(b_j) = 0$ for each $j$.
11. A linear map that vanishes on a basis vanishes on every linear combination of it. Hence $p_T(T) = 0$.

## Idea

Choosing a basis turns endomorphisms into matrices, and this translation respects sums, scalar multiples and composition. So it sends $p(T)$ to $p(M)$ for every polynomial $p$. The matrix theorem says $p_M(M) = 0$, and a map with zero matrix is zero.
