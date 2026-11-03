---
tag: GVVQKX5AB8
kind: object
name: Bondi–Metzner–Sachs group
msc: ["83C30", "83C40", "22E65"]
instance_of: [G5S1M9]
uses: [0H3WZXCZNF, QWK3BYVJ9W, 8ZQ9TA4Q2Q, 3HTF65XMF7, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Bondi%E2%80%93Metzner%E2%80%93Sachs_group
same_as:
  wikidata: Q28456647
  wikipedia: Bondi–Metzner–Sachs group
---

## Description

The Bondi–Metzner–Sachs group, or BMS group, is the [[group|G5S1M9]] of asymptotic symmetries of spacetimes that are [[asymptotically flat|3HTF65XMF7]] at future null infinity.
Use coordinates $(u, z)$ on null infinity $\R \times S^2$, where $u$ is retarded time and $z \in \C \cup \set{\infty}$ is a stereographic coordinate on the sphere.
The group acts by
$$(u, z) \mapsto \Bigl( K(z) \bigl( u + \alpha(z) \bigr), \ \frac{az + b}{cz + d} \Bigr), \qquad K(z) = \frac{1 + \abs{z}^2}{\abs{az + b}^2 + \abs{cz + d}^2}.$$
Here $a, b, c, d \in \C$ with $ad - bc = 1$, and $\alpha$ is a smooth real function on $S^2$.
The maps with $a = d = 1$, $b = c = 0$ are the *supertranslations* $u \mapsto u + \alpha(z)$; they form an infinite-dimensional abelian normal subgroup $S$.
The maps with $\alpha = 0$ form a subgroup isomorphic to the proper orthochronous [[Lorentz group|QWK3BYVJ9W]] $SL(2, \C)/\set{\pm 1}$.
So the BMS group is the [[semidirect product|0H3WZXCZNF]] $S \rtimes SO^+(1, 3)$.
Check of one case: the identity matrix gives $K(z) = (1 + \abs{z}^2)/(\abs{z}^2 + 1) = 1$, so the map is the supertranslation by $\alpha$.

## Remarks

The supertranslations whose function $\alpha$ is a combination of the [[spherical harmonics|3F32Y21HP4]] with $\ell = 0$ and $\ell = 1$ form a 4-dimensional normal subgroup, the translations.
Together with a Lorentz subgroup they form a copy of the [[Poincaré group|8ZQ9TA4Q2Q]], but there are infinitely many such copies, conjugate by supertranslations.
This is why angular momentum at null infinity has no unique definition, unlike energy-momentum.
The group was found by Bondi, van der Burg and Metzner and by Sachs in 1962.

## Explanations

### L1 human

Far away from an isolated system, spacetime looks flat, so one expects the symmetries of flat spacetime, the Poincaré group.
Instead one finds a larger group: besides the Lorentz transformations, one may shift the retarded time by a different amount in each direction of the sky.
These angle-dependent time shifts, the supertranslations, make the group infinite-dimensional.
