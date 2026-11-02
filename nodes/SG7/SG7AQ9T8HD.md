---
tag: SG7AQ9T8HD
kind: concept
name: Ore localization
msc: [16U20, 16S85]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_condition
---

## Summary

Ore localization builds a ring of fractions $R S^{-1}$ of a noncommutative [[ring|0B1261B5ED]] $R$.
In it the elements of a chosen set $S$ become units, and every element has the form $a s^{-1}$.
It exists when $S$ satisfies the [[Ore condition|TJP4ARC2X7]] together with a reversibility condition.
It extends the commutative [[localization|4C1AE84N5N]] and is the main tool to build division rings of fractions of noncommutative domains and [[classical rings of quotients|C5971PGKPH]].

## Explanations

### L1 human

From the integers one builds the rationals by allowing division by nonzero integers.
Ore localization does the same for a noncommutative ring, but only on one side: every new element is a fraction $a s^{-1}$ with the denominator on the right.
For this to give a ring, one must be able to rewrite $s^{-1} a$ as some $b t^{-1}$, and this is what the Ore condition guarantees.
For example, the polynomial ring $k[x]$ over a field localizes to the field $k(x)$ of rational functions, and the [[Weyl algebra|98QE7KY55W]] localizes to a division ring.
