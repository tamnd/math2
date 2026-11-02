---
tag: 1NDRD8BHFG
kind: concept
name: Homotopy limit
msc: [18N40, 55U35, 55P65]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_colimit_and_limit
---

## Summary

A homotopy limit is the version of a [[limit|CHS5AFJGWE]] that respects weak equivalences.
Ordinary limits of diagrams of spaces can change drastically when the diagram is replaced by a weakly equivalent one; homotopy limits do not.
In a [[model category|SDTZVZ6B4Q]] the homotopy limit is the right derived functor of the limit functor.
Homotopy pullbacks, homotopy fixed points and the space of maps out of a homotopy colimit are typical instances.

## Explanations

### L1 human

The pullback of two maps to a space $Z$ consists of pairs of points with the same image.
In homotopy theory equality is too strict; one should allow a path in $Z$ between the two images.
The homotopy pullback of $X \to Z \leftarrow Y$ is therefore the space of triples $(x, \omega, y)$ with $\omega$ a path from the image of $x$ to the image of $y$.
For two points of the real line, the ordinary pullback is empty if the points differ, while the homotopy pullback is the space of paths between them, which is contractible.
Homotopy limits extend this idea from pullbacks to all diagrams.
