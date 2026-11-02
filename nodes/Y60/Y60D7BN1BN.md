---
tag: Y60D7BN1BN
kind: statement
role: theorem
name: Generic flatness
msc: [14A15, 14B25]
uses: [JXRKH6P1Z4, 17NVR4XBHK, ND6XEY68P4, AHTE5DVX61, 5M6KS8F47R]
about: [5M6KS8F47R]
sources:
  - url: https://en.wikipedia.org/wiki/Generic_flatness
same_as:
  wikidata: Q5532671
  wikipedia: Generic flatness
---

## Statement

Let $Y$ be an [[integral scheme|17NVR4XBHK]] that is [[Noetherian|ND6XEY68P4]].
Let $f \colon X \to Y$ be a [[morphism|JXRKH6P1Z4]] [[of finite type|AHTE5DVX61]].
Then there is a nonempty open subset $U \subseteq Y$ such that the restriction $f^{-1}(U) \to U$ is [[flat|5M6KS8F47R]].

## Remarks

The statement reduces to the affine case and to the generic freeness lemma.
That lemma says the following: let $A$ be a Noetherian domain, $B$ a finitely generated $A$-algebra, and $M$ a finitely generated $B$-module.
Then there is a nonzero $a \in A$ such that $M_a$ is a free $A_a$-module.
Its proof uses Noether normalization over the fraction field of $A$ and induction on dimension.
For example, the blow-up of $\mathbb{A}^2_k$ at the origin is flat over $U = \mathbb{A}^2_k \setminus \set{0}$, where it is an isomorphism.
The integrality of $Y$ cannot be dropped.
For $Y = \operatorname{Spec} k[\varepsilon]/(\varepsilon^2)$ and the closed immersion $\operatorname{Spec} k \to Y$, the only nonempty open subset of $Y$ is $Y$, and $k$ is not flat over $k[\varepsilon]/(\varepsilon^2)$.
The same proof gives a sheaf version: a coherent sheaf on $X$ is flat over $Y$ above some nonempty open subset of $Y$.

## Explanations

### L1 human

A family of spaces can behave badly over some special points of the base.
Generic flatness says that this bad behaviour is confined to a proper closed subset.
Over a dense open part of the base, the family is flat, so its fibres vary in a controlled way.

### L2 human

Generic flatness is the starting point of many stratification arguments.
One applies it on $Y$, then again on the closed complement with its reduced structure, and so on; Noetherian induction ends the process.
The result is a finite partition of $Y$ into locally closed pieces over each of which $f$ is flat.
This is how one builds flattening stratifications and proves that Hilbert polynomials of fibres take finitely many values.
The theorem also gives a quick proof of Chevalley's theorem on constructible sets.
