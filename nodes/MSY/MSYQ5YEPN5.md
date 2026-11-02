---
tag: MSYQ5YEPN5
kind: definition
name: Erlangen program
msc: [51N25, 51-03, 20H15]
defines: 9QW65PGEPW
uses: [G5S1M9, 0WCY42EV9V, 85TWR6E75P]
sources:
  - url: https://en.wikipedia.org/wiki/Erlangen_program
---

## Definition

Let $X$ be a set and let $G$ be a [[group|G5S1M9]] with a [[transitive action|0WCY42EV9V]] on $X$.
In the sense of the *Erlangen program*, the pair $(X, G)$ is a *geometry*.
A property of subsets of $X$ belongs to the geometry $(X, G)$ if it is invariant under $G$.
This means that, for each subset $S$ and each $g \in G$, it holds for $S$ exactly when it holds for $g(S)$.
Two subsets of $X$ are *equivalent* in the geometry if some $g \in G$ maps one onto the other.

## Remarks

Example: $X = \R^2$ with $G$ the affine group gives affine geometry.
The property "the points $a, b, c$ are collinear" belongs to it, since affine maps send lines onto lines.
Non-example: the property "the segment $ab$ has length $1$" does not belong to affine geometry, since the map $x \mapsto 2x$ is affine and doubles lengths.
Since $G$ acts transitively, $X$ is a [[homogeneous space|85TWR6E75P]] $G/H$, where $H$ is the stabilizer of a point.
