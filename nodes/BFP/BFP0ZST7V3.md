---
tag: BFP0ZST7V3
kind: conjecture
name: Jacobson's conjecture
msc: [16P40, 16N20]
uses: [0894J980RK, 7HWZ06SRMF, 0MVH4Y1CRZ]
about: [XA0DCNH7WY, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobson%27s_conjecture
same_as:
  wikidata: Q16000128
  wikipedia: Jacobson's conjecture
history:
  posed_by: "Nathan Jacobson"
  first_stated: "1956"
---

## Statement

Let $R$ be a [[ring|0894J980RK]] with unit that is [[Noetherian|0MVH4Y1CRZ]] on both sides, that is, left Noetherian and right Noetherian.
Let $J$ be the [[Jacobson radical|7HWZ06SRMF]] of $R$.
Then
$$\bigcap_{n \ge 1} J^n = 0.$$

## Remarks

The conjecture is open in general.
For commutative Noetherian rings it holds, by the Krull intersection theorem.
The one-sided version, for rings that are only right Noetherian, is false; I. N. Herstein gave a counterexample.
The conjecture is known for several classes of two-sided Noetherian rings, among them the fully bounded Noetherian rings.

## Explanations

### L1 human

The Jacobson radical $J$ collects the elements of a ring that are "small" in a precise sense.
Its powers $J, J^2, J^3, \ldots$ shrink, and the conjecture says that in a Noetherian ring nothing survives in all of them.
For commutative rings this is a classical theorem of Krull, and the question is whether the same holds without commutativity.
