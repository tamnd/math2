---
tag: CFDZJ55N95
kind: statement
role: theorem
name: Gelfand–Raikov theorem
msc: ["22D10", "43A65", "43A35"]
uses: [AHV05ZBCYW, 74BPYJNZTM, FX3NEFYFFN, 3PRZ02APFA]
about: [AHV05ZBCYW, 74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Raikov_theorem
same_as:
  wikidata: Q18207320
  wikipedia: Gelfand–Raikov theorem
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $g \in G$ with $g \ne e$.
Then there is an [[irreducible|FX3NEFYFFN]] [[unitary representation|74BPYJNZTM]] $\pi$ of $G$ on a Hilbert space $H$ such that $\pi(g) \ne \id_H$.

## Remarks

In short, the irreducible unitary representations of a locally compact group separate its points.
The proof works with continuous [[positive-definite functions|3PRZ02APFA]] $\varphi$ with $\varphi(e) \le 1$.
These form a convex set, compact in the weak-$*$ topology of $L^\infty(G)$.
Its nonzero extreme points are exactly the functions $x \mapsto \ip{\pi(x)v}{v}$ with $\pi$ irreducible and $v$ a unit vector.
The left regular representation supplies a positive-definite function that is not constant on the pair $\set{e, g}$, and the Krein–Milman theorem then yields an extreme point with the same property.
Example: for $G = \R$, the characters $x \mapsto e^{ixy}$, $y \in \R$, are one-dimensional irreducible unitary representations, and for $g \ne 0$ one can choose $y$ with $e^{igy} \ne 1$.
For a compact group the representations can be chosen finite-dimensional, which is part of the Peter–Weyl theorem.

## Explanations

### L1 human

A unitary representation lets a group act by rotations on a Hilbert space, and irreducible ones are the building blocks that cannot be split further.
The theorem says that there are enough building blocks to see every element: each element other than the identity acts nontrivially in at least one of them.
So no information about the group is lost when one studies it through its irreducible unitary representations.

### L2 human

The theorem justifies the program of harmonic analysis on locally compact groups, which aims to decompose functions and representations into irreducible pieces.
It is the starting point for the study of the unitary dual and of the group C\*-algebra, since it shows that the irreducible representations already detect the group.
For abelian groups, it says that characters separate points, which is a step towards Pontryagin duality.
Irreducible representations may need to be infinite-dimensional: for a connected simple Lie group such as $SL_2(\R)$, every finite-dimensional unitary representation is trivial.
