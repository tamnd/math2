---
tag: TJP4ARC2X7
kind: concept
name: Ore condition
msc: [16U20, 16S85]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_condition
same_as:
  wikidata: Q986499
  wikipedia: Ore condition
---

## Summary

The Ore condition is a condition on a [[multiplicative set|AN9SKEZ3VY]] $S$ of a noncommutative [[ring|0B1261B5ED]].
It allows one to form fractions $a s^{-1}$ with denominators in $S$.
It asks that a "left fraction" $s^{-1} a$ can always be rewritten as a "right fraction" $b t^{-1}$.
Together with a mild cancellation condition, it is exactly what is needed for the [[Ore localization|SG7AQ9T8HD]] to exist.
For commutative rings it always holds, so it explains why ordinary [[localization|4C1AE84N5N]] needs no extra hypothesis.

## Explanations

### L1 human

In a commutative ring, $a / s$ means the same thing whether you divide on the left or on the right.
In a noncommutative ring, $s^{-1} a$ and $a s^{-1}$ are different, and products of fractions must again be fractions of one kind.
To multiply $a s^{-1}$ by $b t^{-1}$ one needs to move $s^{-1}$ past $b$, that is, to write $s^{-1} b$ as $c u^{-1}$.
The Ore condition says that this is always possible.
For example, in the ring of polynomials $k[x]$ every nonzero polynomial can serve as a denominator, but in the free algebra $k\langle x, y \rangle$ the nonzero elements cannot.
