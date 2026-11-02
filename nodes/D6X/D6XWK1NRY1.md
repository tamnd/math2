---
tag: D6XWK1NRY1
kind: concept
name: Abelian and Tauberian theorems
msc: ["40E05", "40D05", "11M45"]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
same_as:
  wikidata: Q2376918
  wikipedia: Abelian and Tauberian theorems
---

## Summary

Abelian and Tauberian theorems are two opposite kinds of results about [[summability methods|8X25Q4XYMN]].
An Abelian theorem says that a method gives the usual value to every convergent series.
More generally, it says that summability by one method implies summability by another, with the same value.
[[Abel's theorem|0S4EMDQS2F]] is the model.
A Tauberian theorem is a partial converse.
It says that a summable series converges, provided its terms satisfy an extra [[Tauberian condition|6ZDP261K7R]].
[[Tauber's theorem|8SK3GQ4S0M]] is the model.
Tauberian theorems for integral transforms, such as the [[Wiener–Ikehara theorem|KQ57DC3AKM]], give short proofs of the [[prime number theorem|0EHBY5Y84N]].

## Explanations

### L1 human

Summation methods are ways to give a value to a series that may diverge.
An Abelian theorem checks that a method does no harm: a series that already has a sum keeps the same sum.
A Tauberian theorem goes the other way: if a method gives a value and the terms are small enough, the series really converges to that value.
For example, if $\sum a_n x^n \to s$ as $x \to 1^-$ and $n a_n \to 0$, then $\sum a_n = s$.
