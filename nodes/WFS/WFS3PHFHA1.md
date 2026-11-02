---
tag: WFS3PHFHA1
kind: statement
role: theorem
name: Necklace splitting theorem
msc: [05D99, 91B32, 55M20]
uses: [QHJ0GBQE2E]
sources:
  - url: https://en.wikipedia.org/wiki/Necklace_splitting_problem
---

## Statement

Let $k \ge 2$ and $t \ge 1$ be integers.
Let a necklace be a row of beads of $t$ colours.
Suppose colour $i$ occurs exactly $k a_i$ times, for some integer $a_i \ge 0$.
Then the necklace can be cut in at most $(k - 1) t$ places so that the pieces can be divided among $k$ people fairly.
Fairly means that each person receives exactly $a_i$ beads of colour $i$, for every $i$.

## Remarks

For $k = 2$ the result follows from the [[Borsuk–Ulam theorem|QHJ0GBQE2E]].
Model the necklace as the interval $[0, 1]$, with each bead a short subinterval.
A point $x$ of the sphere $S^t \subset \R^{t+1}$ encodes a cut into $t+1$ consecutive pieces of lengths $x_1^2, \dots, x_{t+1}^2$.
The sign of $x_j$ tells which of the two people gets piece $j$.
For each colour, take the amount the first person gets minus half the total; this defines an odd map $S^t \to \R^t$.
By Borsuk–Ulam it has a zero, which is a fair split with at most $t$ cuts.
A final step moves the cuts to bead boundaries.
The general case is due to Noga Alon, by induction on the prime factors of $k$ using a generalisation of Borsuk–Ulam.

The bound is sharp: if the beads of each colour lie in one contiguous block, each block needs $k - 1$ cuts.

## Explanations

### L1 human

Thieves steal a necklace with several kinds of jewels and want to share each kind equally, using as few cuts as possible.
With two thieves and $t$ kinds of jewels, $t$ cuts always suffice, wherever the jewels sit.
The surprising proof uses a theorem from topology about maps on spheres.

### L2 human

This is a standard showcase of topological methods in combinatorics, next to Lovász's proof of the Kneser conjecture.
The continuous version, where colours are replaced by measures on an interval, is the form to which Borsuk–Ulam applies directly, much as in the [[ham sandwich theorem|GDXX60SNG5]].
The bound $(k - 1) t$ cannot be lowered in general, as the example of contiguous colour blocks shows.
