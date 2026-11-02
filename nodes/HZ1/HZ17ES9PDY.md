---
tag: HZ17ES9PDY
kind: concept
name: Dialectica interpretation
msc: ["03F10", "03F25", "03F50"]
uses: [CK8ZQRN183, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
same_as:
  wikidata: Q5270518
  wikipedia: Dialectica interpretation
---

## Summary

The Dialectica interpretation translates [[Heyting arithmetic|CK8ZQRN183]] into Gödel's system T.
This is a quantifier-free theory of computable functionals of finite type.
Gödel published it in 1958 in the journal Dialectica.
Each formula becomes a formula of the form $\exists x\, \forall y\, A_D(x, y)$, and a proof yields a term of system T that gives the witness $x$.
It gives a relative consistency proof of arithmetic and is the main tool for extracting bounds from proofs.

## Explanations

### L1 human

The interpretation reads each statement as a game between two players.
One player chooses $x$, the other answers with $y$, and the first wins if the simple condition $A_D(x, y)$ holds.
A proof of the statement gives a winning strategy, written as a program built from [[primitive recursion|5NVA2JRHPV]] in higher types.
For example, a proof of $\forall n\, \exists m\, (m > n)$ yields the program $n \mapsto n + 1$.
In this way, numbers and bounds can be read off from proofs.
