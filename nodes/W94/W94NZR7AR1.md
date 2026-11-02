---
tag: W94NZR7AR1
kind: example
name: Besicovitch set of measure zero
msc: [28A75, 42B99]
instance_of: [6PEN7AKC7M]
uses: [2Z2QVWZ262, 8J8AW0TG9M, 0R0T1VWH5X]
sources:
  - url: https://en.wikipedia.org/wiki/Kakeya_set
    locator: Besicovitch sets of measure zero
---

## Example

There is a [[Kakeya set|6PEN7AKC7M]] in $\R^2$ of [[Lebesgue measure|2Z2QVWZ262]] zero.
Besicovitch first showed this; the construction below, with Cantor sets, is due to Jean-Pierre Kahane.

Let $C \subseteq [0, 1]$ be the set of numbers $\sum_{i \ge 1} a_i 4^{-i}$ with every digit $a_i \in \set{0, 3}$.
It is the Cantor set obtained by keeping the first and last quarter of each interval.
Let $E$ be the union of all line segments from $(x, 0)$ to $(y/2, 1)$ with $x, y \in C$.

1. $E$ is compact, as the image of the compact set $C \times C \times [0, 1]$ under a continuous map.
2. $E$ contains segments of every slope in a range of directions. The horizontal shift $y/2 - x$ of such a segment has base-$4$ digits $b/2 - a$ with $a, b \in \set{0, 3}$, that is $\frac{3}{2} d$ with $d \in \set{-2, -1, 0, 1}$. Since $\set{-2, -1, 0, 1}$ is a full set of residues modulo $4$, the shifts fill the interval $[-1, 1/2]$. So $E$ contains a segment from height $0$ to height $1$, of length at least $1$, in each direction $(s, 1)$ with $-1 \le s \le 1/2$.
3. $E$ has measure zero. Its horizontal slice at height $t \in (0, 1)$ is $\set{(1 - t)x + t y/2 : x, y \in C}$. Up to scaling, this is the projection of the four-corner Cantor set $C \times C$ onto a line whose direction depends smoothly and injectively on $t$. The set $C \times C$ has finite and positive one-dimensional Hausdorff measure and is purely unrectifiable. By the [[Besicovitch–Federer projection theorem|8J8AW0TG9M]], almost all of its projections have length zero. So almost every slice has length zero, and [[Fubini's theorem|0R0T1VWH5X]] gives that $E$ has area zero.

The directions $(s, 1)$ with $-1 \le s \le 1/2$ fill an arc of angle $\pi/4 + \arctan(1/2)$, which is more than $\pi/3$.
So three rotated copies of $E$ contain unit segments in all directions.
Their union is compact, has measure zero, and is a Kakeya set.

## Explanations

### L1 human

One can find a set in the plane that contains a needle of length one pointing in every direction and yet has area zero.
Here the set is made of all segments joining two thin Cantor dusts on two parallel lines.
The dust is so thin that each horizontal line meets the set in a set of length zero, yet the segments point in a whole range of directions.
Three rotated copies then cover every direction.
