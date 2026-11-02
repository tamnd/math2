---
tag: P5MA4CDRNA
kind: concept
name: Complete atomic Boolean algebra
msc: ["06E10", "06E05"]
specializes: [75BPV95AAS]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Boolean_algebra
---

## Summary

A complete atomic Boolean algebra is a [[complete Boolean algebra|75BPV95AAS]] in which every nonzero element lies above an [[atom|TTVCTW6TNC]].
Every power set algebra is of this kind.
Conversely, every complete atomic Boolean algebra is isomorphic to the power set of its set of atoms.
So these algebras are the same as sets, seen algebraically.
With homomorphisms that preserve all suprema, their category is dual to the category of sets.

## Explanations

### L1 human

An atom is a smallest nonzero element, like a single point among the subsets of a set.
In a complete atomic Boolean algebra, every element is built from the atoms below it, and every collection of atoms builds an element.
So the algebra is just the family of all subsets of its atoms.
For example, the subsets of $\set{1, 2, 3}$ form such an algebra with the three atoms $\set{1}$, $\set{2}$, $\set{3}$.
