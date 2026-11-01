---
tag: PWNZQVQ175
kind: concept
name: Perfect closure
msc: [12F15]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_field
---

## Summary

The perfect closure of a field $K$ of characteristic $p > 0$ is the smallest [[perfect field|VWBVKT794W]] that contains $K$ inside an algebraic closure.
It is obtained by adjoining all $p^n$-th roots of all elements of $K$, so it is a [[purely inseparable extension|966GNVGB8A]] of $K$.
It is the purely inseparable counterpart of the [[separable closure|JJ91A1V8NQ]].
For a perfect field, and for any field of characteristic $0$, the perfect closure is the field itself.

## Explanations

### L1 human

A field of characteristic $p$ is perfect when every element has a $p$-th root.
If some roots are missing, add them, then add their $p$-th roots, and so on forever.
The union of all these steps is the perfect closure.
For $\F_p(t)$ one adds $t^{1/p}$, then $t^{1/p^2}$, and so on.
The result is the union of the fields $\F_p(t^{1/p^n})$ for $n \ge 0$.
