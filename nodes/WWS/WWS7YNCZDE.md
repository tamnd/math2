---
tag: WWS7YNCZDE
kind: concept
name: Metapopulation model of Levins
msc: [92D40, 92D25]
specializes: [1YEMFQ1H32]
sources:
  - url: https://en.wikipedia.org/wiki/Metapopulation
---

## Summary

A metapopulation is a set of local populations of one species that live in separate patches of habitat and are linked by migration.
The Levins model, due to Richard Levins, follows only the fraction of patches that are occupied, which changes by colonisation and local extinction.
It predicts that the species persists if and only if the colonisation rate exceeds the extinction rate.
In that case a fixed fraction of patches stays occupied.

## Explanations

### L1 human

Think of frogs living in many ponds.
A pond's frogs can die out, and frogs from other ponds can settle an empty pond.
The Levins model ignores how many frogs a pond has and only asks whether it has frogs at all.
If ponds are settled at rate $c = 0.5$ and lose their frogs at rate $e = 0.1$, in the long run a fraction $1 - e/c = 0.8$ of the ponds has frogs.
If $e \ge c$, the frogs eventually vanish from all ponds.
