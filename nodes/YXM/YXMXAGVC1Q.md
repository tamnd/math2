---
tag: YXMXAGVC1Q
kind: concept
name: Projective object
msc: [18G05]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_object
same_as:
  wikidata: Q2112502
  wikipedia: Projective object
---

## Summary

A projective object of a [[category|A2DE66937D]] is an object $P$ such that maps from $P$ lift through every [[epimorphism|RVXDSY04KG]].
In a category of modules, the projective objects are exactly the [[projective modules|BFFA03GE3V]], for example the free modules.
Projective objects are used to build projective resolutions, from which left [[derived functors|NPMC3K6J2F]] are computed.
The dual notion is the [[injective object|5QRFTBF4PG]].

## Explanations

### L1 human

Think of an epimorphism $E \to X$ as a way of covering $X$ by a bigger object $E$.
An object $P$ is projective if any map from $P$ into $X$ can be pulled back up to a map into $E$.
Free objects have this property because one only has to choose where the generators go, and each generator can be sent to any preimage.
For example, $\Z$ is projective among abelian groups, but $\Z/2\Z$ is not: the identity of $\Z/2\Z$ does not lift along $\Z \to \Z/2\Z$, since $\Z$ has no element of order $2$.
