---
tag: FTE966EMW8
kind: concept
name: Inner measure
msc: [28A12]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_measure
same_as:
  wikidata: Q6035652
  wikipedia: Inner measure
---

## Summary

The inner measure of a set approximates it from inside: it is the largest measure of a measurable set contained in it.
It is the companion of the [[outer measure|BJ314H17HC]], which approximates from outside.
For Lebesgue measure, a set of finite outer measure is measurable exactly when its inner and outer measures agree.
Historically, Lebesgue defined measurability in this way.

## Explanations

### L1 human

To measure an odd-shaped region from inside, fill it with pieces whose size is known, and take the largest total size you can fit.
The outer measure does the opposite: it covers the region and takes the smallest cover.
For a nice region the two numbers agree.
For example, the set of irrational numbers in $[0, 1]$ has inner and outer Lebesgue measure $1$.
For a Vitali set in $[0, 1]$, the inner measure is $0$ and the outer measure is positive.
