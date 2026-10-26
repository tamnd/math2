---
tag: 02WHMEG5ZR
kind: statement
role: theorem
name: Riemann mapping theorem
aliases: [riemann-mapping]
msc: [30C35]
uses: [0DG0Z72CQD, 0VHNKP1N3K]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_mapping_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Riemann_mapping_theorem
    locator: History
same_as:
  wikidata: Q927051
  wikipedia: Riemann mapping theorem
---

## Statement

Let $U$ be a nonempty open subset of $\mathbb{C}$ with $U \neq \mathbb{C}$.
Suppose that $U$ is simply connected: $U$ is connected, and each closed path in $U$ can be continuously deformed in $U$ to a constant path.
Let $\mathbb{D} = \{ z \in \mathbb{C} : |z| < 1 \}$.
Then there is a biholomorphic map $f$ from $U$ onto $\mathbb{D}$, that is, a bijective [[holomorphic|0DG0Z72CQD]] map with a holomorphic inverse.
Moreover, for each $z_0 \in U$ there is exactly one such $f$ with $f(z_0) = 0$ and $f'(z_0)$ a positive real number.

## Remarks

A biholomorphic map is [[conformal|0VHNKP1N3K]], so $U$ and $\mathbb{D}$ are conformally equivalent.
The case $U = \mathbb{C}$ is excluded: a holomorphic map $\mathbb{C} \to \mathbb{D}$ is bounded, so it is constant by [[Liouville's theorem|0EHKVRF4J6]].
The uniqueness follows from the [[Schwarz lemma|0MB48XDBY3]].
Riemann stated the theorem in his thesis of 1851, and Osgood gave the first rigorous proof in 1900.

## Explanations

### L1 human

The theorem says that every simply connected open set in the plane, except the plane itself, looks like the unit disc to complex analysis.
The set can have a very irregular boundary, and the map still exists.
For the upper half-plane, the [[Cayley transform|0X45ZM731G]] is such a map.
