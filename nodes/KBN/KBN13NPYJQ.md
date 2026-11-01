---
tag: KBN13NPYJQ
kind: concept
name: Completion of a ring
msc: [13B35, 13J10]
sources:
  - url: https://en.wikipedia.org/wiki/Completion_of_a_ring
same_as:
  wikidata: Q3685258
  wikipedia: Completion of a ring
---

## Summary

The completion of a [[commutative ring|0310REJJY8]] $R$ with respect to an [[ideal|096Z9MP2ME]] $I$ is the ring $\hat R = \varprojlim R/I^n$.
Its elements are compatible sequences of residues modulo the powers of $I$.
It is the completion of $R$ for the [[$I$-adic topology|2VF2TSJ3PY]], in the same way as the real numbers complete the rationals.
The $p$-adic integers and the formal power series rings arise in this way.
Completion is a basic tool to study a local ring near its closed point.

## Explanations

### L1 human

Knowing an integer modulo $2$, modulo $4$, modulo $8$, and so on, determines it.
A compatible list of such residues need not come from an integer, and the completion adds all such lists as new elements.
For $\Z$ and the prime $p$ one gets the [[$p$-adic integers|V6TJAFZ4MD]].
For $k[x]$ and the ideal $(x)$ one gets the [[formal power series|033WGN00BF]] $k[\![x]\!]$, where an element is known by its truncations modulo every power of $x$.
The [[definition|NS84D2920R]] makes this precise.
