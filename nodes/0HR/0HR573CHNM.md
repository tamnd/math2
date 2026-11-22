---
tag: 0HR573CHNM
kind: definition
name: Linear span
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 0DTY8B9HMS
uses: [0JB3DP1BMF, 0EPTJA5QV4]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.span
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2A
inventory: [TJ0X2DJ1E9]
---

## Definition

The linear span of a set of vectors is the set of all vectors that can be built from it by scaling and adding.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $S \subseteq V$.
The *linear span* of $S$ is the set $\operatorname{span}(S)$ of all [[linear combinations|0JB3DP1BMF]] of finitely many vectors of $S$:
$$\operatorname{span}(S) = \{a_1 v_1 + \dots + a_k v_k : k \ge 0, \ a_1, \dots, a_k \in F, \ v_1, \dots, v_k \in S\}.$$
We say that $S$ *spans* $V$ when $\operatorname{span}(S) = V$.

## Remarks

Each part of the definition has a job.
The scalars range over the field $F$, so the span depends on $F$: inside $\mathbb{R}$, the real span of $1$ is $\mathbb{R}$, while the rational span of $1$ is $\mathbb{Q}$.
The number $k$ of vectors is finite, because a vector space has no limits, so only finite sums have a value.
The case $k = 0$ is allowed, so the empty sum $0$ always lies in the span, and $\operatorname{span}(\varnothing) = \{0\}$.

For example, in $\mathbb{R}^3$ the span of $(1, 0, 1)$ and $(0, 1, 1)$ is the plane $z = x + y$, since $a(1, 0, 1) + b(0, 1, 1) = (a, b, a + b)$.
The span of one nonzero vector is a line through the origin.

The span is always a [[linear subspace|0EPTJA5QV4]], and it is the intersection of all subspaces that contain $S$, by [[the smallest subspace theorem|2BX666XF68]].
Mathlib takes that second description as its definition of `Submodule.span F S`, and proves the description by combinations as a lemma.
The [[concept page|0DTY8B9HMS]] works through more examples.

## Explanations

### L1 human

The span of some vectors is everything you can reach from them by scaling and adding.
Two arrows in space that do not lie along one line span a whole plane.

### L2 human

To find the span of $(1, 2)$ and $(2, 4)$ in $\mathbb{R}^2$, notice that $(2, 4) = 2(1, 2)$.
So $a(1, 2) + b(2, 4) = (a + 2b)(1, 2)$, and the span is the line of all multiples of $(1, 2)$.
