---
tag: HFBST11CT6
kind: concept
name: Unit in the last place
msc: [65G50, 65Y04]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_in_the_last_place
same_as:
  wikidata: Q7887129
  wikipedia: Unit in the last place
---

## Summary

The unit in the last place, or ulp, of a [[floating-point|RTKRSC3KPH]] number is the value of its last significant digit position.
It is the spacing between neighbouring floating-point numbers at that size.
Errors of computed results are often stated in ulps.
For example, a result correctly rounded to nearest is within half an ulp of the exact value.
The ulp of $1$ is the [[machine epsilon|JA3QXVF2B8]].

## Explanations

### L1 human

If a ruler is marked in millimetres, one millimetre is the smallest step it can show.
The ulp is that smallest step for a floating-point number.
In decimal with three significant digits, the number $3.14$ has ulp $0.01$, while $314$ has ulp $1$.
So the ulp grows with the size of the number, which is why floating-point accuracy is relative and not absolute.
