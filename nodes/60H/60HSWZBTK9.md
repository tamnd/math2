---
tag: 60HSWZBTK9
kind: concept
name: Generator of a semigroup
msc: [47D06, 47D03]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Summary

The generator of a [[strongly continuous semigroup|EVF180QJXY]] $(T(t))_{t \ge 0}$ of operators is the derivative of $T(t)$ at $t = 0$.
It is usually an unbounded, closed, densely defined operator $A$.
The semigroup solves the abstract Cauchy problem $u'(t) = Au(t)$, $u(0) = x$, through $u(t) = T(t)x$, and one writes $T(t) = e^{tA}$.
The generator determines the semigroup uniquely, so questions about evolution equations become questions about one operator.

## Explanations

### L1 human

For a number $a$, the function $t \mapsto e^{ta}$ has derivative $a$ at $t = 0$.
A semigroup is a family of operators that behaves like $e^{ta}$, and its generator plays the role of $a$.
For the heat equation, the semigroup moves an initial temperature forward in time, and the generator is the Laplacian.
For the shift $(T(t)f)(s) = f(s + t)$, the generator is the derivative $d/ds$.
The generator is often a differential operator, which is why it is defined only on a dense set of nice vectors.
