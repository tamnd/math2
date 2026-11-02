---
tag: C72RBH0CDR
kind: concept
name: Proof-theoretic ordinal
msc: ["03F15", "03F30"]
specializes: [0YSCSX5YZC]
uses: [0YSCSX5YZC, 0QFT7Z76N5, 0ZHQMQ2C1N, KT50SMH3EC]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
---

## Summary

The proof-theoretic ordinal of a formal theory measures how much [[transfinite induction|0ZHQMQ2C1N]] the theory can prove.
It is the supremum of the order types of the computable well-orderings that the theory proves to be well-founded.
It is a countable [[ordinal|0YSCSX5YZC]], and it gives a scale on which theories can be compared by strength.
For [[Peano arithmetic|0QFT7Z76N5]] it is [[epsilon nought|KT50SMH3EC]].

## Explanations

### L1 human

Some orderings of the natural numbers are well-orderings: every decreasing sequence in them stops.
A theory can prove this for some such orderings and not for others.
The longest orderings that the theory still trusts give an ordinal, its proof-theoretic ordinal.
A stronger theory trusts longer orderings, so it gets a larger ordinal.
For example, Peano arithmetic trusts each ordering shorter than $\varepsilon_0$, but not the ordering of length $\varepsilon_0$ itself.
