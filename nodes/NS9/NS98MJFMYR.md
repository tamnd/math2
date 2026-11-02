---
tag: NS98MJFMYR
kind: definition
name: Functor of points
msc: [14A15, 18F20]
defines: SWWW9X4A3N
uses: [5A35TYZD02, JXRKH6P1Z4, 28NQ0KRHD3, DAMK8XE1FR, KCCHH87H6E, D6DF1ARPVD]
sources:
  - url: https://en.wikipedia.org/wiki/Functor_represented_by_a_scheme
---

## Definition

Let $\mathrm{Sch}$ be the category of [[schemes|5A35TYZD02]] and [[morphisms of schemes|JXRKH6P1Z4]], and let $X$ be a scheme.
The *functor of points* of $X$ is the [[functor|28NQ0KRHD3]]
$$h_X \colon \mathrm{Sch}^{\mathrm{op}} \to \mathrm{Set}, \quad h_X(T) = \Hom_{\mathrm{Sch}}(T, X),$$
on the [[opposite category|DAMK8XE1FR]] of $\mathrm{Sch}$.
For a morphism $u \colon T' \to T$, the map $h_X(u)$ sends $a \colon T \to X$ to $a \circ u$.
An element of $h_X(T)$ is a *$T$-point* of $X$; for a ring $A$, one writes $X(A) = h_X(\operatorname{Spec} A)$.

## Remarks

By the [[Yoneda lemma|D6DF1ARPVD]], the rule $X \mapsto h_X$ is fully faithful, so a scheme is determined up to unique isomorphism by its functor of points.
It suffices to know $X(A)$ for all commutative rings $A$.
Example: for $X = \mathbb{A}^n_\Z = \operatorname{Spec} \Z[x_1, \ldots, x_n]$, a morphism $\operatorname{Spec} A \to X$ is a ring map $\Z[x_1, \ldots, x_n] \to A$.
Such a map is given by the images of the $x_i$, so $X(A) = A^n$.
Non-example: the constant functor $F$ with $F(T) = \set{0, 1}$ for all $T$ is not of the form $h_X$.
For the empty scheme $\emptyset$, the set $h_X(\emptyset)$ has exactly one element for every $X$, while $F(\emptyset)$ has two.
A functor isomorphic to some $h_X$ is called [[representable|KCCHH87H6E]], and $X$ then represents it.
