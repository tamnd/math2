---
tag: 0HR573CHNM
kind: definition
name: Linear span
msc: [15A03]
defines: 0DTY8B9HMS
uses: [0JB3DP1BMF, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: Definition
inventory: [TJ0X2DJ1E9]
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $S \subseteq V$.
The *linear span* of $S$ is the set $\operatorname{span}(S)$ of all [[linear combinations|0V8F3E48E6]] of finitely many vectors of $S$:
$$\operatorname{span}(S) = \{a_1 v_1 + \cdots + a_k v_k : k \ge 0, \ a_i \in F, \ v_i \in S\}.$$

## Remarks

The span is a [[linear subspace|00YC1D652K]] of $V$, and it is the intersection of all subspaces of $V$ that contain $S$.
The span of the empty set is $\{0\}$.
In $\R^3$, the span of one nonzero vector is a line through the origin.
The span of two non-parallel vectors is a plane through the origin.

## Explanations

### L1 human

The span of some vectors is everything we can reach from them by scaling and adding.
Two arrows in space that do not point along the same line span a whole plane.
The span is always a subspace.
