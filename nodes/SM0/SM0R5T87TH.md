---
tag: SM0R5T87TH
kind: concept
name: Hellinger distance
msc: [62B10, 60B10]
sources:
  - url: https://en.wikipedia.org/wiki/Hellinger_distance
same_as:
  wikidata: Q3030678
  wikipedia: Hellinger distance
---

## Summary

The Hellinger distance is a distance between two probability distributions.
It compares the square roots of their densities in the $L^2$ sense.
It takes values in $[0, 1]$ and behaves well under independent products.
It is a standard tool in asymptotic statistics, for example for rates of convergence of estimators and in testing.

## Explanations

### L1 human

Take the square roots of two density functions, so that each becomes a unit vector in a space of functions.
The Hellinger distance measures how far apart these two unit vectors are.
Two equal distributions have distance $0$, and two distributions that live on disjoint sets have distance $1$.
For instance, a fair coin and a coin that always shows heads have squared Hellinger distance $1 - 1/\sqrt{2} \approx 0.29$.
[[Total variation distance|3SZESKX3N5]] is another common distance, and the two are always comparable.
