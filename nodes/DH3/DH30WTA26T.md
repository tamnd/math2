---
tag: DH30WTA26T
kind: concept
name: Term evaluation
msc: [08A40, 03C07]
sources:
  - url: https://en.wikipedia.org/wiki/Term_(logic)
---

## Summary

Term evaluation computes the value of a [[term|6D3WA7N2W4]] in an algebra once each variable has been given a value.
The value is defined by recursion on the term.
Variables take their assigned values, and a function symbol applied to subterms is computed with the matching operation of the algebra.
It is the bridge between syntax and algebra: identities, term operations and the free algebras of a variety are all defined through it.

## Explanations

### L1 human

A term such as $x \cdot (y + 1)$ is only a formula on paper.
To evaluate it in the ring of integers, choose numbers for the variables, say $x = 3$ and $y = 4$.
Then compute from the inside out: $y + 1 = 5$, and $x \cdot 5 = 15$.
The same term evaluated in the ring $\Z/7\Z$ with the same choices gives $1$, so the value depends on the algebra as well as on the assignment.
