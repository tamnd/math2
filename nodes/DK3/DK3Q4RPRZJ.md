---
tag: DK3Q4RPRZJ
kind: concept
name: Nilpotent operator
msc: [47A05, 47B01]
specializes: [063D5Z2C70]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_operator
same_as:
  wikidata: Q7037181
  wikipedia: Nilpotent operator
---

## Summary

A nilpotent operator is a bounded linear operator $T$ on a Banach space with $T^n = 0$ for some positive integer $n$.
It is the operator version of a [[nilpotent endomorphism|063D5Z2C70]] and of a [[nilpotent matrix|07BSPZPSMF]].
On a nonzero space its spectrum is $\set{0}$.
Operators with spectrum $\set{0}$ are called quasinilpotent; every nilpotent operator is quasinilpotent, but the Volterra operator is quasinilpotent without being nilpotent.

## Explanations

### L1 human

A nilpotent operator dies after a fixed number of applications.
On pairs of sequences, the map $(x, y) \mapsto (0, x)$ is an example: applied twice it gives $(0, 0)$.
In infinite dimensions one must be careful: an operator can shrink everything faster and faster under powers without ever reaching $0$, and such an operator is not nilpotent.
