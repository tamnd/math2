---
tag: BNR4H5GCTP
kind: concept
name: Braid group
msc: ["20F36", "57K10"]
specializes: [SAWBDBHE41]
sources:
  - url: https://en.wikipedia.org/wiki/Braid_group
same_as:
  wikidata: Q220409
  wikipedia: Braid group
---

## Summary

The braid group $B_n$ is the [[group|G5S1M9]] of braids with $n$ strands.
Two braids are equal when one can be deformed into the other, and the product places one braid after the other.
Artin gave its presentation with generators $\sigma_1, \ldots, \sigma_{n-1}$, the crossings of neighbouring strands, so $B_n$ is an [[Artin group|SAWBDBHE41]].
It is also the fundamental group of the space of sets of $n$ distinct points in the plane.
It is also the [[mapping class group|JV5NYG913V]] of a disk with $n$ marked points.
Braid groups link algebra with knot theory: by Alexander's theorem, every link is the closure of a braid.

## Explanations

### L1 human

Fix $n$ pegs on a top bar and $n$ pegs on a bottom bar, and join them with $n$ strings that always go downward.
Two such braids are the same if one can be moved into the other without cutting the strings or moving the pegs.
To multiply two braids, hang one below the other.
The basic braid $\sigma_i$ crosses string $i$ over string $i + 1$, and its inverse crosses it back under.
For example, with three strands, $\sigma_1 \sigma_2 \sigma_1$ and $\sigma_2 \sigma_1 \sigma_2$ are the same braid: both reverse the order of the three strings.
