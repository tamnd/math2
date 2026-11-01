---
tag: E1SQWQ2PAV
kind: concept
name: Kloosterman sum
msc: [11L05]
specializes: [97PBMQCPPM]
sources:
  - url: https://en.wikipedia.org/wiki/Kloosterman_sum
same_as:
  wikidata: Q6421354
  wikipedia: Kloosterman sum
---

## Summary

A Kloosterman sum is an [[exponential sum|97PBMQCPPM]] over the invertible residues $x$ modulo $m$ with phase $(ax + b\bar{x})/m$.
Here $\bar{x}$ is the inverse of $x$ modulo $m$.
It is a real number, and for a prime modulus $p$ not dividing $ab$ Weil's bound gives $\abs{K(a, b; p)} \le 2\sqrt{p}$.
Kloosterman sums appear in the Fourier coefficients of Poincaré series, in the circle method for quadratic forms, and in the spectral theory of automorphic forms.

## Explanations

### L1 human

Pair each invertible residue $x$ modulo $m$ with its inverse $\bar{x}$, and turn $ax + b\bar{x}$ into a point on the unit circle.
The Kloosterman sum adds these points.
For a prime modulus $p$ there are $p - 1$ terms, but the inverse map scrambles them so much that the sum has size at most $2\sqrt{p}$.
For $m = 5$ and $a = b = 1$, the sum equals $2 + 2\cos(4\pi/5) \approx 0.38$.
