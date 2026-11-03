---
tag: 572DS8WXEH
kind: concept
name: L-infinity algebra
msc: [17B55, 18M70, 55P62]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_Lie_algebra
same_as:
  wikidata: Q42614797
  wikipedia: Homotopy Lie algebra
---

## Summary

An $L_\infty$-algebra, or strongly homotopy Lie algebra, is a graded vector space with a whole sequence of multilinear brackets $l_1, l_2, l_3, \ldots$.
The map $l_1$ is a differential and $l_2$ is a bracket.
The Jacobi identity for $l_2$ holds only up to a homotopy given by $l_3$, and so on.
A [[differential graded Lie algebra|D5XH66A8RP]] is the special case where all brackets $l_k$ with $k \ge 3$ vanish.
$L_\infty$-algebras are used in [[deformation theory|SWFR1GD6QT]], in rational homotopy theory and in mathematical physics.
In these fields many structures hold only up to homotopy.

## Explanations

### L1 human

In a Lie algebra the Jacobi identity holds exactly.
In many constructions it holds only "up to a correction term", and the correction term itself satisfies a rule only up to a further correction.
An $L_\infty$-algebra records this whole tower of corrections in one structure.
The first level is a differential $l_1$ with $l_1 \circ l_1 = 0$, as in a chain complex.
The second level is a bracket $l_2$ that is compatible with $l_1$.
The third map $l_3$ measures the failure of the Jacobi identity for $l_2$.
