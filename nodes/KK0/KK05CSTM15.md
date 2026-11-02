---
tag: KK05CSTM15
kind: statement
role: theorem
name: Alexander duality
msc: [55M05]
uses: [NJQMWVK3QK, 6N7BC70CX0, T62369RFH6, 0TVJZYB6SH, 9VY90HJVZX]
about: [NJQMWVK3QK, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Alexander_duality
same_as:
  wikidata: Q4720484
  wikipedia: Alexander duality
---

## Statement

Let $n \ge 1$ and let $K$ be a nonempty, [[compact|0TVJZYB6SH]], locally contractible proper subspace of the [[sphere|T62369RFH6]] $S^n$.
Then for every integer $i$ there is an isomorphism
$$\tilde H_i(S^n \setminus K; \Z) \cong \tilde H^{\,n-i-1}(K; \Z),$$
where $\tilde H_i$ is [[reduced homology|NJQMWVK3QK]] and $\tilde H^{\,j}$ is reduced [[singular cohomology|6N7BC70CX0]].

## Remarks

The proof uses a duality between the cohomology of a compact subset of a manifold and the homology of the manifold relative to its complement.
This duality is proved like [[Poincaré duality|9VY90HJVZX]].
The long exact sequence of the pair $(S^n, S^n \setminus K)$ then gives the result.
For an arbitrary compact $K$, the statement still holds with Čech cohomology in place of singular cohomology.
With singular cohomology, local contractibility cannot be dropped: the Warsaw circle in $S^2$ has the singular cohomology of a point but separates $S^2$ into two components.

Example: if $K \subset S^n$ is homeomorphic to $S^{n-1}$, then $\tilde H_0(S^n \setminus K) \cong \tilde H^{\,n-1}(S^{n-1}) \cong \Z$.
So the complement has exactly two path components, which is the Jordan–Brouwer separation theorem.

Example: for a knot $K \subset S^3$, that is, a subspace homeomorphic to $S^1$, $H_1(S^3 \setminus K) \cong \tilde H^1(S^1) \cong \Z$, whatever the knot is.

## Explanations

### L1 human

The holes in the complement of a shape in a sphere are determined by the holes of the shape itself, with dimensions flipped.
A circle drawn on the $2$-sphere cuts it into two pieces.
A knotted circle in $3$-space always has a complement with exactly one independent loop around it, however complicated the knot.

### L2 human

Alexander duality computes the homology of complements of embedded subsets, such as knot complements and complements of embedded spheres.
It gives a quick proof of the Jordan–Brouwer separation theorem in all dimensions.
Its proof is a direct application of the duality theory of manifolds, and its Čech version is a standard reason to introduce Čech cohomology.
