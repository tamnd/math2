---
tag: RVG9Z8NYA6
kind: concept
name: Natural density
msc: [11B05]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_density
same_as:
  wikidata: Q752723
  wikipedia: Natural density
---

## Summary

The natural density, or asymptotic density, of a set $A$ of positive integers is a limit as $n \to \infty$.
It is the limit of the proportion of $\set{1, \dots, n}$ that lies in $A$.
It makes precise statements such as "half of all integers are even" or "almost all integers are composite".
Not every set has a natural density, but every set has an upper and a lower density.
Many results of number theory, such as the [[Chebotarev density theorem|X8VKW5Y1CZ]], are statements about densities.

## Explanations

### L1 human

Count how many of the numbers $1, 2, \dots, n$ lie in $A$, divide by $n$, and let $n$ grow.
If the ratio settles down, its limit is the density of $A$.
The multiples of $3$ have density $1/3$, and the perfect squares have density $0$, because there are only about $\sqrt{n}$ of them up to $n$.
The set of numbers whose first decimal digit is $1$ has no density: the ratio keeps swinging between about $1/9$ and about $5/9$.
