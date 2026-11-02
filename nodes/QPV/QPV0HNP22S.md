---
tag: QPV0HNP22S
kind: statement
role: theorem
name: Gentzen's consistency proof
msc: ["03F30", "03F15", "03F05"]
uses: [0QFT7Z76N5, KT50SMH3EC, 0ZHQMQ2C1N, X9WYNYE29C, 5NVA2JRHPV]
about: [0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Gentzen's_consistency_proof
same_as:
  wikidata: Q5533794
  wikipedia: Gentzen's consistency proof
---

## Statement

Let PA be first-order [[Peano arithmetic|0QFT7Z76N5]], and let PRA be primitive recursive arithmetic.
Fix a standard [[primitive recursive|5NVA2JRHPV]] notation system for the ordinals below [[epsilon nought|KT50SMH3EC]], ordered by a primitive recursive relation $\prec$.
Then the statement that PA is consistent is provable in PRA extended by the rule of [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ for quantifier-free formulas.

## Remarks

Gentzen published the proof in 1936, and a second proof in 1938.
In the second proof, one assigns to each derivation of a sequent in a sequent calculus for PA an ordinal below $\varepsilon_0$.
One then gives a primitive recursive reduction step that turns any derivation of the empty sequent into another derivation of the empty sequent with a smaller ordinal.
Transfinite induction along $\prec$ shows that no derivation of the empty sequent exists.

By [[Gödel's second incompleteness theorem|X9WYNYE29C]], PA does not prove its own consistency.
So PA does not prove the transfinite induction used here, although every part of the proof other than this induction is finitary.
Gentzen later showed directly that PA proves transfinite induction along $\prec$ up to each ordinal below $\varepsilon_0$, but not up to $\varepsilon_0$.
Thus $\varepsilon_0$ is exactly the length of induction that PA cannot reach.

## Explanations

### L1 human

Gödel showed that arithmetic cannot prove its own freedom from contradiction.
Gentzen found what extra principle is enough to prove it.
The principle is induction along an ordering of length $\varepsilon_0$, which is easy to describe with finite symbols.
Every other step of the proof uses only simple, finite reasoning about formulas.

### L2 human

The proof assigns ordinals to proofs and shows that reduction steps make the ordinal go down.
Since the ordinals below $\varepsilon_0$ are well-ordered, the reduction must stop, and so no proof of a contradiction can exist.
This is the first ordinal analysis: it shows that $\varepsilon_0$ is the proof-theoretic ordinal of PA.
The method extends to stronger theories, which get larger ordinals.
