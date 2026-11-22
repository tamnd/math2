---
tag: 0BJKVF90Z6
kind: definition
name: Spanning set
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 088RYKAWK9
uses: [0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2A
---

## Definition

A spanning set of a vector space is a set of vectors from which every vector of the space can be built.
Let $F$ be a field and let $V$ be a vector space over $F$.
A subset $S \subseteq V$ is a *spanning set* of $V$, and $S$ *spans* $V$, when
$$\operatorname{span}(S) = V,$$
where $\operatorname{span}$ is the [[linear span|0HR573CHNM]].
Equivalently, for every $v \in V$ there are finitely many vectors $s_1, \dots, s_k \in S$ and scalars $a_1, \dots, a_k \in F$ with $v = a_1 s_1 + \dots + a_k s_k$.

## Remarks

The definition asks for equality with $V$, and one inclusion is free: $\operatorname{span}(S) \subseteq V$ always holds, since $V$ is closed under the operations.
So to show that $S$ spans, you only show that every vector of $V$ is a combination of vectors of $S$.

For example, $(1, 0)$, $(0, 1)$ and $(1, 1)$ span $\mathbb{R}^2$, because $(a, b) = a(1, 0) + b(0, 1)$, and the third vector may get the coefficient $0$.
In contrast, $(1, 2)$ and $(2, 4)$ fail, because all their combinations lie on the line $y = 2x$.
The empty set spans the zero space, since its span is $\{0\}$.

A spanning set that is also linearly independent is a [[basis|0KCQ9Y3QKA]], and [[every spanning set contains a basis|06MRNP4BNT]].
A space with a finite spanning set is [[finite-dimensional|0ZHWKQMVX5]].
In Mathlib, "$S$ spans $V$" is the statement `Submodule.span F S = ⊤`.
The [[concept page|088RYKAWK9]] gives the pivot test and more examples.

## Explanations

### L1 human

A spanning set is a kit of building blocks from which you can make every vector of the space.
It may hold more blocks than you need.

### L2 human

To see that $(1, 1)$ and $(1, -1)$ span $\mathbb{R}^2$, solve $a(1, 1) + b(1, -1) = (x, y)$.
This gives $a = \tfrac{x + y}{2}$ and $b = \tfrac{x - y}{2}$, which exist for every $x$ and $y$.
