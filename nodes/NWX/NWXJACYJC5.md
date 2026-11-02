---
tag: NWXJACYJC5
kind: statement
role: theorem
name: Lefschetz duality
msc: [55M05, 57N65]
uses: [7DS6B2BFK8, 913WEQERBE, ZEA0PEM3B2, N7SXBQ7WK0, 4BVWH0BN28, 6N7BC70CX0, 9VY90HJVZX]
about: [6N7BC70CX0, 4BVWH0BN28]
sources:
  - url: https://en.wikipedia.org/wiki/Lefschetz_duality
same_as:
  wikidata: Q6516730
  wikipedia: Lefschetz duality
---

## Statement

Let $M$ be a compact [[manifold with boundary|7DS6B2BFK8]] of dimension $n$ with boundary $\partial M$, and let $R$ be a commutative ring with $1$.
Assume that the interior of $M$ is $R$-[[oriented|913WEQERBE]], and let $[M] \in H_n(M, \partial M; R)$ be the corresponding relative [[fundamental class|ZEA0PEM3B2]].
Let $H^k$ be [[singular cohomology|6N7BC70CX0]], and use [[relative homology|4BVWH0BN28]] and relative cohomology for the pair $(M, \partial M)$.
Then for every $k$, the [[cap product|N7SXBQ7WK0]] with $[M]$ gives isomorphisms
$$H^k(M; R) \to H_{n-k}(M, \partial M; R) \qquad\text{and}\qquad H^k(M, \partial M; R) \to H_{n-k}(M; R).$$

## Remarks

The relative fundamental class is the class whose restriction to $H_n(M, M \setminus \set{x})$ is the local orientation at each interior point $x$.
The proof uses a collar of the boundary to compare $M$ with its interior.
It then applies the duality theorem behind [[Poincaré duality|9VY90HJVZX]] to the interior, a noncompact manifold without boundary.
When $\partial M = \emptyset$, both isomorphisms reduce to Poincaré duality.

Example: for the disc $M = D^n$ with $\partial M = S^{n-1}$, $H^0(D^n) \cong \Z$ and $H_n(D^n, S^{n-1}) \cong \Z$.
Also $H^n(D^n, S^{n-1}) \cong \Z$ matches $H_0(D^n) \cong \Z$, and all other groups vanish on both sides.

## Explanations

### L1 human

Poincaré duality pairs holes of complementary dimensions on a closed manifold.
For a manifold with an edge, the same pairing works if one side of the pairing is measured relative to the edge.
For a disc, the single point-like piece matches the whole disc counted modulo its boundary circle.

### L2 human

Lefschetz duality is the form of Poincaré duality used for compact manifolds with boundary, such as knot exteriors and cobordisms.
Take a compact oriented $(2m+1)$-manifold $M$ and a field $F$.
Lefschetz duality and the long exact sequence of $(M, \partial M)$ show that the kernel of $H_m(\partial M; F) \to H_m(M; F)$ has half the dimension of $H_m(\partial M; F)$.
It is the basic tool in the study of manifolds with boundary and of bordism.
