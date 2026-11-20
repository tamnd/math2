---
tag: 0EVHJFTG9Z
kind: definition
name: Linear independence
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 0CRMGPAH83
uses: [0JB3DP1BMF]
formal:
  - system: lean4
    library: mathlib
    decl: LinearIndependent
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2A
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A family $(v_1, \dots, v_k)$ of vectors of $V$ is *linearly independent* when the only [[linear combination|0JB3DP1BMF]] of them that equals $0$ is the trivial one.
This means that
$$a_1 v_1 + \cdots + a_k v_k = 0 \implies a_1 = \cdots = a_k = 0$$
for all $a_1, \dots, a_k \in F$.
An arbitrary family $(v_i)_{i \in I}$ is *linearly independent* when each finite subfamily is linearly independent.
A family that is not linearly independent is *linearly dependent*.
A subset $S \subseteq V$ is linearly independent when the family $(v)_{v \in S}$, indexed by $S$ itself, is linearly independent.

## Remarks

The vectors $(1, 0)$ and $(1, 1)$ in $\R^2$ are linearly independent; the vectors $(1, 2)$ and $(2, 4)$ are linearly dependent.
A family that contains the zero vector, or the same vector twice, is linearly dependent.
A family of at least one vector is linearly dependent if and only if one of its vectors is a linear combination of the others.
See the [[dependence lemma|~ddec9473]].
In $F^n$, a family of more than $n$ vectors is linearly dependent.
The empty family is linearly independent.
Mathlib's `LinearIndependent R v` takes a family `v : ι → M`; for a set `s`, one writes `LinearIndependent R ((↑) : s → M)`.

## Explanations

### L1 human

Vectors are linearly independent when none of them is redundant.
No vector can be built from the others, so each one adds a new direction.
Two arrows in the plane are independent exactly when they do not lie on one line.
