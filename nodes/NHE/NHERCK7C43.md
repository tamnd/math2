---
tag: NHERCK7C43
kind: example
name: Poincaré homology sphere
msc: [57K30, 57M05]
instance_of: [HK8NS02NNE]
sources:
  - url: https://en.wikipedia.org/wiki/Homology_sphere
---

## Example

Identify the $3$-sphere $S^3$ with the group [[$SU(2)$|E5P8AG6CK7]] of unit quaternions.
The double cover $SU(2) \to SO(3)$ maps onto the rotation group of a regular icosahedron, a group of order $60$ isomorphic to $A_5$.
Its preimage $I^*$ in $SU(2)$ is the binary icosahedral group, of order $120$.
The Poincaré homology sphere is the quotient $P = S^3 / I^*$ of $S^3$ by the action of $I^*$ by left multiplication.

This action is free, so $P$ is a closed orientable [[3-manifold|R20TB2KEQQ]] with [[fundamental group|S1XK3HXHFX]] $I^*$.
The group $I^*$ is perfect, so $H_1(P; \Z)$, the abelianization of $I^*$, is $0$.
By [[Poincaré duality|9VY90HJVZX]], $H_2(P; \Z) \cong H^1(P; \Z) = \Hom(H_1(P; \Z), \Z) = 0$, and $H_3(P; \Z) = \Z$.
So $P$ has the homology of $S^3$ and is a [[homology sphere|HK8NS02NNE]].
It is not homeomorphic to $S^3$, because its fundamental group is not trivial.

## Remarks

The same manifold is obtained from a solid regular dodecahedron by gluing each face to the opposite face after a turn of $1/10$ of a full turn.
It is also the link of the singularity of $x^2 + y^3 + z^5 = 0$ in $\C^3$, often written $\Sigma(2, 3, 5)$.
Poincaré found it while testing whether homology characterises the $3$-sphere, and this example led him to the [[Poincaré conjecture|3R064KFF68]], which uses the fundamental group instead.

## Explanations

### L1 human

The Poincaré homology sphere looks like the $3$-sphere to homology: it has no holes of dimension $1$ or $2$.
Still, it contains loops that cannot be shrunk to a point.
It shows that counting holes with homology is not enough to recognise the sphere.
