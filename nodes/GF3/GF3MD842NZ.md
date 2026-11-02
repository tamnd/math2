---
tag: GF3MD842NZ
kind: definition
name: Approximately finite-dimensional C*-algebra
msc: [46L05, 46L35]
defines: 4Y7VENNBVK
uses: [0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Approximately_finite-dimensional_C*-algebra
---

## Definition

Let $A$ be a C*-algebra.
Then $A$ is *approximately finite-dimensional*, or *AF*, if it has finite-dimensional C\*-subalgebras $A_1 \subseteq A_2 \subseteq \cdots$ whose union is dense in $A$.
Equivalently, $A$ is isomorphic to the C\*-algebraic [[direct limit|7SXKJG1Q9B]] of a sequence $A_1 \to A_2 \to \cdots$ of finite-dimensional C\*-algebras and $*$-homomorphisms.

## Remarks

Every finite-dimensional C\*-algebra is isomorphic to a direct sum $M_{n_1}(\C) \oplus \cdots \oplus M_{n_k}(\C)$ of [[matrix rings|0FHVPRAE60]].
An AF algebra in this sense is separable.
Some authors call a nonseparable C\*-algebra AF when every finite subset can be approximated by elements of a finite-dimensional C\*-subalgebra.

Example: the compact operators $K(H)$ on a separable infinite-dimensional Hilbert space $H$ with orthonormal basis $(e_k)$.
Let $A_n$ be the operators that map $\operatorname{span}(e_1, \ldots, e_n)$ into itself and vanish on its orthogonal complement; then $A_n \cong M_n(\C)$ and $A_n \subseteq A_{n+1}$.
The union is dense because the finite-rank operators are dense in $K(H)$, and $P_n T P_n \to T$ for compact $T$, where $P_n$ is the projection onto the span.

Non-example: $C([0, 1])$ is not AF.
A finite-dimensional commutative C\*-algebra is spanned by projections, and the only projections in $C([0,1])$ are $0$ and $1$, since $[0,1]$ is connected.
So every finite-dimensional C\*-subalgebra lies in the constants $\C 1$, which are not dense.
