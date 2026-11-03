---
tag: D2WZ0M5RWX
kind: concept
name: Berlekamp–Welch algorithm
msc: [94B35, 94B05]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Welch_algorithm
same_as:
  wikidata: Q4892328
  wikipedia: Berlekamp–Welch algorithm
---

## Summary

The Berlekamp–Welch algorithm decodes a [[Reed–Solomon code|5VBWJ7EFTX]] up to half its [[minimum distance|M2X88AXM17]].
It finds the sent polynomial by solving one system of linear equations over the [[finite field|0ZXZ82FTX2]], followed by one polynomial division.
The key idea is an unknown error-locator polynomial that vanishes at the corrupted positions.
It is a simple polynomial-time decoder and the starting point of the [[Guruswami–Sudan algorithm|W0V3GVZ4VQ]].

## Explanations

### L1 human

The receiver gets the values of an unknown polynomial $f$ at $n$ points, but a few values are wrong.
Imagine a polynomial $E$ that is zero exactly at the wrong positions.
Then $f(a_i) E(a_i) = y_i E(a_i)$ at every point, whether the value $y_i$ is correct or not.
Treating $Q = fE$ and $E$ as unknowns makes these equations linear, so ordinary linear algebra finds them.
Dividing $Q$ by $E$ then gives back $f$.
