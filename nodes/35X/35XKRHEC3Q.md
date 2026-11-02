---
tag: 35XKRHEC3Q
kind: concept
name: Hyponormal operator
msc: [47B20]
sources:
  - url: https://en.wikipedia.org/wiki/Hyponormal_operator
same_as:
  wikidata: Q5959976
  wikipedia: Hyponormal operator
---

## Summary

A hyponormal operator is a bounded operator $T$ on a Hilbert space with $T^*T - TT^* \ge 0$, equivalently $\norm{T^*x} \le \norm{Tx}$ for all $x$.
The class contains the normal operators and the [[subnormal operators|81MZ023K1A]], and it is strictly larger than both.
Hyponormal operators share several properties of normal operators: for instance, the norm equals the spectral radius.

## Explanations

### L1 human

For a normal operator, $T$ and its adjoint stretch every vector by the same amount.
A hyponormal operator only requires that the adjoint stretches no vector more than $T$ does.
The unilateral shift on sequences is an example: it keeps every length, while its adjoint, the backward shift, shortens the vector $(1, 0, 0, \ldots)$ to $0$.
