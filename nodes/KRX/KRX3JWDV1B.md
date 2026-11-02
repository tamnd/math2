---
tag: KRX3JWDV1B
kind: definition
name: Aperiodic set of prototiles
msc: [52C23, 52C20, 05B45]
defines: Z3FCJZF6WK
uses: [GKJK293DXS, WFRGSBFZGV]
sources:
  - url: https://en.wikipedia.org/wiki/Aperiodic_set_of_prototiles
---

## Definition

Let $n \ge 1$ and let $S$ be a finite set of subsets of $\R^n$, called *prototiles*, possibly together with matching rules on how they may meet.
A tiling of $\R^n$ *by* $S$ is a [[tiling|GKJK293DXS]] in which every tile is congruent to a member of $S$ and the matching rules hold.
The set $S$ is *aperiodic* if:

1. there is a tiling of $\R^n$ by $S$;
2. no tiling of $\R^n$ by $S$ is [[periodic|WFRGSBFZGV]].

## Remarks

Example: the two rhombi of the [[Penrose tiling|MBE83FTRBG]], with their matching rules, form an aperiodic set of prototiles in $\R^2$.

Non-example: the set $S = \set{[0,1]^2}$ consisting of the unit square is not aperiodic.
Clause 1 holds, but the standard grid of unit squares is a periodic tiling by $S$, so clause 2 fails.

A tiling with no nonzero period is called *non-periodic*.
A set of prototiles is aperiodic exactly when it admits tilings and all of them are non-periodic.
The first aperiodic set, found by Robert Berger in 1966, consisted of a very large number of square tiles with coloured edges.
