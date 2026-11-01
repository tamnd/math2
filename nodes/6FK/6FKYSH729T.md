---
tag: 6FKYSH729T
kind: concept
name: Quasi-isometry
msc: [20F65, 51F30, 53C23]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-isometry
same_as:
  wikidata: Q614527
  wikipedia: Quasi-isometry
---

## Summary

A quasi-isometry is a map between [[metric spaces|0VKD1TP7F3]] that distorts distances by at most a fixed factor and a fixed additive error.
In addition, its image comes within a bounded distance of every point.
It ignores all small-scale structure and keeps only the large-scale shape of a space.
Two spaces joined by a quasi-isometry are called quasi-isometric, and this is an equivalence relation.
It is the basic notion of sameness in [[geometric group theory|2T3218RXTD]], since all [[word metrics|VCHJVR9NGH]] of a finitely generated group are quasi-isometric to one another.

## Explanations

### L1 human

Look at a space from very far away, so far that bounded errors become invisible.
Two spaces are quasi-isometric if they look the same from there.
The integers $\Z$ and the real line $\R$ are quasi-isometric: the inclusion $\Z \to \R$ keeps distances exactly, and every real number is within $1/2$ of an integer.
Likewise the grid $\Z^2$ looks like the plane $\R^2$.
A bounded space, such as a disc, is quasi-isometric to a single point.
