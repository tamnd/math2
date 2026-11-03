---
tag: DZWEWHZ20N
kind: concept
name: Joint entropy
msc: [94A17]
specializes: [Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Joint_entropy
same_as:
  wikidata: Q1364826
  wikipedia: Joint entropy
---

## Summary

The joint entropy $H(X, Y)$ of two discrete random variables is the [[Shannon entropy|Y86E072V0V]] of the pair $(X, Y)$, computed from their [[joint distribution|0DR81R1F2B]].
It measures the uncertainty of the two values taken together.
It is at least the larger of $H(X)$ and $H(Y)$ and at most $H(X) + H(Y)$, with equality on the right exactly for independent variables.
Together with [[conditional entropy|F3ZNDD6GG7]] it gives the chain rule $H(X, Y) = H(X) + H(Y \mid X)$.

## Explanations

### L1 human

Joint entropy asks how much information two random quantities carry together.
If they are independent, such as two fair coins, the information adds: $1 + 1 = 2$ bits.
If one determines the other, such as a fair coin and a copy of it, the pair carries only $1$ bit, since the second value adds nothing new.
In general the answer lies between these extremes, and the gap from the sum measures how much the two variables share.
