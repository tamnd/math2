---
tag: Z3VCZYHPKY
kind: concept
name: Current algebra
msc: [17B65, 81R10]
specializes: [5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Current_algebra
---

## Summary

A current algebra is a [[Lie algebra|5JJYBJ6A8K]] of maps from a space into a fixed Lie algebra $\mathfrak{g}$, with the bracket taken pointwise.
Algebraically it is the tensor product $\mathfrak{g} \otimes A$ of $\mathfrak{g}$ with a commutative algebra $A$ of functions.
The name comes from quantum field theory, where the commutation relations of current operators take this form.
[[Loop algebras|YJFGP89JYD]], where $A$ is the ring of Laurent polynomials, are the most important case.

## Explanations

### L1 human

Fix a Lie algebra $\mathfrak{g}$, for example the $2 \times 2$ matrices of trace zero.
A current is a rule that attaches an element of $\mathfrak{g}$ to every point of a space, varying nicely from point to point.
Two currents are bracketed point by point, so the currents form a Lie algebra again, now of infinite dimension in most cases.
For example, polynomial curves $t \mapsto x_0 + t x_1 + t^2 x_2$ in $\mathfrak{g}$ form the current algebra $\mathfrak{g} \otimes \C[t]$.
