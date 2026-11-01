---
tag: AZ6H4ZKK55
kind: statement
role: theorem
name: Carathéodory's theorem on boundary extension
msc: [30C35, 30D40]
uses: [0VHNKP1N3K, 8G5ABXRK85, 02WHMEG5ZR, 05GZ11PWRY, 0DRKT1QJR7]
about: [0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(conformal_mapping)
same_as:
  wikidata: Q4378889
  wikipedia: Carathéodory's theorem (conformal mapping)
---

## Statement

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]].
Let $J \subset \C$ be a Jordan curve, that is, a subset homeomorphic to a circle, and let $\Omega$ be the bounded component of $\C \setminus J$.
Let $f \colon \mathbb{D} \to \Omega$ be a [[conformal map|0VHNKP1N3K]] of $\mathbb{D}$ onto $\Omega$.
Then $f$ extends to a [[homeomorphism|05GZ11PWRY]] of the [[closure|0DRKT1QJR7]] $\overline{\mathbb{D}}$ onto $\overline{\Omega} = \Omega \cup J$.

## Remarks

Such an $f$ exists by the [[Riemann mapping theorem|02WHMEG5ZR]], since $\Omega$ is simply connected by the Jordan curve theorem.
The proof rests on a length–area estimate.
Let $\zeta$ be a point of the unit circle and let $r$ be small.
By the Cauchy–Schwarz inequality and the finite area of $\Omega$, some arc $\set{\abs{z - \zeta} = \rho} \cap \mathbb{D}$ with $r^2 < \rho < r$ has an image of length at most $C/\sqrt{\log(1/r)}$.
Because $J$ is a Jordan curve, a short crosscut of $\Omega$ cuts off a piece of small diameter, and this gives the continuity of $f$ at $\zeta$.
The Jordan property also gives injectivity on the circle.
The converse holds: if $f$ extends to such a homeomorphism, the boundary of $\Omega$ is the image of the circle, hence a Jordan curve.
A more general form says that $f$ extends continuously to $\overline{\mathbb{D}}$ if and only if the boundary of $\Omega$ is locally connected.
Example: the boundary of the slit disc $\mathbb{D} \setminus [0, 1)$ is not a Jordan curve.
A conformal map from $\mathbb{D}$ onto it extends continuously, but two points of the circle go to each inner point of the slit, so the extension is not injective.

## Explanations

### L1 human

The Riemann mapping theorem gives a conformal map from the disc onto any proper simply connected region, but it says nothing about the edge.
Carathéodory's theorem says that if the edge of the region is a simple closed curve, the map behaves well up to the edge.
The circle is then mapped continuously and one-to-one onto the boundary curve.

### L2 human

The theorem lets one transfer boundary value problems, such as the [[Dirichlet problem|8D56GQ4AG8]], from the disc to any Jordan domain.
It also shows that a conformal map between two Jordan domains extends to a homeomorphism of their closures, by composing two Riemann maps.
For domains with worse boundaries, the right replacement for boundary points is the notion of a [[prime end|GNWE3XR0ZG]].
Carathéodory's prime end theorem gives a bijection between the circle and the prime ends.
