---
tag: 2D88FYZ3DZ
kind: concept
name: Barker code
msc: [94A55, 05B20, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Barker_code
same_as:
  wikidata: Q808256
  wikipedia: Barker code
---

## Summary

A Barker code is a finite sequence of $+1$s and $-1$s whose aperiodic autocorrelation at every nonzero shift is $-1$, $0$ or $1$.
Its autocorrelation therefore has one tall peak and very small side values.
This makes it ideal for synchronization and for radar pulse compression with a [[matched filter|M15T6421X2]].
Barker codes are known only for the lengths $2, 3, 4, 5, 7, 11$ and $13$.
See the [[definition|2A8JHA6WT6]].

## Explanations

### L1 human

Take a short pattern of pluses and minuses, slide a copy of it along itself, and at each offset add up the products of the overlapping entries.
For a Barker code, every offset other than zero gives a sum of $-1$, $0$ or $1$, while the zero offset gives the full length.
So the pattern lines up with itself in only one position, and a receiver can locate it precisely in time.
The length-$13$ code $+ + + + + - - + + - + - +$ is the best known one.
It is believed that no longer Barker codes exist.
