---
tag: XM772FD0BS
kind: statement
role: theorem
name: Hilbert's theorem on the hyperbolic plane
msc: [53C42, 53A05]
uses: [7CBT4SM83Y, SQVQ5DQT6W, 6RW68JGBHC]
about: [SQVQ5DQT6W]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert's_theorem_(differential_geometry)
same_as:
  wikidata: Q2008549
  wikipedia: Hilbert's theorem (differential geometry)
---

## Statement

Let $S$ be a complete two-dimensional [[Riemannian manifold|7CBT4SM83Y]] whose [[Gaussian curvature|SQVQ5DQT6W]] is a negative constant.
Then there is no smooth isometric [[immersion|6RW68JGBHC]] of $S$ into $\R^3$.
In particular, the hyperbolic plane cannot be realized as a smooth surface in $\R^3$ with its induced metric.

## Remarks

After scaling, one may assume $K = -1$; one may also pass to the universal cover, which is the hyperbolic plane.
For an immersed surface with $K < 0$, the two asymptotic directions at each point give coordinates in which the angle $\omega$ between the coordinate curves satisfies the sine-Gordon equation $\omega_{uv} = \sin\omega$.
Completeness lets these coordinates cover the whole plane, and the equation then bounds the area of every coordinate quadrilateral by $2\pi$.
This contradicts the fact that the hyperbolic plane has infinite area.

The [[pseudosphere|44WEBQSKEY]] has constant curvature $-1$ and lies in $\R^3$, but it is not complete: it ends in a sharp edge.
The smoothness hypothesis matters: by the Nash–Kuiper theorem there are $C^1$ isometric embeddings of the hyperbolic plane into $\R^3$.
For constant positive curvature the situation is different, since round spheres are complete and lie in $\R^3$.

## Explanations

### L1 human

The hyperbolic plane is a surface that curves like a saddle at every point, by the same amount everywhere, and goes on forever.
Hilbert's theorem says that you cannot build such a surface in ordinary space without creases or edges.
Every smooth attempt, like the pseudosphere, must stop at some edge.
This is why hyperbolic geometry is usually drawn with models such as the Poincaré disc, which distort distances.

### L2 human

The theorem explains why the hyperbolic plane is studied as an abstract Riemannian manifold rather than as a surface in space.
Efimov later showed that a complete surface with curvature bounded above by a negative constant cannot be smoothly immersed in $\R^3$ either.
In contrast, the Nash embedding theorems show that every Riemannian manifold embeds isometrically in some higher-dimensional Euclidean space.
The proof is a good example of how the Gauss equation turns a geometric problem into a partial differential equation.
