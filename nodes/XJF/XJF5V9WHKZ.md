---
tag: XJF5V9WHKZ
kind: statement
role: theorem
name: Gleason–Yamabe theorem
msc: ["22D05", "22E05", "22A05"]
uses: [AHV05ZBCYW, 7JBRGCVJRB, QYCFH68RD1, 0CB0DX5BVV, HPMAJV2RDY]
about: [AHV05ZBCYW, 7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_fifth_problem
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]].
Then there is an [[open subgroup|QYCFH68RD1]] $G'$ of $G$ with the following property.
Let $U$ be any open neighbourhood of the identity in $G'$.
Then there is a compact [[normal subgroup|0CB0DX5BVV]] $K$ of $G'$ with $K \subseteq U$ such that $G'/K$ is isomorphic, as a topological group, to a [[Lie group|7JBRGCVJRB]].

## Remarks

The proof has two parts.
Gleason showed that a locally compact group with [[no small subgroups|HPMAJV2RDY]] is a Lie group, by building one-parameter subgroups and a Lie algebra from the group itself.
Yamabe then showed that every locally compact group can be reduced to this case by dividing out small compact normal subgroups, after passing to an open subgroup.
Example: for $G = \Z_p$, the $p$-adic integers, take $G' = G$ and $K = p^n \Z_p$ inside a given neighbourhood of $0$; then $G/K = \Z/p^n\Z$ is a finite group, hence a Lie group of dimension $0$.
The open subgroup is needed.
The group $G = PSL_2(\Q_p)$ is simple as an abstract group, so its only compact normal subgroup is trivial.
But $G$ is totally disconnected and not discrete, so it is not a Lie group.
Here one takes for $G'$ a compact open subgroup such as the image of $SL_2(\Z_p)$, which is profinite.
A corollary is that a locally compact group with no small subgroups is a Lie group.

## Explanations

### L1 human

The theorem says that every locally compact group is close to a Lie group.
After passing to an open piece of the group and ignoring an arbitrarily small compact part, what is left is a smooth group.
So the smooth groups of calculus and geometry, together with compact groups such as profinite groups, are the building blocks of all locally compact groups.

### L2 human

The theorem gives the solution of Hilbert's fifth problem: a locally Euclidean group has no small subgroups, so it is a Lie group.
It is also the starting point of the structure theory of locally compact groups.
For a connected locally compact group one can take $G' = G$, so $G$ is a projective limit of Lie groups.
The theorem has found use outside group theory, for example in Breuillard, Green and Tao's classification of approximate groups and in Gromov's theorem on groups of polynomial growth.
