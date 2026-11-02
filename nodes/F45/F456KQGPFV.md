---
tag: F456KQGPFV
kind: statement
role: theorem
name: Einstein problem
msc: [52C23, 52C20, 05B45]
uses: [GKJK293DXS, WFRGSBFZGV, Z3FCJZF6WK]
about: [Z3FCJZF6WK]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein_problem
same_as:
  wikidata: Q18204561
  wikipedia: Einstein problem
---

## Statement

There is a single closed topological disk $T$ in the plane $\R^2$ with the following two properties.

1. The plane has a [[tiling|GKJK293DXS]] in which every tile is congruent to $T$.
2. No tiling of the plane in which every tile is congruent to $T$ is [[periodic|WFRGSBFZGV]].

In other words, the one-element set $\set{T}$ is an [[aperiodic set of prototiles|Z3FCJZF6WK]], and $T$ is called an *aperiodic monotile* or *einstein*.

## Remarks

The question whether one tile can be aperiodic, with no matching rules, is the einstein problem; the name plays on the German "ein Stein", one stone.
David Smith, Joseph Samuel Myers, Craig S. Kaplan and Chaim Goodman-Strauss answered it in 2023 with the "hat", a polygon made of eight kites with angles $60^\circ, 90^\circ, 120^\circ, 90^\circ$.
Tilings by the hat use both the hat and its mirror image.
The same authors later found the "spectre", which tiles the plane only non-periodically even when only rotations and translations are allowed.
The proof groups the tiles of any hat tiling into larger clusters that again form a tiling of the same kind.
This hierarchical structure at all scales rules out periods.

## Explanations

### L1 human

For a long time people asked whether one single shape could cover the whole plane, but only in patterns that never repeat.
Two shapes were known to do it, such as the Penrose tiles.
In 2023 an amateur, David Smith, found a single shape, called the hat, that does it.
Any tiling by hats is forced to be non-repeating.

### L2 human

Aperiodic sets of prototiles had shrunk from Berger's huge set of tiles in 1966 to the two Penrose tiles in the 1970s.
The einstein problem asked whether the number can be $1$.
The hat solves it if reflections are allowed, and the spectre solves it even with rotations and translations only.
The key technique, as for Penrose tilings, is a substitution: tilings are built from clusters that copy the structure on a larger scale.
