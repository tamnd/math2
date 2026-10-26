---
tag: 0FYQMKFE77
kind: concept
name: Order of quantifiers
aliases: [quantifier-order]
msc: [03B10]
uses: [0B88PQTJ66, 0JW2FHW7G3]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
same_as:
  wikidata: Q592911
  wikipedia: Quantifier (logic)
---

## Summary

In a statement with several quantifiers, the order of different quantifiers changes the meaning.
For a [[predicate|0T3DPBG981]] $P(x, y)$, the statement $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$, but the converse is false in general.
Two quantifiers of the same type commute: $\forall x \, \forall y \, P(x, y)$ is equivalent to $\forall y \, \forall x \, P(x, y)$, and the same holds for $\exists$.

## Remarks

On the integers, $\forall x \, \exists y \, (y > x)$ is true, but $\exists y \, \forall x \, (y > x)$ is false.
In $\forall x \, \exists y$, the choice of $y$ can depend on $x$.
The definitions of continuity and of uniform continuity differ only in the order of quantifiers.

## Explanations

### L1 human

"Every person has a mother" is $\forall x \, \exists y$: each person has their own mother.
"Some person is the mother of every person" is $\exists y \, \forall x$: one mother for all.
The first sentence is true, and the second is false.
