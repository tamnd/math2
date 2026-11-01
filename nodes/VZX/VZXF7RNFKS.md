---
tag: VZXF7RNFKS
kind: concept
name: Germ
msc: [54A20, 58A99]
sources:
  - url: https://en.wikipedia.org/wiki/Germ_(mathematics)
same_as:
  wikidata: Q2520842
  wikipedia: Germ (mathematics)
---

## Summary

The germ of a function at a point records the behaviour of the function on arbitrarily small [[neighbourhoods|0ZCY0Z80B6]] of the point and forgets the rest.
Two functions have the same germ at $x$ when they agree on some neighbourhood of $x$.
Germs make local properties, such as derivatives and local power series, into properties of single objects.
They are the stalks of the sheaf of functions and appear throughout analysis, geometry and singularity theory.

## Explanations

### L1 human

Look at a function through a microscope at one point, and keep zooming in.
Two functions have the same germ at the point if, after enough zoom, they look identical.
For example, $t \mapsto t$ and $t \mapsto \abs{t}$ on $\R$ have the same germ at $1$, since they agree on $(0, 2)$.
They have different germs at $0$, because every interval around $0$ contains negative numbers, where they differ.
