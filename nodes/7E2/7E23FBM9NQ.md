---
tag: 7E23FBM9NQ
kind: definition
name: Quadratic field
msc: [11R11]
defines: 7SV4WA92SM
uses: [MWBDFS2KJ5, 0EAJ2XXADC, 08X0VCR2NW]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_field
---

## Definition

A *quadratic field* is an [[algebraic number field|MWBDFS2KJ5]] $K$ with [[degree|0EAJ2XXADC]] $[K : \Q] = 2$.

## Remarks

Every quadratic field is $\Q(\sqrt{d}) = \set{a + b\sqrt{d} : a, b \in \Q}$ for exactly one [[square-free integer|08X0VCR2NW]] $d$ with $d \ne 0, 1$.
It is called real if $d > 0$ and imaginary if $d < 0$.
Example: $\Q(\sqrt{2})$; the element $\sqrt{2}$ is a root of the irreducible polynomial $x^2 - 2$, so $1, \sqrt{2}$ is a basis and the degree is $2$.
Non-example: $\Q(\sqrt[3]{2})$ has degree $3$, because $x^3 - 2$ is irreducible over $\Q$; so it is a number field but not a quadratic field.
The ring of integers of $\Q(\sqrt{d})$ is $\Z[(1 + \sqrt{d})/2]$ if $d \equiv 1 \pmod 4$, and $\Z[\sqrt{d}]$ if $d \equiv 2$ or $3 \pmod 4$.
The discriminant is $d$ in the first case and $4d$ in the second.
