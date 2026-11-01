---
tag: MP3F49QT3C
kind: problem
name: Group isomorphism problem
msc: ["20F10", "03D40"]
uses: [TJKANTKASZ, 0JGEQXQ4AC, 08MG7H8JW5]
about: [08MG7H8JW5, TJKANTKASZ]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism_problem
same_as:
  wikidata: Q5611242
  wikipedia: Group isomorphism problem
history:
  posed_by: "Max Dehn"
  first_stated: "1911"
---

## Problem

The *group isomorphism problem* asks for an algorithm that takes two finite [[presentations|0JGEQXQ4AC]] of groups and decides whether the groups they define are [[isomorphic|08MG7H8JW5]].
The problem may also be posed inside a class of [[finitely presented groups|TJKANTKASZ]]: the input is two presentations of groups of the class.

## Remarks

The problem is unsolvable in general.
By the Adian–Rabin theorem, there is no algorithm that decides whether a finite presentation defines the trivial group.
Since the trivial group has the finite presentation $\langle \ \mid \ \rangle$, no algorithm decides isomorphism of finitely presented groups.

The problem is solvable for some classes.
For finitely generated abelian groups given by finite presentations, the Smith normal form of the relation matrix gives the invariant factors.
Two such groups are isomorphic exactly when the invariants agree.
It is also solvable for [[hyperbolic groups|JWJ8YPR7EB]].
It is one of the three decision problems, with the word problem and the [[conjugacy problem|4AF7AF7690]], that Max Dehn posed.

For finite groups given by their multiplication tables the question is always decidable, and the interest is in the running time; this is a different, computational problem.

## Explanations

### L1 human

The same group can be written with very different generators and rules.
For example, $\langle a, b \mid a^2, b^3, a b a^{-1} b^{-1} \rangle$ and $\langle c \mid c^6 \rangle$ both define the cyclic group of order $6$, with $c = ab$.
The isomorphism problem asks whether a computer can always tell when two descriptions define the same group.
In general it cannot: no program can even decide whether a given description defines the group with one element.
