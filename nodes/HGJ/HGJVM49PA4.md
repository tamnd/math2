---
tag: HGJVM49PA4
kind: concept
name: Double-negation translation
msc: ["03F25", "03F55", "03B20"]
uses: [Q11N8X99FK, 0XR7A7RSXB, 0QFT7Z76N5, CK8ZQRN183]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
same_as:
  wikidata: Q5299605
  wikipedia: Double-negation translation
---

## Summary

A double-negation translation is a map from formulas to formulas that embeds classical logic into [[intuitionistic logic|Q11N8X99FK]].
It inserts [[negations|0XR7A7RSXB]] $\neg \neg$ at chosen places, so that a formula is classically provable exactly when its translation is intuitionistically provable.
The best known versions are due to Kolmogorov, to Gödel and Gentzen, and to Kuroda.
It shows that [[Peano arithmetic|0QFT7Z76N5]] is consistent if [[Heyting arithmetic|CK8ZQRN183]] is.

## Explanations

### L1 human

Intuitionistic logic rejects some classical reasoning, such as "$A$ or not $A$".
But it accepts "it is not the case that neither $A$ nor not $A$", that is, $\neg \neg (A \vee \neg A)$.
The translation rewrites each classical claim in such a doubly negated, weaker form.
Then every classical proof becomes an intuitionistic proof of the weaker claim.
So a contradiction in classical reasoning would give a contradiction in intuitionistic reasoning too.
