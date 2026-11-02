---
tag: DVSTWGVCSZ
kind: concept
name: Coequalizer
msc: [18A30]
specializes: [BJS1CGTKQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Coequalizer
same_as:
  wikidata: Q5140810
  wikipedia: Coequalizer
---

## Summary

The coequalizer of two parallel morphisms $f, g \colon X \to Y$ in a [[category|A2DE66937D]] is a universal morphism $q \colon Y \to Q$ with $q \circ f = q \circ g$.
It is the [[colimit|BJS1CGTKQ5]] of the diagram formed by $f$ and $g$, and it is dual to the [[equalizer|CTJ5AD8ST5]].
In sets it is the quotient of $Y$ that identifies $f(x)$ with $g(x)$ for each $x$.
In abelian groups it is the cokernel of $f - g$.

## Explanations

### L1 human

Given two functions $f$ and $g$ from $X$ to $Y$, glue $f(x)$ to $g(x)$ in $Y$ for every $x$, and keep gluing until the identifications are consistent.
The result is a quotient set $Q$ of $Y$, and $q$ sends each element of $Y$ to its glued class.
For example, let $X = \{*\}$, $Y = [0, 1]$, $f(*) = 0$ and $g(*) = 1$.
The coequalizer glues the two ends of the interval, and with the quotient topology it gives a circle.
