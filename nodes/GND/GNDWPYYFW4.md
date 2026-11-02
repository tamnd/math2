---
tag: GNDWPYYFW4
kind: concept
name: IEEE 754 standard
msc: [65Y04, 65G50]
specializes: [RTKRSC3KPH]
sources:
  - url: https://en.wikipedia.org/wiki/IEEE_754
same_as:
  wikidata: Q828287
  wikipedia: IEEE 754
---

## Summary

IEEE 754 is the technical standard for [[floating-point arithmetic|RTKRSC3KPH]] used by almost all modern processors.
It fixes the binary formats, such as single precision and double precision, and how their bits encode sign, exponent and significand.
It requires the basic operations to be correctly rounded, and it defines special values: signed zeros, infinities, NaN and [[subnormal numbers|DHXXSN12JC]].
Because of it, the same floating-point program gives the same results on different machines, which makes error analysis portable.

## Explanations

### L1 human

Before the standard, each computer maker had its own way of storing real numbers, and the same program could give different answers on different machines.
IEEE 754 is the agreement that settled this.
A double-precision number uses $64$ bits: $1$ bit for the sign, $11$ bits for the exponent and $52$ bits for the fraction.
This gives about $16$ significant decimal digits and numbers up to about $1.8 \times 10^{308}$.
It also says what $1/0$ is (infinity) and what $0/0$ is (NaN, "not a number"), so a computation does not simply crash.
