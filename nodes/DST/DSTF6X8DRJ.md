---
tag: DSTF6X8DRJ
kind: concept
name: Admissible decision rule
msc: [62C15]
sources:
  - url: https://en.wikipedia.org/wiki/Admissible_decision_rule
same_as:
  wikidata: Q4683801
  wikipedia: Admissible decision rule
---

## Summary

A decision rule is admissible if no other rule beats it in the following sense.
The other rule is at least as good for every value of the parameter and strictly better for some value.
Admissibility is a minimal requirement of rationality in [[statistical decision theory|CPFSBBHXT5]]: an inadmissible rule can be replaced by one that never does worse.
[[Stein's example|7SC9E65XDN]] shows that even very natural estimators can fail to be admissible.

## Explanations

### L1 human

Compare two rules by their average loss for each possible truth.
If one rule is never worse than another and sometimes better, the worse one should never be used: it is inadmissible.
An admissible rule is one that cannot be beaten in this complete way.
Being admissible does not mean being good.
The rule that always guesses $0$, ignoring the data, is admissible for estimating a normal mean, because nothing beats it when the truth is $0$.
