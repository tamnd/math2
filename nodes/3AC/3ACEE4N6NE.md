---
tag: 3ACEE4N6NE
kind: concept
name: Henselian field
msc: [12J10, 13J15]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Summary

A Henselian field is a [[valued field|B85T5VKR3M]] in which the conclusion of [[Hensel's lemma|010QVB71T2]] holds, see the [[definition|Z3KPTM2YWX]].
In it, a simple root of a polynomial modulo the maximal ideal lifts to a true root.
Its [[valuation ring|QSX12D8RQM]] is a [[Henselian ring|RNXPV3KC5J]].
Complete fields for a discrete valuation, such as the [[p-adic numbers|BT6T702C28]] and [[fields of formal Laurent series|YZWYF7DXTW]], are Henselian.
In a Henselian field the valuation extends in only one way to each algebraic extension, which makes their extension theory clean.

## Explanations

### L1 human

Over the $7$-adic numbers, one can solve $x^2 = 2$ by first solving it modulo $7$ and then correcting the answer step by step.
Modulo $7$, the number $3$ works, since $9 - 2 = 7$.
A field is Henselian when this "solve approximately, then refine" method always works for simple roots.
The rationals with the $7$-adic valuation are not Henselian: the approximate root $3$ exists, but $\sqrt 2$ is not rational.
