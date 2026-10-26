---
tag: 05WAF5T0GZ
kind: statement
role: corollary
name: Maximal ideals are prime
msc: [13A15]
uses: [09J6KGT65G, 06HC6HK0Z8, 0WD3SE7S1X, 0AVXBEC05W]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_ideal
    locator: Properties
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $M$ be a [[maximal ideal|09J6KGT65G]] of $R$.
Then $M$ is a [[prime ideal|06HC6HK0Z8]].

## Remarks

The proof: [[$R/M$ is a field|0WD3SE7S1X]], so it is an integral domain, so [[$M$ is prime|0AVXBEC05W]].
The converse is false: the zero ideal of $\mathbb{Z}$ is prime but not maximal.
In $\mathbb{Z}$, every nonzero prime ideal is maximal.

## Explanations

### L1 human

Every field is an integral domain.
So when $R/M$ is a field, $R/M$ is an integral domain, and $M$ is prime.
The zero ideal of the integers shows that a prime ideal need not be maximal.
