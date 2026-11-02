---
tag: 6HAZ0AKKAR
kind: definition
name: Frame
msc: [06D22, 18F70]
defines: 306PWGH7BF
uses: [D7A0ZGZT5S, 0HM0HQCK6N, NG943XNQWH, 02BH3MCBQB, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Heyting_algebra
---

## Definition

Let $L$ be a [[complete lattice|D7A0ZGZT5S]].
It is a *frame* if for every $a \in L$ and every family $(b_i)_{i \in I}$ of elements of $L$,
$$a \wedge \bigvee_{i \in I} b_i = \bigvee_{i \in I} (a \wedge b_i).$$
A *frame homomorphism* between frames is a map that preserves finite meets, including the top element, and arbitrary joins, including the bottom element.

## Remarks

Example: for a [[topological space|0CQHFPGJ45]] $X$, the [[open sets|02BH3MCBQB]] of $X$ ordered by inclusion form a frame $\Omega(X)$; joins are unions, finite meets are intersections, and $U \cap \bigcup_i V_i = \bigcup_i (U \cap V_i)$.
Non-example: the lattice of subspaces of $\R^2$ is complete but not a frame; for three distinct lines $a, b, c$ through $0$, $a \wedge (b \vee c) = a$ while $(a \wedge b) \vee (a \wedge c) = \set{0}$.
A complete lattice is a frame if and only if it is a [[Heyting algebra|NG943XNQWH]], with implication $a \to b = \bigvee \set{c : a \wedge c \le b}$.
Every frame is a [[distributive lattice|0HM0HQCK6N]].
As ordered sets, frames, locales and complete Heyting algebras are the same objects; the three names differ in the maps one uses between them.
