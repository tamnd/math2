---
tag: JJ0PQZ7VZX
kind: definition
name: Circle packing
msc: [52C15, 52C26, 05B40]
defines: S360JBEYKD
uses: [060W5CBZP6, 0Q0H13G8ZB]
sources:
  - url: https://en.wikipedia.org/wiki/Circle_packing
---

## Definition

Let $(C_i)_{i \in I}$ be a family of [[circles|060W5CBZP6]] of positive radius in the plane $\R^2$, and let $D_i$ be the closed disc bounded by $C_i$.
The family is a *circle packing* if the discs $D_i$ have pairwise disjoint interiors.
Its *tangency graph* has vertex set $I$, with an edge between distinct $i$ and $j$ when $C_i$ and $C_j$ are tangent.
A packing of *equal circles* is one in which all radii are equal.

## Remarks

Example: the circles of radius $1$ centred at $(0, 0)$ and $(2, 0)$.
The distance between centres is $2$, the sum of the radii, so the [[discs|0Q0H13G8ZB]] meet in the single point $(1, 0)$ and their interiors are disjoint.
The tangency graph is one edge.
Non-example: circles of radius $1$ centred at $(0, 0)$ and $(1, 0)$; the distance $1$ is less than $2$, so the open discs overlap.
The same notion is used on the sphere and in the hyperbolic plane.
A packing of equal circles of radius $r$ is the same as a sphere packing in $\R^2$ with radius $r$.
