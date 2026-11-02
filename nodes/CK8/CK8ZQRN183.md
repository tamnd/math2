---
tag: CK8ZQRN183
kind: concept
name: Heyting arithmetic
msc: ["03F55", "03F30", "03F50"]
uses: [0QFT7Z76N5, Q11N8X99FK]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
same_as:
  wikidata: Q5548813
  wikipedia: Heyting arithmetic
---

## Summary

Heyting arithmetic, HA, is the theory of the natural numbers with the axioms of [[Peano arithmetic|0QFT7Z76N5]] and the rules of [[intuitionistic logic|Q11N8X99FK]].
It is the standard formal system for constructive arithmetic.
Every existence theorem of HA comes with a way to compute a witness.
It proves the same formulas as Peano arithmetic up to a double-negation translation, so the two theories are equally consistent.

## Explanations

### L1 human

Heyting arithmetic keeps the usual axioms of the natural numbers, including induction.
It only removes one rule of logic: the law that every statement is either true or false.
So it can prove "$A$ or $B$" only when it can tell which of the two holds.
For example, it proves that every number is even or odd, because one can compute which.
It cannot prove the statement "every program halts or does not halt", since no algorithm decides which.
