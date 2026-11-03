---
tag: EH7XF8CNFQ
kind: concept
name: Nussinov algorithm
msc: [92C40, 92D20, 90C39]
sources:
  - url: https://en.wikipedia.org/wiki/Nussinov_algorithm
same_as:
  wikidata: Q2005549
  wikipedia: Nussinov algorithm
---

## Summary

The Nussinov algorithm predicts the secondary structure of an RNA molecule.
It maximizes the number of base pairs, subject to the rule that pairs do not cross.
It is a [[dynamic programming|R3FXF08WBH]] method over intervals of the sequence and runs in time proportional to the cube of the length.
It is too crude for accurate prediction, but its recursion is the template for the energy-minimization methods used in practice.

## Explanations

### L1 human

An RNA strand folds back on itself, and its letters pair up: $A$ with $U$, $G$ with $C$, and also $G$ with $U$.
If you draw the strand along a line and each pair as an arc above it, the arcs of a secondary structure never cross.
The Nussinov algorithm finds a non-crossing set of arcs that is as large as possible.
It does so by solving the problem for every stretch of the strand, from short stretches to the whole strand.
For $GGGAAACCC$ it finds the hairpin that pairs the three $G$ with the three $C$.
