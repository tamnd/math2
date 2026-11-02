---
tag: 1AKB4XHMTH
kind: concept
name: Numerical stability
msc: [65G50, 65F35]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_stability
same_as:
  wikidata: Q1430640
  wikipedia: Numerical stability
---

## Summary

An algorithm is numerically stable when the errors it makes, such as [[round-off errors|CPN6SD3BTV]], are not amplified beyond what the problem itself forces.
The strongest common form is backward stability: the computed answer is the exact answer for a slightly perturbed input, as in [[backward error analysis|CMXHRNWY35]].
A stable algorithm applied to a well-conditioned problem gives an accurate answer; for an ill-conditioned problem even a stable algorithm can give large errors.
For methods for differential equations, stability means instead that errors in the steps stay bounded, as checked by [[von Neumann stability analysis|2Z7NASDQB6]].

## Explanations

### L1 human

Two formulas can be equal in exact arithmetic but behave very differently on a computer.
For example, the roots of $x^2 - 10^8 x + 1 = 0$ are about $10^8$ and $10^{-8}$.
The textbook formula computes the small root as $(10^8 - \sqrt{10^{16} - 4})/2$, a difference of two almost equal numbers, and loses most of its digits.
The equivalent formula $2/(10^8 + \sqrt{10^{16} - 4})$ has no such subtraction and is accurate.
The second formula is a stable way to compute the small root and the first is not.
