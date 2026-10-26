---
tag: 0J6G5NJC5R
kind: statement
role: theorem
name: Kuratowski's theorem
msc: [05C10]
uses: [0P11X5HKAX, 029JQEK15B, 030A3FHN14]
sources:
  - url: https://en.wikipedia.org/wiki/Kuratowski's_theorem
    locator: Statement
same_as:
  wikidata: Q837902
  wikipedia: Kuratowski's theorem
---

## Statement

A subdivision of a [[graph|0JD5C82QMB]] $H$ is a graph that $H$ gives when some edges are replaced by paths with new inner vertices.
Let $G$ be a finite graph.
Then $G$ is [[planar|029JQEK15B]] if and only if no [[subgraph|0P11X5HKAX]] of $G$ is a subdivision of $K_5$ or of $K_{3,3}$.

## Remarks

One direction is easy: a subdivision of a nonplanar graph is nonplanar, and [[$K_5$ and $K_{3,3}$ are not planar|030A3FHN14]].
Wagner's theorem is a related result: a finite graph is planar if and only if it has neither $K_5$ nor $K_{3,3}$ as a minor.

## History

Kazimierz Kuratowski published the theorem in 1930.
Orrin Frink and Paul Smith proved it independently in the same year, but they did not publish their proof.
Lev Pontryagin reportedly proved it around 1927, and in the Soviet Union it was also known under his name.

## Explanations

### L1 human

There are exactly two kinds of obstacle to drawing a graph without crossings.
A graph is planar unless it contains a copy of $K_5$ or $K_{3,3}$ in which some edges are stretched into paths.
