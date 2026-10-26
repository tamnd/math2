---
tag: 0ZJM9D7NPS
kind: statement
role: theorem
name: Canonical isomorphism with the double dual
msc: [15A04]
uses: [0M856Q1AMZ, 00889YD15K]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Injection into the double-dual
---

## Statement

Let $F$ be a field and let $V$ be a vector space over $F$.
Let $V^{**} = (V^*)^*$ be the dual of the [[dual space|07JBSZE0V4]].
The *evaluation map* $\operatorname{ev} \colon V \to V^{**}$ is defined by $\operatorname{ev}(v)(f) = f(v)$ for $v \in V$ and $f \in V^*$.
This map is linear and injective.
If $V$ is finite-dimensional, then $\operatorname{ev}$ is an isomorphism.

## Remarks

The evaluation map does not depend on a choice of basis, so it is called *canonical* or *natural*.
In finite dimensions, it is an isomorphism because it is injective and $\dim V^{**} = \dim V^* = \dim V$.
For infinite-dimensional $V$, the evaluation map is not surjective.

## Explanations

### L1 human

A vector $v$ can act on linear forms: it sends each form $f$ to the number $f(v)$.
This turns each vector into an element of the double dual.
In finite dimensions, every element of the double dual comes from exactly one vector in this way.
