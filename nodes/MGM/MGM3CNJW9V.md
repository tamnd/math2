---
tag: MGM3CNJW9V
kind: concept
name: Discrete valuation ring
msc: [13F30, 13H05, 13F10]
specializes: [0CMD0BCH8T, QSX12D8RQM]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_valuation_ring
same_as:
  wikidata: Q986694
  wikipedia: Discrete valuation ring
---

## Summary

A discrete valuation ring is a [[principal ideal domain|0CMD0BCH8T]] with exactly one nonzero [[prime ideal|00MHHZ9SNE]].
It is the ring of elements of nonnegative value for a [[discrete valuation|A2KKZAV29W]] on its field of fractions.
Discrete valuation rings are among the simplest rings that are not fields: their ideals form a single chain of powers of one element.
They describe the local behaviour of curves at smooth points and of number rings at a prime.

## Explanations

### L1 human

In a discrete valuation ring there is one special element $\pi$, a uniformizer, and every nonzero element is a unit times a power of $\pi$.
The power of $\pi$ measures "how divisible" an element is.
The main example is the ring $\Z_{(p)}$ of fractions $a/b$ with $p \nmid b$, where $\pi = p$.
For instance, $12/5 = 3/5 \cdot 2^2$ in $\Z_{(2)}$, so its value is $2$.
Another example is the ring of formal power series $k[\![t]\!]$, where $\pi = t$ and the value of a series is its lowest degree.
