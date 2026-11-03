---
tag: FPD6AN79QX
kind: concept
name: Beta normal form
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_normal_form
same_as:
  wikidata: Q4897305
  wikipedia: Beta normal form
---

## Summary

A lambda term is in beta normal form when no [[beta reduction|Y9B9CVY6SJ]] step can be applied to it.
Such a term is a finished computation, its value.
By the [[Church–Rosser theorem|7NNF74EYDX]], a term has at most one beta normal form up to renaming of bound variables.
Some terms, such as $(\lambda x.\, x\, x)(\lambda x.\, x\, x)$, have no normal form at all.

## Explanations

### L1 human

A normal form is an expression that cannot be simplified any further.
In arithmetic, $2 + 3$ simplifies to $5$, and $5$ is the normal form.
In the lambda calculus, $(\lambda x.\, x)\, y$ simplifies to $y$, and $y$ is the normal form.
A term whose computation runs forever, such as a term that copies itself at every step, has no normal form.
