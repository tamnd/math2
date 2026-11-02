---
tag: PV0XXSWFC7
kind: concept
name: Premeasure
msc: [28A12]
sources:
  - url: https://en.wikipedia.org/wiki/Pre-measure
same_as:
  wikidata: Q1393014
  wikipedia: Pre-measure
---

## Summary

A premeasure is a countably additive size function defined only on a [[ring of sets|KWE1DBMN9B]].
Such a ring is closed under finite unions and differences, but not under countable unions.
It is the raw material for building a [[measure|PR11BZQQPG]].
By [[Carathéodory's extension theorem|Q8EXG7EKYW]] every premeasure extends to a measure on the generated $\sigma$-algebra.

## Explanations

### L1 human

Often one knows the size of simple sets, such as finite unions of intervals, before one knows the size of complicated sets.
A premeasure records these sizes and asks that they add up correctly, even when a simple set is cut into countably many simple pieces.
For example, length on finite unions of half-open intervals $(a, b]$ is a premeasure.
If $(0, 1]$ is cut into the pieces $(1/2, 1]$, $(1/4, 1/2]$, $(1/8, 1/4]$, and so on, the lengths $1/2 + 1/4 + 1/8 + \cdots$ add up to $1$.
