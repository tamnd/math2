---
tag: EGKVP4KK6V
kind: definition
name: Abelian scheme
msc: [14K05, 14K10, 14L15]
defines: JDDXZ89N33
uses: [TJ04VQP4NB, EXKGG9X6J0, 9537RKBZPP, R7W03TXRS9]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_variety
---

## Definition

Let $S$ be a scheme.
An *abelian scheme* over $S$ is a [[group scheme|TJ04VQP4NB]] $\pi \colon A \to S$ such that:

1. $\pi$ is [[smooth|EXKGG9X6J0]];
2. $\pi$ is [[proper|9537RKBZPP]];
3. every fibre of $\pi$ is geometrically connected.

## Remarks

For each point $s \in S$, the fibre $A_s$ is an [[abelian variety|R7W03TXRS9]] over the residue field $\kappa(s)$.
An abelian scheme over $\operatorname{Spec} k$, for a field $k$, is the same as an abelian variety over $k$.
The group law of an abelian scheme is commutative.

Example: let $S = \operatorname{Spec} \Z[1/2]$ and let $E \subseteq \mathbb{P}^2_S$ be the closure of $y^2 = x^3 - x$, with unit section the point at infinity.
The discriminant of this Weierstrass equation is $64 = 2^6$, a unit on $S$.
So every fibre is a smooth curve of genus $1$, and $E$ is an abelian scheme of relative dimension $1$.

Non-example: the same equation over $\operatorname{Spec} \Z$ fails clause 1.
Modulo $2$, the curve $y^2 = x^3 + x$ is singular at the point $(1, 0)$, where both partial derivatives $2y$ and $3x^2 + 1$ vanish.
