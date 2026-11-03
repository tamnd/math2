---
tag: 9KYWN94QDN
kind: concept
name: Banach algebra
msc: [46H05, 46J05]
specializes: [4DJ4V5VBSH]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_algebra
same_as:
  wikidata: Q806066
  wikipedia: Banach algebra
---

## Summary

A Banach algebra is an associative algebra over $\R$ or $\C$ with a complete norm that satisfies $\norm{xy} \le \norm{x}\norm{y}$.
It is a [[normed algebra|4DJ4V5VBSH]] that is also a [[Banach space|06GZ956657]].
Completeness makes power series converge, so in a unital Banach algebra $1 - x$ is invertible when $\norm{x} < 1$.
In a nonzero complex unital Banach algebra the spectrum of every element is a nonempty compact set.
Algebras of bounded operators, continuous functions and integrable functions on groups are the main examples, and [[C*-algebras|M2WFY1D3SZ]] are the most studied special class.

## Explanations

### L1 human

A Banach algebra is a space where one can add, multiply and take limits, with sizes measured by a norm.
The norm of a product is at most the product of the norms, so multiplication cannot blow up sizes.
The continuous functions on $[0, 1]$, with the largest absolute value as norm, form a Banach algebra.
The $n \times n$ complex matrices with the operator norm form another, and there the algebra is not commutative.
The point of the theory is to study invertibility and spectra of elements, as for matrices, in infinite dimensions.
