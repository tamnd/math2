---
tag: TDQ7AXGM6P
kind: concept
name: Polynomial hierarchy
msc: [68Q15, 03D15]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_hierarchy
same_as:
  wikidata: Q2103021
  wikipedia: Polynomial hierarchy
---

## Summary

The polynomial hierarchy is an infinite tower of complexity classes $\Sigma_k^p$ and $\Pi_k^p$, one pair for each $k \ge 0$.
Its first levels are [[P|GVT2NKN37K]], [[NP|QQRA9GBW51]] and [[co-NP|5HWR2NK8N1]], and level $k$ allows $k$ alternating quantifiers over polynomial-size witnesses.
The whole hierarchy lies inside [[PSPACE|T9NTRY93ZT]].
Many conditional results in complexity theory take the form "unless the polynomial hierarchy collapses".

## Explanations

### L1 human

NP problems ask whether some short certificate exists, like a satisfying assignment.
Higher levels ask nested questions, such as whether there is a small circuit that, for every input, agrees with a given formula.
Each extra switch between "there is" and "for every" gives a new level.
It is believed that every level is strictly larger than the one below.
If two consecutive levels were equal, all higher levels would fall down to them; this is called a collapse.
