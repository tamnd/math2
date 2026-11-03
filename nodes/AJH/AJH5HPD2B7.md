---
tag: AJH5HPD2B7
kind: statement
role: theorem
name: Wang tile undecidability
msc: [03D35, 05B45, 52C20]
uses: [3J6YG01N22, W6ESDYBF8Z]
about: [BBYNPDWR5R]
sources:
  - url: https://en.wikipedia.org/wiki/Wang_tile
---

## Statement

A [[Wang tile|BBYNPDWR5R]] is a unit square whose four edges carry colours from a finite set, and tiles may not be rotated or reflected.
A finite set $W$ of Wang tiles *tiles the plane* if there is a map $\tau \colon \Z^2 \to W$ with two properties for all $(i, j) \in \Z^2$.
The right edge of $\tau(i, j)$ has the colour of the left edge of $\tau(i + 1, j)$.
The top edge of $\tau(i, j)$ has the colour of the bottom edge of $\tau(i, j + 1)$.
Then the domino problem is undecidable: the language of codes of finite sets $W$ of Wang tiles that tile the plane is not [[decidable|3J6YG01N22]].

## Remarks

The proof encodes the run of a [[Turing machine|W6ESDYBF8Z]] on blank tape into tilings, so that a tile set tiles the plane exactly when the machine never halts.
Then a decision procedure for tilings would solve the halting problem.
The hard part is to force the computation to appear in every tiling, and this is done with an aperiodic tile set that builds a hierarchy of nested squares.
Wang had observed that, if every tile set that tiles the plane also had a periodic tiling, the problem would be decidable.
Berger proved the theorem in 1966, and thereby showed that aperiodic sets of Wang tiles exist.
By a compactness argument, $W$ tiles the plane if and only if it tiles every finite square $\set{0, \dots, m}^2$.
So the set of tile sets that do not tile the plane is recursively enumerable, and the set of tile sets that do tile the plane is not.
Example: a single tile with all four edges of one colour tiles the plane, while a single tile whose left and right edges have different colours does not.

## Explanations

### L1 human

Given a finite collection of coloured square tiles, can one cover the whole infinite floor so that touching edges always match?
For each small collection one may find the answer by hand.
The theorem says that no computer program can answer this question correctly for every collection.
The reason is that tiles can be designed to imitate any computer, so the tiling question contains the question of whether a program runs forever.

### L2 human

The theorem is a standard example of undecidability outside logic, in geometry and combinatorics.
It is proved by a [[many-one reduction|JTAH37JTHD]] from the complement of the halting problem for machines started on a blank tape.
It implies that tiling sets of many other kinds, and the emptiness of two-dimensional subshifts of finite type, are undecidable.
By contrast, the analogous problem in one dimension is decidable, since it reduces to finding a cycle in a finite graph.
