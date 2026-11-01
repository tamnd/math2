---
tag: T6HCX959PJ
kind: concept
name: Gorenstein ring
msc: [13H10, 13D05]
sources:
  - url: https://en.wikipedia.org/wiki/Gorenstein_ring
same_as:
  wikidata: Q5586177
  wikipedia: Gorenstein ring
---

## Summary

A Gorenstein ring is a Noetherian ring whose local rings have finite injective dimension as modules over themselves.
Gorenstein rings sit between [[complete intersection rings|EPM2HKGMZS]] and [[Cohen–Macaulay rings|N1QJQEGBFC]]: every complete intersection is Gorenstein and every Gorenstein ring is Cohen–Macaulay.
They are exactly the Cohen–Macaulay local rings whose [[canonical module|W5ECXPM6FW]] is the ring itself, which makes duality statements particularly clean.

## Explanations

### L1 human

Gorenstein rings have a built-in symmetry.
For a finite-dimensional local algebra over a field, the condition says that the "bottom" of the ring, the part killed by every non-unit, is one-dimensional.
The ring $K[x]/(x^3)$ is Gorenstein: its bottom is spanned by $x^2$.
The ring $K[x,y]/(x^2, xy, y^2)$ is not: its bottom is spanned by both $x$ and $y$.
