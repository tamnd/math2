---
tag: V0RBKHYTV7
kind: concept
name: Valuation on convex bodies
msc: [52B45, 52A20]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(geometry)
same_as:
  wikidata: Q85812715
  wikipedia: Valuation (geometry)
---

## Summary

A valuation on convex bodies is a function $\varphi$ on the nonempty compact convex sets of $\R^n$ that is additive in the inclusion–exclusion sense.
This means $\varphi(K \cup L) + \varphi(K \cap L) = \varphi(K) + \varphi(L)$ whenever $K \cup L$ is convex.
Volume, surface area, the Euler characteristic and all [[intrinsic volumes|C2CK6KSSTV]] are valuations.
Valuations are the finitely additive "measures" of convex geometry, and their classification, starting with [[Hadwiger's theorem|7V2X68AMEY]], is a central theme of integral geometry.
This notion is unrelated to valuations of fields in algebra.

## Explanations

### L1 human

A valuation is a way to measure convex shapes that does not count overlaps twice.
If two convex shapes together form a convex shape, then the measure of the union plus the measure of the overlap equals the sum of the two measures.
Area and perimeter of plane convex sets behave like this.
The function that gives $1$ to every nonempty convex set also does: $1 + 1 = 1 + 1$.
