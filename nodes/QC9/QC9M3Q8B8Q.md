---
tag: QC9M3Q8B8Q
kind: concept
name: Lindenbaum–Tarski algebra
msc: ["03G05", "03B05"]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
same_as:
  wikidata: Q841805
  wikipedia: Lindenbaum–Tarski algebra
---

## Summary

The Lindenbaum–Tarski algebra of a logical theory is the set of its formulas taken up to provable equivalence, with the operations induced by the connectives.
For a theory of classical [[propositional logic|09K9MWD2QQ]] it is a [[Boolean algebra|0XADJKM699]].
It turns statements about provability into statements about an algebra, and it is the basic tool in algebraic proofs of completeness theorems.

## Explanations

### L1 human

Two formulas such as $p \wedge q$ and $q \wedge p$ look different but say the same thing.
The Lindenbaum–Tarski algebra glues together all formulas that the theory proves to be equivalent.
Each glued class becomes one element, and "and", "or" and "not" act on these classes.
With one propositional variable $p$ and no extra axioms, there are exactly four classes, those of $p$, $\neg p$, $p \vee \neg p$ and $p \wedge \neg p$.
