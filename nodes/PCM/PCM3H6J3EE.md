---
tag: PCM3H6J3EE
kind: example
name: Sierpiński carpet
msc: [54F15, 28A80, 54F50]
instance_of: [NJQ196M1WR]
uses: [0TVJZYB6SH, 0V032VWTHD, A3W7RGXXK9]
sources:
  - url: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_carpet
same_as:
  wikidata: Q280081
  wikipedia: Sierpiński carpet
---

## Example

Let $S_0 = [0, 1]^2$.
Divide each square of side $3^{-k}$ in $S_k$ into $9$ equal squares of side $3^{-k-1}$.
Remove the interior of the middle one; the result is $S_{k+1}$.
The *Sierpiński carpet* is $S = \bigcap_{k \ge 0} S_k$.

The set $S$ is a [[continuum|NJQ196M1WR]].
Each $S_k$ is a finite union of closed squares, so it is [[compact|0TVJZYB6SH]].
It is [[connected|0V032VWTHD]], since the $8$ kept squares in each divided square form a ring in which neighbours share an edge.
The intersection of a decreasing sequence of nonempty compact connected sets in the plane is nonempty, compact and connected.

## Remarks

The set $S_k$ consists of $8^k$ squares of area $9^{-k}$, so $S$ has area $\lim_k (8/9)^k = 0$.
Its Hausdorff dimension is $\log 8 / \log 3 \approx 1.893$.
Its [[Lebesgue covering dimension|A3W7RGXXK9]] is $1$.
Sierpiński showed that every compact subset of the plane of dimension at most $1$ embeds in the carpet, so it is a universal plane curve.

## Explanations

### L1 human

Take a square, cut it into a three by three grid, and throw away the middle piece.
Do the same with each of the eight pieces left, and keep going forever.
What remains is a lacy set with holes at every scale.
It has no area, yet it is all in one piece, and it contains a copy of every curve that can be drawn in the plane.
