---
tag: S6CCJBJKHR
kind: definition
name: Fiber product of schemes
msc: [14A15, 18A30]
defines: 1DZMT4S9FB
uses: [5A35TYZD02, JXRKH6P1Z4, Q05K04QJ71, 1735VGRT2P]
sources:
  - url: https://en.wikipedia.org/wiki/Fiber_product_of_schemes
---

## Definition

Let $S$, $X$ and $Y$ be [[schemes|5A35TYZD02]], and let $f \colon X \to S$ and $g \colon Y \to S$ be [[morphisms of schemes|JXRKH6P1Z4]].
A *fiber product* of $X$ and $Y$ over $S$ is a scheme $P$ with morphisms $p \colon P \to X$ and $q \colon P \to Y$ such that:

1. $f \circ p = g \circ q$.
2. For every scheme $T$ and morphisms $a \colon T \to X$ and $b \colon T \to Y$ with $f \circ a = g \circ b$, there is a unique morphism $h \colon T \to P$ with $p \circ h = a$ and $q \circ h = b$.

The fiber product exists for all such data and is unique up to unique isomorphism.
It is written $X \times_S Y$; it is the [[pullback|Q05K04QJ71]] in the category of schemes.

## Remarks

Example: for ring maps $A \to B$ and $A \to C$, the fiber product of $\operatorname{Spec} B$ and $\operatorname{Spec} C$ over $\operatorname{Spec} A$ is $\operatorname{Spec}(B \otimes_A C)$.
The projections come from $b \mapsto b \otimes 1$ and $c \mapsto 1 \otimes c$, and clause 2 follows from the universal property of the [[tensor product of algebras|1735VGRT2P]].
Non-example: the underlying set of $X \times_S Y$ is in general not the fiber product of the underlying sets.
For instance, $\operatorname{Spec} \C \times_{\operatorname{Spec} \R} \operatorname{Spec} \C = \operatorname{Spec}(\C \otimes_\R \C) \cong \operatorname{Spec}(\C \times \C)$ has two points, while the set product has one.
When $S = \operatorname{Spec} \Z$, one writes $X \times Y$ for $X \times_S Y$.
