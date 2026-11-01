---
tag: KCFXR9K3GD
kind: concept
name: VC dimension
msc: [05D05, 68Q32]
sources:
  - url: https://en.wikipedia.org/wiki/Vapnik–Chervonenkis_dimension
same_as:
  wikidata: Q2662236
  wikipedia: Vapnik–Chervonenkis dimension
---

## Summary

The VC dimension (Vapnik–Chervonenkis dimension) of a [[family of sets|0C21Q694AG]] is the size of the largest set on which it cuts out every subset.
It measures the complexity of the family as a single number.
By the [[Sauer–Shelah lemma|Y4FQT5WPQJ]], a family of finite VC dimension $d$ picks out only polynomially many subsets, about $n^d$, of an $n$-point set.
This is why VC dimension controls sample sizes in statistical learning theory.

## Explanations

### L1 human

Think of each set in the family as a rule that says "yes" to some points and "no" to others.
A set of points is shattered when the rules together can produce every possible yes/no pattern on it.
The VC dimension is the largest number of points that can be shattered.
For example, intervals on the real line can shatter any two points but no three points $a < b < c$, because no interval contains $a$ and $c$ but not $b$.
So intervals have VC dimension $2$.
