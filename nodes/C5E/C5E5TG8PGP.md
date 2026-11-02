---
tag: C5E5TG8PGP
kind: concept
name: Ordinal analysis
msc: ["03F15", "03F05"]
uses: [N4EDJNMTEF, C72RBH0CDR, 0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
same_as:
  wikidata: Q7100782
  wikipedia: Ordinal analysis
---

## Summary

Ordinal analysis is the part of [[proof theory|N4EDJNMTEF]] that assigns to a formal theory its [[proof-theoretic ordinal|C72RBH0CDR]].
It measures the strength of a theory by the transfinite inductions that the theory can prove.
It started with Gentzen's consistency proof for [[Peano arithmetic|0QFT7Z76N5]], which gives the ordinal $\varepsilon_0$.
An ordinal analysis usually also yields a consistency proof and a description of the provably total functions of the theory.

## Explanations

### L1 human

Theories of arithmetic and of sets differ in strength, and ordinal analysis gives a ruler to measure them.
The marks on the ruler are countable ordinals, written in a finite notation system.
To place a theory, one shows that it proves induction up to every mark below some ordinal, and that it cannot reach that ordinal.
For Peano arithmetic the answer is $\varepsilon_0$.
Stronger theories, such as parts of second-order arithmetic, get much larger ordinals.
