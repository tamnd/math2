---
tag: V6TJAFZ4MD
kind: concept
name: p-adic integer
msc: [12J25, 11S99]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_number
---

## Summary

The $p$-adic integers are the [[p-adic numbers|BT6T702C28]] $x$ with $\abs{x}_p \le 1$.
They form a ring $\Z_p$, which is a [[discrete valuation ring|MGM3CNJW9V]] with maximal ideal $p\Z_p$ and residue field $\F_p$.
The ring $\Z_p$ is compact, and it is the inverse limit of the rings $\Z / p^n \Z$.
It holds, in one object, the information of all congruences modulo powers of $p$.

## Explanations

### L1 human

A $p$-adic integer is a base $p$ expansion $a_0 + a_1 p + a_2 p^2 + \cdots$ that goes on forever to the left.
Cutting it after $n$ digits gives a residue modulo $p^n$, and these residues fit together.
Every ordinary integer is a $p$-adic integer, and so is every fraction whose denominator is not divisible by $p$.
For example, $1/2$ is a $3$-adic integer, but $1/3$ is not.
