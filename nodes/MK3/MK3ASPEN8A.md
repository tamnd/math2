---
tag: MK3ASPEN8A
kind: concept
name: Carlson symmetric forms
msc: ["33E05", 33F05]
specializes: [NXMCYGCB59]
sources:
  - url: https://en.wikipedia.org/wiki/Carlson_symmetric_form
same_as:
  wikidata: Q5042922
  wikipedia: Carlson symmetric form
---

## Summary

The Carlson symmetric forms $R_F$, $R_J$, $R_C$ and $R_D$ are a standard set of [[elliptic integrals|NXMCYGCB59]] that are symmetric in their main arguments.
Every elliptic integral can be written with them, and in particular the Legendre integrals $F$, $E$ and $\Pi$.
Their symmetry gives a duplication theorem that leads to fast and stable numerical algorithms, which is why software libraries use them.

## Explanations

### L1 human

Legendre's forms of the elliptic integrals depend on an angle and a modulus, and the formulas that transform them are lopsided.
Carlson's forms put the three roots of the cubic under the square root on an equal footing, so permuting $x$, $y$, $z$ does not change the value.
For example $R_F(x, y, z) = \frac{1}{2}\int_0^\infty dt / \sqrt{(t + x)(t + y)(t + z)}$, and $R_F(x, x, x) = 1/\sqrt{x}$.
The complete integral of the first kind is $K(k) = R_F(0, 1 - k^2, 1)$.
