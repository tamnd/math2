---
tag: JMWHKWD7EX
kind: example
name: Hopf link
msc: [57K10]
instance_of: [1A5WRCNTM3]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_link
same_as:
  wikidata: Q864313
  wikipedia: Hopf link
---

## Example

Let $C_1 = \set{(x, y, 0) \in \R^3 : x^2 + y^2 = 1}$ and $C_2 = \set{(x, 0, z) \in \R^3 : (x - 1)^2 + z^2 = 1}$.
Each of them is a round [[circle|060W5CBZP6]].
They are disjoint: a common point would have $y = 0$ and $z = 0$, so $x = \pm 1$ from $C_1$ and $x \in \set{0, 2}$ from $C_2$, which is impossible.
So $C_1 \cup C_2$ is a [[link|1A5WRCNTM3]] with $2$ components, the *Hopf link*.
The circle $C_2$ passes once through the flat disk bounded by $C_1$, at the point $(0, 0, 0)$, and it meets that disk nowhere else.
Hence the [[linking number|SFJ329YB9F]] of the two components is $\pm 1$, the sign depending on the orientations.
The unlink of two components has linking number $0$, so the Hopf link is not equivalent to it: the two rings cannot be pulled apart.

## Remarks

Each component is an [[unknot|1TQ06R4Q66]].
The Hopf link has a diagram with $2$ crossings, and it is the only nontrivial link with at most $2$ crossings.
Its complement in $S^3$ is homeomorphic to $T^2 \times (0, 1)$, the product of a torus and an open interval, so its link group is $\Z \times \Z$.
Any two distinct fibres of the [[Hopf fibration|M5AKNYC4QQ]] $S^3 \to S^2$ form a Hopf link, which gives the name.
It is the torus link of type $(2, 2)$, a two-component relative of the [[torus knots|NS60VV786W]].

## Explanations

### L1 human

The Hopf link is two rings hooked together, like two neighbouring links of a chain.
Each ring on its own is unknotted, but they cannot be separated without cutting one of them.
It is the simplest link that is really linked.
