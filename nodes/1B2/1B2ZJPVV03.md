---
tag: 1B2ZJPVV03
kind: statement
role: theorem
name: Wagner's theorem
msc: [05C10, 05C83]
uses: [0JD5C82QMB, 029JQEK15B, VYQ32ZBPEE, 03WKB2H474, 0V0GC7BQAN]
about: [029JQEK15B, VYQ32ZBPEE]
sources:
  - url: https://en.wikipedia.org/wiki/Wagner's_theorem
same_as:
  wikidata: Q7959587
  wikipedia: Wagner's theorem
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]].
Then $G$ is [[planar|029JQEK15B]] if and only if neither the [[complete graph|03WKB2H474]] $K_5$ nor the [[complete bipartite graph|0V0GC7BQAN]] $K_{3,3}$ is a [[minor|VYQ32ZBPEE]] of $G$.

## Remarks

Deleting vertices or edges and contracting edges keep a plane drawing plane, so every minor of a planar graph is planar.
Since $K_5$ and $K_{3,3}$ are not planar, a planar graph has neither as a minor.
For the converse, if $G$ is not planar, [[Kuratowski's theorem|0J6G5NJC5R]] gives a subgraph that is a subdivision of $K_5$ or of $K_{3,3}$.
Contracting the subdivided paths of this subgraph back to single edges gives $K_5$ or $K_{3,3}$ as a minor.
For example, the [[Petersen graph|0NR95CTFCZ]] is not planar: contracting its five spokes gives $K_5$.
Klaus Wagner published the theorem in 1937.

## Explanations

### L1 human

A graph is planar when you can draw it without crossings.
Wagner's theorem says that the only obstacles are the five-vertex complete graph and the three-houses-three-utilities graph, found inside $G$ after deleting and shrinking parts.
So to prove a graph is not planar, it is enough to exhibit one of these two inside it.

### L2 human

Wagner's theorem is the minor version of Kuratowski's theorem.
It shows that the class of planar graphs is closed under minors and is described by exactly two forbidden minors.
The [[Robertson–Seymour theorem|WP3GDNWJJW]] says that every minor-closed class of graphs has such a finite description.
