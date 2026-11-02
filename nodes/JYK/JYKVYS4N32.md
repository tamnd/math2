---
tag: JYKVYS4N32
kind: concept
name: Kauffman bracket
msc: [57K14]
sources:
  - url: https://en.wikipedia.org/wiki/Bracket_polynomial
same_as:
  wikidata: Q4953698
  wikipedia: Bracket polynomial
---

## Summary

The Kauffman bracket is a Laurent polynomial in one variable $A$ attached to an unoriented diagram of a [[link|1A5WRCNTM3]].
It is computed by smoothing every crossing in the two possible ways and counting the circles that result.
It is unchanged by the second and third [[Reidemeister moves|T3HAGWYKK7]] and changes by a simple factor under the first.
After a correction by the writhe, it gives the [[Jones polynomial|4SPC17FPXE]].

## Explanations

### L1 human

At each crossing of a knot drawing you can cut and reconnect the strands in two ways, so that the crossing disappears.
Doing this at every crossing leaves a set of disjoint circles.
The bracket adds up all the ways to do this, with a weight that depends on how many smoothings of each type you chose and how many circles you got.
It is a recipe that turns any diagram into a polynomial by simple counting.
