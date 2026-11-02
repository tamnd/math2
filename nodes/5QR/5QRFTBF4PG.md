---
tag: 5QRFTBF4PG
kind: concept
name: Injective object
msc: [18G05]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_object
same_as:
  wikidata: Q1625040
  wikipedia: Injective object
---

## Summary

An injective object of a [[category|A2DE66937D]] is an object $I$ such that maps into $I$ extend along every [[monomorphism|Y2NP1JFR86]].
In a category of modules, the injective objects are exactly the [[injective modules|85H7PRHDPZ]].
Among abelian groups they are the [[divisible groups|ZXVBEPMTCN]], such as $\Q$ and $\Q/\Z$.
Injective objects are used to build injective resolutions, from which right [[derived functors|NPMC3K6J2F]] such as sheaf cohomology are computed.
The dual notion is the [[projective object|YXMXAGVC1Q]].

## Explanations

### L1 human

Suppose $A$ sits inside a larger object $B$, and a map is given on $A$ with values in $I$.
The object $I$ is injective if such a map can always be extended to all of $B$.
The rational numbers have this property among abelian groups, because one can always divide in $\Q$ to find a value for a new element.
The integers do not: the map $2\Z \to \Z$ sending $2$ to $1$ cannot be extended to $\Z$, since its value at $1$ would be an integer whose double is $1$.
