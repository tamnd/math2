---
tag: RSNG3V23MA
kind: proof
name: Proof of the Cayley-Hamilton theorem for linear maps
msc: ["15A04", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0QEM68Y0DE
methods: [DX2H7AD66G, 0NTF6DMVAP]
uses: [0BZ81AJNWF, 0BNEXSKNRV, 0YYMY95FWS, 05Q1B7MH0M, 059THXBRBB, 0F765KFC2J]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: lead section
---

## Proof

We choose a basis, check that taking matrices turns $p(T)$ into $p(M)$, and then apply the Cayley-Hamilton theorem for matrices.

1. If $V = 0$, then every endomorphism of $V$ is the zero map, so $p_T(T) = 0$.
   From now on let $n = \dim V \ge 1$.
2. Choose a basis $B = (b_1, \dots, b_n)$ of $V$.
   For an endomorphism $S$ of $V$ let $[S]_B$ be its [[matrix in the basis B|0YYMY95FWS]], and put $M = [T]_B$.
3. Column $j$ of $[S]_B$ is the coordinate vector of $S(b_j)$, and taking coordinates is linear by the [[isomorphism with the coordinate space|059THXBRBB]].
   So $[S + S']_B = [S]_B + [S']_B$ and $[c S]_B = c [S]_B$ for every $c \in F$.
4. By the rule for the [[matrix of a composition|05Q1B7MH0M]], $[S \circ S']_B = [S]_B [S']_B$.
   Also $[\mathrm{id}_V]_B = I_n$, since $\mathrm{id}_V(b_j) = b_j$ for each $j$.
5. By step 4 and induction on $k$, $[T^k]_B = M^k$ for every $k \ge 0$.
6. Let $p(x) = \sum_k c_k x^k \in F[x]$.
   By the definition of the [[value of a polynomial at an endomorphism|0BNEXSKNRV]] and steps 3 and 5,
$$[p(T)]_B = \sum_k c_k M^k = p(M).$$
7. By the [[definition of the characteristic polynomial of a linear map|0BZ81AJNWF]], $p_T = p_M$.
8. The [[Cayley-Hamilton theorem for matrices|0F765KFC2J]], applied over the field $F$, gives $p_M(M) = 0$.
9. By steps 6, 7 and 8, $[p_T(T)]_B = p_M(M) = 0$.
10. So every column of $[p_T(T)]_B$ is zero, which means $p_T(T)(b_j) = 0$ for each $j$.
11. A linear map that vanishes on a basis vanishes on every linear combination of the basis vectors, and so on all of $V$.
    Hence $p_T(T) = 0$.

## Idea

A basis turns endomorphisms into matrices, and this translation respects sums, scalar multiples and composition.
So it sends $p(T)$ to $p(M)$ for every polynomial $p$, and the characteristic polynomial of $T$ is that of $M$ by definition.
The matrix theorem says $p_M(M) = 0$, and a map with zero matrix is the zero map.
The only care needed is step 7: the definition of $p_T$ does not depend on the basis, because similar matrices have the same characteristic polynomial.

## Variants

One can avoid the reduction by proving the theorem for $T$ directly.
Over an algebraically closed field, choose a basis in which $T$ is upper triangular and use the chain of invariant subspaces, as in the triangular proof of the [[matrix theorem|0F765KFC2J]].
Another direct route proves $p_T(T) v = 0$ one vector at a time.
The span $W$ of $v, Tv, T^2 v, \dots$ is invariant, and in the basis $v, Tv, \dots, T^{k-1} v$ the restriction of $T$ has a companion matrix.
The characteristic polynomial $q$ of that companion matrix satisfies $q(T) v = 0$, and $q$ divides $p_T$ because $T$ is block triangular in a basis of $V$ that extends this basis of $W$.
