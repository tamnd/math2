---
tag: DHR34DAPNQ
kind: statement
role: theorem
name: Families index theorem
msc: [58J20, 19K56, 19L64]
uses: [QK2ECEQYA5, H353HJA3E5, CX4M8K61AB, MT9P2X85V8, F31T650DKY, 9E4JE4902G, JBX99NRRB6, 6XRTXBPASW]
about: [MT9P2X85V8, 9E4JE4902G]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Statement

Let $B$ be a compact Hausdorff space.
Let $\pi \colon Z \to B$ be a [[fibre bundle|CX4M8K61AB]] whose fibre is a closed smooth manifold $M$, with structure group the diffeomorphism group of $M$.
Write $Z_b = \pi^{-1}(b)$, and let $T_v Z$ be the vertical tangent bundle, made of the tangent spaces of the fibres.
Let $E, F$ be complex vector bundles over $Z$, and let $P = (P_b)_{b \in B}$ be a continuous family of [[elliptic differential operators|MT9P2X85V8]] $P_b \colon C^\infty(Z_b; E) \to C^\infty(Z_b; F)$.

1. The family has an analytic index $\operatorname{ind} P \in K(B)$, the [[index bundle|H353HJA3E5]] of the family of Fredholm operators obtained from $P$.
When $\dim \ker P_b$ is constant, it equals $[\ker P] - [\operatorname{coker} P]$.
2. The [[principal symbols|F31T650DKY]] define a class $[\sigma(P)] \in K_c(T_v^* Z)$.
A fibrewise topological index gives a homomorphism $\operatorname{t-ind} \colon K_c(T_v^* Z) \to K(B)$.
It is built from an embedding of $Z$ into $B \times \R^N$ over $B$ and the [[Thom isomorphism in K-theory|JBX99NRRB6]].
3. The theorem states that $\operatorname{ind} P = \operatorname{t-ind}[\sigma(P)]$ in $K(B)$, where $K$ is [[complex K-theory|9E4JE4902G]].

## Remarks

The proof follows the K-theoretic proof of the [[Atiyah–Singer index theorem|QK2ECEQYA5]], carried out over the base $B$.
Both indices are homomorphisms with the same formal properties, and they agree for the basic families on vector bundles over $B$.
For $B$ a point it is the Atiyah–Singer index theorem, since $K(\text{point}) = \Z$.

Taking [[Chern characters|6XRTXBPASW]] gives a cohomological form: $\operatorname{ch}(\operatorname{ind} P)$ is obtained, up to a sign fixed by orientation conventions, by integrating $\operatorname{ch}[\sigma(P)]$ times the Todd class of $T_v Z \otimes \C$ over the fibres.
The index bundle carries more information than the numerical index.
Its rank is the numerical index of each $P_b$, and its Chern classes record how the kernels and cokernels twist over $B$.

Example: let $Q \colon C^\infty(M; E_0) \to C^\infty(M; F_0)$ be one elliptic operator on $M$ and let $V \to B$ be a complex vector bundle.
On $Z = B \times M$ take $P_b = Q \otimes \id_{V_b}$.
Then $\ker P_b = \ker Q \otimes V_b$ and $\operatorname{coker} P_b = \operatorname{coker} Q \otimes V_b$, so $\operatorname{ind} P = (\operatorname{ind} Q)\,[V] \in K(B)$, an integer multiple of $[V]$.

## Explanations

### L1 human

Instead of one elliptic operator, consider a family of them depending continuously on a parameter in a space $B$.
The solutions of each operator form a vector space whose dimension may jump, but the formal difference of kernels and cokernels forms a K-theory class over $B$.
The theorem computes this class from topology, just as the Atiyah–Singer theorem computes the index of a single operator.

### L2 human

The families index theorem is used to compute determinant line bundles and their curvature, which is important in gauge theory and string theory.
It is also the starting point for index theorems with values in the K-theory of C*-algebras, as in the work of Mishchenko and Fomenko on higher signatures.
Its real version, with values in real K-theory, gives mod $2$ invariants of families such as those used in the study of spin manifolds.
