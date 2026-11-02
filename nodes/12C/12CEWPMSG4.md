---
tag: 12CEWPMSG4
kind: concept
name: Mackey machine
msc: [22D30, 22D10]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_imprimitivity
---

## Summary

The Mackey machine is a method to find the irreducible [[unitary representations|74BPYJNZTM]] of a [[locally compact group|AHV05ZBCYW]] $G$.
It builds them from a closed normal subgroup $N$ and from smaller subgroups.
In its basic form $G = N \rtimes H$ with $N$ abelian.
One lets $H$ act on the characters of $N$, picks one character in each orbit, and [[induces|6Q7AHAZ6Q4]] from its stabiliser.
When the orbits are well behaved, this gives every irreducible representation exactly once up to equivalence.
It explains the representations of the $ax + b$ group, of the Euclidean motion groups and of the Poincaré group.

## Explanations

### L1 human

Many groups are built from a simple abelian part, like translations, and a group that acts on it, like rotations.
The translations alone have one-dimensional representations, labelled by frequencies.
The rotations move these frequencies around, and frequencies in the same orbit give the same representation of the whole group.
So one picks one frequency per orbit, looks at the rotations that fix it, and combines the two pieces by induction.
For the motion group of the plane, the orbits are the circles of radius $r > 0$ and the origin, and each circle gives one infinite-dimensional irreducible representation.
