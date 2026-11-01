---
tag: 6PCQEXEX4N
kind: conjecture
name: Collatz conjecture
msc: [11B83, 11B37]
uses: [0MWKJ44V5A, 0G9EKM0E15, RVG9Z8NYA6]
about: [6PCQEXEX4N]
sources:
  - url: https://en.wikipedia.org/wiki/Collatz_conjecture
same_as:
  wikidata: Q837314
  wikipedia: Collatz conjecture
history:
  posed_by: "Lothar Collatz"
  first_stated: "1937"
---

## Statement

Let $T$ be the map on the positive integers given by $T(n) = n/2$ if $n$ is even and $T(n) = 3n + 1$ if $n$ is odd.
For every positive integer $n$, there is an integer $k \ge 0$ with $T^k(n) = 1$, where $T^k$ is the $k$-fold iterate of $T$.

## Remarks

The conjecture is open.
It has been checked by computer for all starting values up to very large bounds.
Riho Terras showed in 1976 that the set of $n$ having some iterate $T^k(n) < n$ has [[natural density|RVG9Z8NYA6]] $1$.
Terence Tao showed in 2019 that almost all orbits, in the sense of logarithmic density, reach values below $f(n)$ for any function $f$ that tends to infinity.
For example, starting from $6$ the [[sequence|0G9EKM0E15]] is $6, 3, 10, 5, 16, 8, 4, 2, 1$.
Starting from $27$ it takes $111$ steps to reach $1$ and climbs as high as $9232$ on the way.
Once the sequence reaches $1$, it cycles through $1, 4, 2, 1$; the conjecture says that this is the only cycle and that no orbit grows without bound.

## Explanations

### L1 human

Pick a positive whole number.
If it is even, halve it; if it is odd, triple it and add one.
Repeat.
The conjecture says that you always end up at $1$, whatever number you start from.
The rule is simple enough for a child, yet nobody has found a proof, and many think current methods are not strong enough.
