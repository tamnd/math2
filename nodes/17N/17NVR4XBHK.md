---
tag: 17NVR4XBHK
kind: concept
name: Integral scheme
msc: [14A15]
specializes: [ZXSN8D4MCB]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry
---

## Summary

An integral scheme is a nonempty [[scheme|5A35TYZD02]] whose ring of functions on each nonempty open set is an [[integral domain|0QVD7WBFGN]].
Equivalently, it is [[reduced|ZXSN8D4MCB]] and its underlying space is irreducible.
Integral schemes are the scheme version of varieties, and each has a function field: the local ring at its [[generic point|3A19C4YXGE]].

## Explanations

### L1 human

An integral scheme is "all in one piece" and has no nilpotent fuzz.
The line $\operatorname{Spec} k[x]$ and $\operatorname{Spec} \Z$ are integral.
The union of the two coordinate axes, $\operatorname{Spec} k[x, y]/(xy)$, is reduced but made of two pieces, so it is not integral: $x \cdot y = 0$ with $x \ne 0$ and $y \ne 0$.
The double point $\operatorname{Spec} k[x]/(x^2)$ is one piece but not reduced, so it is not integral either.
