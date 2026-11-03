---
tag: TGGDV86S17
kind: definition
name: K0 of a C*-algebra
msc: [46L80, 19K14]
defines: BP86XQRZD2
uses: [M2WFY1D3SZ, GT9S7APKG1, 5FDMY7PDYY]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Definition

Let $A$ be a unital [[C*-algebra|M2WFY1D3SZ]].
For $n \ge 1$, let $P_n(A)$ be the set of projections $p = p^* = p^2$ in the matrix algebra $M_n(A)$, and let $P_\infty(A)$ be the disjoint union of the $P_n(A)$.
For $p \in P_n(A)$ and $q \in P_m(A)$, write $p \sim_0 q$ if there is $v \in M_{m,n}(A)$ with $v^* v = p$ and $v v^* = q$; this is [[Murray–von Neumann equivalence|GT9S7APKG1]].
Let $p \oplus q$ be the block diagonal matrix $\operatorname{diag}(p, q) \in P_{n+m}(A)$.
The set $D(A) = P_\infty(A)/\sim_0$ is a commutative monoid under $[p] + [q] = [p \oplus q]$, with neutral element the class of the zero projection.
The group $K_0(A)$ is the [[Grothendieck group|5FDMY7PDYY]] of the monoid $D(A)$.

If $A$ is not unital, let $\widetilde{A}$ be its unitization and $\pi \colon \widetilde{A} \to \C$ the quotient map with kernel $A$.
Then $K_0(A)$ is the kernel of the induced map $\pi_* \colon K_0(\widetilde{A}) \to K_0(\C)$.

## Remarks

Every element of $K_0(A)$, for $A$ unital, has the form $[p] - [q]$ with $p, q \in P_\infty(A)$.
Example: for $A = M_k(\C)$, two projections are equivalent exactly when they have the same rank, so $D(A) \cong \N$ and $K_0(A) \cong \Z$, with $[p] \mapsto \operatorname{rank} p$.
Non-example of the monoid being cancellative: in $B(H)$ with $H$ infinite-dimensional and separable, $[1] + [1] = [1]$, so $K_0(B(H)) = 0$ although $D(B(H))$ is not zero.
Other standard values are $K_0(\mathcal{K}) \cong \Z$ for the compact operators $\mathcal{K}$ and $K_0(C(X)) \cong K^0(X)$ for compact Hausdorff $X$.
A $*$-homomorphism $\varphi \colon A \to B$ induces a group homomorphism $\varphi_* \colon K_0(A) \to K_0(B)$, so $K_0$ is a functor.
