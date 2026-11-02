---
tag: 9YA6S6HD9V
kind: concept
name: Homotopy
msc: [55Q05, 55P10]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy
same_as:
  wikidata: Q746083
  wikipedia: Homotopy
---

## Summary

A homotopy between two [[continuous maps|0VGFHTM75Y]] $f, g \colon X \to Y$ is a continuous deformation of $f$ into $g$, parametrised by a time $t \in [0, 1]$.
Formally it is a continuous map $H \colon X \times [0, 1] \to Y$ with $H(\cdot, 0) = f$ and $H(\cdot, 1) = g$.
Homotopy is the basic notion of algebraic topology.
Homotopic maps induce the same maps on homology and cohomology, and homotopies that fix a base point give the same maps on homotopy groups.

## Explanations

### L1 human

Think of $f$ as a picture drawn in $Y$, and of the homotopy as a film that moves this picture continuously until it becomes $g$.
At each moment $t$ the frame $H(\cdot, t)$ is again a continuous map.
For example, in the plane $\R^2$ any two maps $f, g \colon X \to \R^2$ are joined by the straight-line homotopy $H(x, t) = (1 - t) f(x) + t g(x)$.
In a space with a hole, such as the plane without the origin, a loop around the hole cannot be moved to a constant loop.
