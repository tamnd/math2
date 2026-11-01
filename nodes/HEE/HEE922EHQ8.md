---
tag: HEE922EHQ8
kind: concept
name: Residually finite group
msc: ["20E26"]
specializes: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Residually_finite_group
same_as:
  wikidata: Q3777935
  wikipedia: Residually finite group
---

## Summary

A [[group|G5S1M9]] is residually finite if every element other than the identity survives in some finite quotient.
So the group can be studied through its finite images, which separate all its elements.
[[Free groups|0KTW26C80J]], finitely generated abelian groups and finitely generated subgroups of $GL(n, \C)$ are residually finite.
A finitely generated residually finite group is [[Hopfian|PHEN4E1JPT]], and a finitely presented residually finite group has solvable word problem.

## Explanations

### L1 human

To see that an element $g$ is not the identity, map the group onto a finite group and look at the image of $g$.
In a residually finite group this always works for a suitable finite group.
For example, the integer $n \ne 0$ survives in $\Z / (\abs{n} + 1)$, since $0 < \abs{n} < \abs{n} + 1$.
The group of rational numbers fails badly: it has no finite quotient except the trivial one.
