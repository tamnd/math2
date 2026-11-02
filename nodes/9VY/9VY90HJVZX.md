---
tag: 9VY90HJVZX
kind: statement
role: theorem
name: Poincaré duality
msc: [55M05, 57N65, 57P10]
uses: [QQQ9B1DK4P, 913WEQERBE, ZEA0PEM3B2, N7SXBQ7WK0, 6N7BC70CX0, M0Q5CFJ7ZH, ST71ZV3FES, RNDDWDAFJ5, 1DDYB6VVSR]
about: [6N7BC70CX0, M0Q5CFJ7ZH, ZEA0PEM3B2]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9_duality
same_as:
  wikidata: Q2063099
  wikipedia: Poincaré duality
---

## Statement

Let $M$ be a closed [[topological manifold|QQQ9B1DK4P]] of dimension $n$, that is, compact and without boundary.
Let $R$ be a commutative ring with $1$, and assume that $M$ is $R$-[[oriented|913WEQERBE]], with [[fundamental class|ZEA0PEM3B2]] $[M] \in H_n(M; R)$.
Then for every $k$ the map
$$D \colon H^k(M; R) \to H_{n-k}(M; R), \qquad D(a) = [M] \frown a,$$
given by the [[cap product|N7SXBQ7WK0]], is an isomorphism from [[singular cohomology|6N7BC70CX0]] to [[singular homology|M0Q5CFJ7ZH]].

## Remarks

The proof first shows a version with compactly supported cohomology for every $R$-oriented manifold, not only closed ones.
It holds for open subsets of $\R^n$ that are convex, and it passes to unions by a Mayer–Vietoris argument and to increasing unions by a limit argument.
For a closed manifold, compactly supported cohomology is ordinary cohomology.

Every closed manifold is $\Z/2$-oriented, so the theorem always holds with $\Z/2$ coefficients.
With a field $F$ of coefficients, it implies that the pairing $H^k(M; F) \times H^{n-k}(M; F) \to F$, $(a, b) \mapsto \langle a \smile b, [M] \rangle$, is nondegenerate.
In particular, the [[Betti numbers|ST71ZV3FES]] satisfy $b_k(M) = b_{n-k}(M)$ for closed orientable $M$, and the [[Euler characteristic|RNDDWDAFJ5]] of a closed manifold of odd dimension is $0$.

The hypotheses are needed.
Without orientability: for the [[real projective plane|1DDYB6VVSR]], $H^0(\R P^2; \Z) = \Z$ but $H_2(\R P^2; \Z) = 0$.
Without compactness: $H^0(\R^n; \Z) = \Z$ but $H_n(\R^n; \Z) = 0$ for $n \ge 1$.

## Explanations

### L1 human

On a closed oriented manifold of dimension $n$, the holes of dimension $k$ and the holes of dimension $n - k$ come in matching pairs.
For a closed orientable surface, the number of independent loops is even, because each loop has a partner loop that it crosses once.
The duality comes from cutting the manifold into cells and also into the dual cells, where each $k$-cell matches an $(n - k)$-cell crossing it.

### L2 human

The theorem identifies cohomology and homology of closed oriented manifolds with a shift of degree $n$.
It turns the cup product into intersection of cycles, which gives the intersection form of a $4$-manifold and its unimodularity.
It yields the symmetry of Betti numbers and the vanishing of the Euler characteristic in odd dimensions.
Lefschetz duality extends it to compact manifolds with boundary, and Alexander duality is a consequence for complements of subsets of spheres.
