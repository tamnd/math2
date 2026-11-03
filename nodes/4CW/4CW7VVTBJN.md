---
tag: 4CW7VVTBJN
kind: definition
name: Operator K-theory
msc: [46L80, 19K99]
defines: DQZ8S67ZE6
uses: [M2WFY1D3SZ, 5FDMY7PDYY, 7SB03M850M]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Definition

Let $A$ be a unital [[C*-algebra|M2WFY1D3SZ]], and let $M_n(A)$ be the C*-algebra of $n \times n$ matrices over $A$.
Embed $M_n(A)$ in $M_{n+1}(A)$ by $a \mapsto \begin{pmatrix} a & 0 \\ 0 & 0 \end{pmatrix}$ and let $M_\infty(A) = \bigcup_n M_n(A)$.

1. A *projection* is an element $p$ with $p = p^2 = p^*$.
Two projections $p, q \in M_\infty(A)$ are *Murray–von Neumann equivalent* if $p = v^* v$ and $q = v v^*$ for some $v \in M_\infty(A)$.
The classes form a commutative monoid under $[p] + [q] = [\operatorname{diag}(p, q)]$, and $K_0(A)$ is its [[Grothendieck group|5FDMY7PDYY]].
2. Let $U_n(A)$ be the group of unitaries of $M_n(A)$, embedded in $U_{n+1}(A)$ by $u \mapsto \operatorname{diag}(u, 1)$, and let $U_\infty(A) = \bigcup_n U_n(A)$.
Then $K_1(A)$ is the group of classes of $U_\infty(A)$.
Here $u$ and $w$ in $U_n(A)$ are identified when they are joined by a continuous path in $U_m(A)$ for some $m \ge n$.
3. If $A$ is not unital, let $\tilde{A}$ be its [[unitization|7SB03M850M]]; then $K_0(A)$ is the kernel of the map $K_0(\tilde{A}) \to K_0(\C)$ induced by $\tilde{A} \to \C$, and $K_1(A) = K_1(\tilde{A})$.

*Operator K-theory* is the pair of functors $A \mapsto K_0(A)$ and $A \mapsto K_1(A)$.

## Remarks

The group $K_1(A)$ is abelian, since $\operatorname{diag}(uw, 1)$ is joined by a path of unitaries to $\operatorname{diag}(u, w)$ and to $\operatorname{diag}(wu, 1)$.
For the suspension $SA = C_0(\R, A)$ one has $K_1(A) \cong K_0(SA)$, and Bott periodicity in this setting says $K_0(A) \cong K_1(SA)$.

Example: $A = \C$.
A projection in $M_n(\C)$ is the orthogonal projection onto a subspace, and two projections are equivalent exactly when the subspaces have the same dimension.
So the monoid is $\N$ and $K_0(\C) \cong \Z$.
Each unitary group $U_n(\C)$ is path-connected, so $K_1(\C) = 0$.

Non-example: projections in $A$ itself are not enough in general.
In $A = C(S^2)$ the only projections are $0$ and $1$, since $S^2$ is connected; but $K_0(C(S^2)) \cong \Z \oplus \Z$, and the extra generator comes from a projection in $M_2(C(S^2))$.

For a compact Hausdorff space $X$, the [[Serre–Swan theorem|B31RNWHHAY]] gives $K_0(C(X)) \cong K^0(X)$.
