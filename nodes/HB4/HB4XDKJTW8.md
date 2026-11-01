---
tag: HB4XDKJTW8
kind: concept
name: Annihilator
msc: [13C99, 13A15]
sources:
  - url: https://en.wikipedia.org/wiki/Annihilator_(ring_theory)
same_as:
  wikidata: Q567083
  wikipedia: Annihilator (ring theory)
---

## Summary

Let $M$ be a module over a commutative ring $R$.
The annihilator of $M$ is the set of elements of $R$ that send every element of $M$ to zero.
It is an ideal of $R$.
It measures how far the action of $R$ on $M$ is from being faithful.
It is used to study the [[support of a module|FETMR0M0M8]] and the [[associated primes|ERFZ6S8X0X]].
It differs from the [[annihilator of a subspace|0ASHNYF7AG]] in linear algebra, which lives in the dual space.

## Explanations

### L1 human

The annihilator of a module collects the ring elements that "kill" the whole module.
For the $\Z$-module $\Z/6\Z$, multiplying by $6$, $12$ or $-18$ gives zero on every element, and multiplying by any integer outside $6\Z$ does not.
So the annihilator of $\Z/6\Z$ is $6\Z$.
For a single element $m$, its annihilator is the set of $r$ with $rm = 0$.
