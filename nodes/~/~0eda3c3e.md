---
tag: ~0eda3c3e
kind: statement
role: theorem
name: Pythagorean theorem
aliases: [pythagoras-theorem]
msc: [51M04]
uses: [~68dd3a3a, ~9f546482, ~5eb2e3e8]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pythagorean_theorem
    locator: Converse
same_as:
  wikidata: Q11518
  wikipedia: Pythagorean theorem
---

## Statement

Let $ABC$ be a [[triangle|~68dd3a3a]] in the Euclidean space $\mathbb{R}^n$. Let $d$ be the [[Euclidean distance|~5eb2e3e8]], and let $\angle ABC$ be the [[angle at $B$|~9f546482]].
Then
$$d(A, C)^2 = d(A, B)^2 + d(B, C)^2$$
if and only if $\angle ABC = \pi / 2$.

## Remarks

The direction "if" is the classical theorem: in a right triangle, the square of the hypotenuse is the sum of the squares of the legs, $a^2 + b^2 = c^2$. The direction "only if" is its converse.
In vector form: for vectors $u$ and $v$ with $u \cdot v = 0$, $\|u + v\|^2 = \|u\|^2 + \|v\|^2$.
The theorem is the special case $\gamma = \pi / 2$ of the [[law of cosines|~39817e5a]].
Mathlib states the equivalence for all points $A$, $B$ and $C$, with its convention for the angle at a repeated point.

## History

The theorem carries the name of the Greek philosopher Pythagoras. Euclid's Elements proves it as Proposition 47 of Book I, and the converse as Proposition 48.

## Explanations

### L1 human

Build a square on each side of a right triangle. The two small squares together have the same area as the big square on the longest side. For the sides $3$, $4$ and $5$: $9 + 16 = 25$.
