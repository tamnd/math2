---
tag: HH35EXPKEC
kind: definition
name: Partial linear space
msc: ["51A45", "51E14", "05B25"]
defines: CX07CWPCDX
uses: [FGKNAFNHA3]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_linear_space
---

## Definition

Let $(P, L, I)$ be an [[incidence structure|FGKNAFNHA3]] with point set $P$, line set $L$ and incidence relation $I \subseteq P \times L$.
It is a *partial linear space* if:

1. any two distinct points are incident with at most one common line;
2. every line is incident with at least two points.

It is a *linear space* if in clause 1 "at most one" is replaced by "exactly one".

## Remarks

Example: the $3 \times 3$ grid, with $P = \set{1, 2, 3}^2$ and $L$ the three rows $\set{i} \times \set{1, 2, 3}$ and the three columns $\set{1, 2, 3} \times \set{j}$.
A row and a column meet in one point, two rows or two columns are disjoint, so two distinct points share at most one line; each line has three points.

Non-example: $P = \set{a, b, c}$ with lines $\set{a, b}$ and $\set{a, b, c}$.
The points $a$ and $b$ lie on two lines, so clause 1 fails.

Clause 1 is equivalent to its dual: two distinct lines meet in at most one point.
Partial linear spaces are also called semilinear spaces or near-linear spaces.
