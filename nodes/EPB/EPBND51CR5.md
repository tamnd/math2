---
tag: EPBND51CR5
kind: concept
name: Total variation of a measure
msc: [28A10, 28A33]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation
---

## Summary

Let $\nu$ be a [[signed measure|VG2P7R91Z7]] or a [[complex measure|NY6TYHRGMS]].
Its total variation $\abs{\nu}$ is the smallest positive measure with $\abs{\nu(E)} \le \abs{\nu}(E)$ for every set $E$.
It is computed as the supremum of $\sum \abs{\nu(E_i)}$ over partitions of a set into measurable pieces.
For a signed measure it equals $\nu^+ + \nu^-$ from the Jordan decomposition.
The number $\abs{\nu}(X)$ is the total variation norm, which makes the finite signed or complex measures a Banach space.
It extends the [[total variation|8QA5DEWNYD]] of a function to measures.

## Explanations

### L1 human

A signed measure can make a set look small by cancelling positive and negative parts.
The total variation removes this cancellation: it counts all the positive mass and all the negative mass.
For example, on $[-1, 1]$ the signed measure $\nu(E) = \int_E x \, dx$ gives the whole interval measure $0$, but its total variation gives it $\int_{-1}^{1} \abs{x} \, dx = 1$.
