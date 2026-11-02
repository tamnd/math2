---
tag: BBYNPDWR5R
kind: example
name: Wang tile
msc: [52C20, 05B45, 37B51]
illustrates: [624XDXX8FN]
uses: [W6ESDYBF8Z, Z7TN2B35B0]
sources:
  - url: https://en.wikipedia.org/wiki/Wang_tile
same_as:
  wikidata: Q474147
  wikipedia: Wang tile
---

## Example

A Wang tile is a unit square whose four edges carry colours from a finite set.
Fix a finite set $W$ of Wang tiles.
A tiling by $W$ is a map $\tau \colon \Z^2 \to W$ such that adjacent edges match.
That is, for each $(i, j)$, the right edge of $\tau(i, j)$ has the colour of the left edge of $\tau(i+1, j)$.
Also the top edge of $\tau(i, j)$ has the colour of the bottom edge of $\tau(i, j+1)$.
Tiles may not be rotated or reflected.

The set of all tilings by $W$ is a two-dimensional [[subshift of finite type|624XDXX8FN]] in $W^{\Z^2}$.
Indeed, its forbidden patterns are the pairs of adjacent tiles whose common edge has two different colours.
There are finitely many of them.

Check of a small case: let $W$ consist of one tile whose four edges all have the colour $a$.
All matching conditions hold, so the constant map is a tiling, and it is periodic.
Now let $W$ consist of one tile with left edge $a$ and right edge $b \ne a$.
Two such tiles can never sit side by side, so $W$ admits no tiling.

## Remarks

The domino problem asks for an algorithm that decides, given $W$, whether $W$ tiles the plane.
Berger proved that no such algorithm exists, by simulating a [[Turing machine|W6ESDYBF8Z]] with Wang tiles and reducing to the [[halting problem|Z7TN2B35B0]].
A key step is the existence of an aperiodic set of Wang tiles: a set that tiles the plane, but only in non-periodic ways.
Jeandel and Rao found an aperiodic set of $11$ Wang tiles and showed that no set with fewer tiles is aperiodic.

## Explanations

### L1 human

Wang tiles are square dominoes with coloured edges, and neighbouring edges must have the same colour.
Some sets of such tiles cover the plane in a repeating pattern, some cannot cover it at all.
Surprisingly, some sets cover the plane but never in a repeating way.
Because of this, no computer program can decide for every set of tiles whether it covers the plane.
