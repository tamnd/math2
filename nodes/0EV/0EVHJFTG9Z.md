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

A family of vectors is linearly independent when the zero vector can be written as a combination of it in only one way, with all coefficients zero.
Let $F$ be a field and let $V$ be a vector space over $F$.
A finite family $(v_1, \dots, v_k)$ of vectors of $V$ is *linearly independent* when, for all $a_1, \dots, a_k \in F$,
$$a_1 v_1 + \dots + a_k v_k = 0 \implies a_1 = \dots = a_k = 0.$$
In words, the only [[linear combination|0JB3DP1BMF]] of the family with value $0$ is the trivial one.
A family $(v_i)_{i \in I}$ with any index set $I$ is *linearly independent* when every finite subfamily is linearly independent.
A family that is not linearly independent is *linearly dependent*.
A subset $S \subseteq V$ is *linearly independent* when the family $(v)_{v \in S}$, indexed by $S$ itself, is linearly independent.

## Remarks

The condition is an implication, and its direction is the point.
The trivial combination always has value $0$, so the definition asks that no other combination does.
For $(1, 0)$ and $(1, 1)$, the equation $a(1, 0) + b(1, 1) = (a + b, b) = (0, 0)$ forces $b = 0$ and then $a = 0$, so the family is independent.
For $(1, 2)$ and $(2, 4)$, the relation $2(1, 2) - (2, 4) = 0$ has nonzero coefficients, so the family is dependent.

The infinite case uses finite subfamilies because a linear combination may involve only finitely many vectors.
For example, the monomials $1, x, x^2, \dots$ in $F[x]$ are independent, since every finite set of them is.

The definition is for families, which may repeat a vector.
The family $(v, v)$ is dependent, by $1v - 1v = 0$, while the subset $\{v\}$ is independent when $v \ne 0$.
Mathlib's `LinearIndependent F v` takes a family `v : ι → V`, and a set `s` is independent when the family of its elements, `LinearIndependent F ((↑) : s → V)`, is.

The empty family is independent, since its only combination is the empty one.
Every family that contains $0$ is dependent.
The [[concept page|0CRMGPAH83]] gives the tests by pivots and by determinants, and the [[dependence lemma|H75GS7QVPB]] gives the form "no vector is a combination of the others".

## Explanations

### L1 human

Vectors are independent when none of them can be built from the others.
Two arrows in the plane are independent exactly when they do not lie on one line.

### L2 human

To test $1 + x$ and $1 - x$ in the polynomials, set $a(1 + x) + b(1 - x) = 0$.
Collecting terms gives $(a + b) + (a - b)x = 0$, so $a + b = 0$ and $a - b = 0$, and then $a = b = 0$.
So the two polynomials are independent.
