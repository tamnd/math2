---
tag: WGN82TCEF2
kind: concept
name: p-adic absolute value
msc: [12J25, 11S99]
specializes: [1H5F1BP6XS]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_valuation
---

## Summary

For a prime $p$, the $p$-adic absolute value of a nonzero rational number $x$ is $\abs{x}_p = p^{-v_p(x)}$, where $v_p$ is the [[p-adic valuation|03HDF50VN4]].
It is a [[non-Archimedean absolute value|1H5F1BP6XS]] on $\Q$.
Completing $\Q$ for it gives the field of [[p-adic numbers|BT6T702C28]].
Together with the usual [[absolute value|0FFXKTKKQC]], these are all the nontrivial absolute values on $\Q$ up to equivalence.

## Explanations

### L1 human

The $p$-adic absolute value measures how divisible a number is by $p$.
The more factors of $p$ a number has, the smaller its $p$-adic size.
For example, $\abs{12}_2 = 1/4$ because $12 = 2^2 \cdot 3$, and $\abs{3/8}_2 = 8$ because $8 = 2^3$ is in the denominator.
Numbers not divisible by $p$, in numerator or denominator, have size $1$.
