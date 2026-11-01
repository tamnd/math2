---
tag: QVPYBPRHRC
kind: concept
name: Mahler measure
msc: [11R06, 11C08]
sources:
  - url: https://en.wikipedia.org/wiki/Mahler_measure
same_as:
  wikidata: Q6734205
  wikipedia: Mahler measure
---

## Summary

The Mahler measure of a complex polynomial is the absolute value of its leading coefficient times a product over its roots.
Each root outside the unit circle contributes its absolute value, and the other roots contribute $1$.
It is multiplicative and, for integer polynomials, it is at least $1$.
It measures the size of a polynomial in a way adapted to its roots.
Small Mahler measures of integer polynomials are the subject of [[Lehmer's conjecture|NDRRH2YD2C]].

## Explanations

### L1 human

Factor the polynomial into its leading coefficient and linear factors.
Keep the leading coefficient and every root of absolute value bigger than $1$, and multiply their absolute values.
For $x^2 - 2$, the roots are $\pm \sqrt{2}$, so the Mahler measure is $\sqrt{2} \cdot \sqrt{2} = 2$.
The [[definition|1PJS951C8N]] states the formula.
