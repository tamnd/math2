---
tag: QPRHC4DZ20
kind: example
name: Space-filling curve
msc: [54C05, 54F15]
illustrates: [Q5QFYKD004]
uses: [0X3WGX95FE, 01RVCMSN5N, 0BXNDZFQME]
sources:
  - url: https://en.wikipedia.org/wiki/Space-filling_curve
same_as:
  wikidata: Q567843
  wikipedia: Space-filling curve
---

## Example

A *space-filling curve* is a [[continuous|0X3WGX95FE]] [[surjection|01RVCMSN5N]] from $[0, 1]$ onto the square $[0, 1]^2$.
Here is one, due to Lebesgue.
Each point $x$ of the [[Cantor set|0BXNDZFQME]] $C$ has a unique expansion $x = \sum_{n \ge 1} 2 a_n 3^{-n}$ with digits $a_n \in \set{0, 1}$.
Set
$$f(x) = \left( \sum_{n \ge 1} a_{2n-1} 2^{-n}, \ \sum_{n \ge 1} a_{2n} 2^{-n} \right).$$
On each open interval removed in the construction of $C$, extend $f$ linearly between its values at the two ends.

The check has three steps.
The map $f$ is onto.
Take binary expansions of both coordinates of a point of $[0, 1]^2$; interleaving their digits gives a point of $C$ that $f$ sends to it.
The map $f$ is continuous on $C$.
Two points of $C$ less than $3^{-2m}$ apart share their first $2m$ digits, so their images differ by at most $2^{-m}$ in each coordinate.
The two ends of a removed interval of length $3^{-k}$ share their first $k - 1$ digits.
So short removed intervals carry small linear pieces, and the extended map is continuous.

## Remarks

No space-filling curve is injective.
A continuous bijection $[0, 1] \to [0, 1]^2$ would be a homeomorphism, since $[0, 1]$ is compact and the square is Hausdorff.
That is impossible: removing an inner point disconnects $[0, 1]$, but removing a point does not disconnect the square.
The first space-filling curve was found by Peano, and Hilbert gave another one.

## Explanations

### L1 human

A space-filling curve is a pencil line drawn without lifting the pencil, in a finite time, that passes through every point of a filled square.
It comes as the limit of ever finer zigzag paths.
The curve must cross itself: it passes through some points more than once.
