---
tag: X8BWXFGK53
kind: statement
role: theorem
name: Mayer–Vietoris sequence
msc: [55N10, 55U15]
uses: [0CQHFPGJ45, 0RZH6W98HK, M0Q5CFJ7ZH, JB7ZBFBA9C]
about: [M0Q5CFJ7ZH]
sources:
  - url: https://en.wikipedia.org/wiki/Mayer%E2%80%93Vietoris_sequence
same_as:
  wikidata: Q2421905
  wikipedia: Mayer–Vietoris sequence
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $A, B \subseteq X$ be subspaces whose [[interiors|0RZH6W98HK]] cover $X$.
Let $H_n$ denote [[singular homology|M0Q5CFJ7ZH]] with coefficients in an abelian group.
Then there are homomorphisms $\partial \colon H_n(X) \to H_{n-1}(A \cap B)$ such that the sequence
$$\cdots \to H_n(A \cap B) \xrightarrow{\Phi} H_n(A) \oplus H_n(B) \xrightarrow{\Psi} H_n(X) \xrightarrow{\partial} H_{n-1}(A \cap B) \to \cdots \to H_0(X) \to 0$$
is [[exact|JB7ZBFBA9C]], where $\Phi(x) = (i_* x, -j_* x)$ and $\Psi(y, z) = k_* y + l_* z$ for the inclusions $i \colon A \cap B \to A$, $j \colon A \cap B \to B$, $k \colon A \to X$ and $l \colon B \to X$.

## Remarks

Let $C_\bullet^{A+B}(X)$ be the complex of singular chains that are sums of simplices lying in $A$ or in $B$.
There is a short exact sequence of chain complexes $0 \to C_\bullet(A \cap B) \to C_\bullet(A) \oplus C_\bullet(B) \to C_\bullet^{A+B}(X) \to 0$.
Its long exact sequence in homology is the Mayer–Vietoris sequence, once one knows that the inclusion $C_\bullet^{A+B}(X) \to C_\bullet(X)$ induces isomorphisms in homology.
This last fact uses barycentric subdivision and needs the interiors of $A$ and $B$ to cover $X$.
Without this hypothesis the sequence can fail.
Take $X = [0, 1]$, $A = [0, 1/2]$ and $B = (1/2, 1]$, so that $A \cap B = \emptyset$.
Exactness at $H_0(A) \oplus H_0(B)$ would make the map $\Z^2 \to \Z = H_0(X)$ injective, which is false.
Example: write the sphere $S^n$, $n \ge 1$, as the union of two open caps, each contractible, whose intersection deformation retracts to $S^{n-1}$.
The sequence in reduced homology gives $\tilde H_k(S^n) \cong \tilde H_{k-1}(S^{n-1})$, hence $H_n(S^n; \Z) \cong \Z$.
There is a reduced version when $A \cap B \neq \emptyset$, and a dual version for singular cohomology with the arrows reversed.

## Explanations

### L1 human

If a space is glued from two pieces, its homology can be computed from the homology of the pieces and of their overlap.
The Mayer–Vietoris sequence is the exact rule for this computation.
Holes in the whole space come either from holes in the pieces or from the overlap.
If the overlap has several parts, or holes that get filled in the pieces, these create a new hole one dimension higher in the whole space.
For example, a circle is two arcs overlapping in two small arcs, and the two components of the overlap produce the loop of the circle.

### L2 human

It is the main computational tool of basic algebraic topology.
It is the analogue for open covers of the long exact sequence of a pair, and it can also be derived from that sequence by excision.
It gives the homology of spheres, of wedge sums and of connected sums, and it is the inductive step in proofs about manifolds, such as Poincaré duality.
The same pattern appears for de Rham cohomology, for sheaf cohomology and in any cohomology theory satisfying the Eilenberg–Steenrod axioms.
