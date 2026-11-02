---
tag: SMAQN2N739
kind: concept
name: Indefinite sum
msc: [39A12, 39A70]
sources:
  - url: https://en.wikipedia.org/wiki/Indefinite_sum
same_as:
  wikidata: Q6015812
  wikipedia: Indefinite sum
---

## Summary

An indefinite sum, or antidifference, of a function $f$ is a function $F$ whose forward difference is $f$, that is $F(x + 1) - F(x) = f(x)$.
It plays the role for sums that an [[antiderivative|0BYWRWFT4F]] plays for integrals.
With an indefinite sum, every finite sum $\sum_{k=a}^{b-1} f(k)$ becomes the difference $F(b) - F(a)$.

## Explanations

### L1 human

Summing a sequence is the reverse of taking differences.
If you know a function $F$ whose steps are exactly the terms you want to add, then the total of the terms is just how far $F$ has moved.
For $f(x) = x$, the function $F(x) = x(x-1)/2$ works, since $F(x + 1) - F(x) = x$.
So $0 + 1 + \dots + (n-1) = F(n) - F(0) = n(n-1)/2$.
