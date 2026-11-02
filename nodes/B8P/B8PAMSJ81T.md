---
tag: B8PAMSJ81T
kind: concept
name: Plücker coordinates
msc: ["51M30", "14M15", "51N15"]
sources:
  - url: https://en.wikipedia.org/wiki/Pl%C3%BCcker_coordinates
same_as:
  wikidata: Q2559456
  wikipedia: Plücker coordinates
---

## Summary

Plücker coordinates describe a line of three-dimensional projective space by six homogeneous numbers, the $2 \times 2$ minors of a matrix whose rows span the line.
They turn the set of lines of $\mathbb{P}^3$ into the points of a quadric in $\mathbb{P}^5$, the [[Klein quadric|6WV71T5CK1]].
More generally, the same minors embed every [[Grassmannian|CYPA882RB9]] into a projective space.

## Explanations

### L1 human

A point of projective space has coordinates, but a line is a bigger object, so how does one give it coordinates?
Pick two points on the line and write their coordinates as the two rows of a $2 \times 4$ matrix.
The six $2 \times 2$ minors of that matrix do not depend, up to a common factor, on which two points were picked.
These six numbers are the Plücker coordinates of the line.
For the line through $[1 : 0 : 0 : 0]$ and $[0 : 1 : 0 : 0]$, only one minor is nonzero.
