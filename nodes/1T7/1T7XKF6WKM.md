---
tag: 1T7XKF6WKM
kind: definition
name: Affine morphism
msc: [14A15]
defines: AFC6JMYWEH
uses: [JXRKH6P1Z4, B3V3XJ2W8G]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_of_algebras
---

## Definition

A [[morphism of schemes|JXRKH6P1Z4]] $f \colon X \to Y$ is *affine* if $Y$ has a cover by open [[affine|B3V3XJ2W8G]] subschemes $V_i$ with each $f^{-1}(V_i)$ affine.

## Remarks

If $f$ is affine, then $f^{-1}(V)$ is affine for every open affine subscheme $V$ of $Y$.
Example: every morphism $\operatorname{Spec} A \to \operatorname{Spec} B$ is affine; take the cover of $Y = \operatorname{Spec} B$ by itself, with preimage $\operatorname{Spec} A$.
Example: a closed immersion is affine, since over $\operatorname{Spec} B$ it is $\operatorname{Spec} B/I \to \operatorname{Spec} B$ for an ideal $I$.
Non-example: for a field $k$, the morphism $\mathbb{A}^2_k \setminus \set{0} \to \operatorname{Spec} k$ is not affine.
The only open affine of $\operatorname{Spec} k$ is the whole space, and its preimage $\mathbb{A}^2_k \setminus \set{0}$ is not an affine scheme.
Its ring of global functions is $k[x, y]$, whose spectrum also contains the origin.
