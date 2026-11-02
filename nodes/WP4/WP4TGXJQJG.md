---
tag: WP4TGXJQJG
kind: concept
name: Sufficient statistic
msc: [62B05]
specializes: [0Q5CG2NEQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Sufficient_statistic
same_as:
  wikidata: Q1099110
  wikipedia: Sufficient statistic
---

## Summary

A [[statistic|0Q5CG2NEQ8]] is sufficient for a parameter when it keeps all the information that the sample contains about that parameter.
Once its value is known, the rest of the data has a distribution free of the parameter, so it says nothing more about it.
Sufficiency allows data reduction without loss, and it underlies the [[Rao–Blackwell theorem|Y3TX4J41TP]] and the theory of optimal estimators.
The [[Fisher–Neyman factorization theorem|Z6MF9ZGCMW]] gives a practical test for it.

## Explanations

### L1 human

Toss a coin $10$ times to learn its chance of heads.
Only the number of heads matters, not the order in which heads and tails came.
Given that there were $4$ heads, every order of $4$ heads and $6$ tails is equally likely, whatever the coin.
So the number of heads is a sufficient statistic: it compresses the data without losing anything about the coin.
