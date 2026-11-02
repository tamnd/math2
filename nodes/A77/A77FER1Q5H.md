---
tag: A77FER1Q5H
kind: concept
name: Curry–Howard correspondence
msc: ["03B40", "03F03", "68N18"]
uses: [BD756KR8FM, Q11N8X99FK, Q48KGV33AH]
sources:
  - url: https://en.wikipedia.org/wiki/Curry–Howard_correspondence
same_as:
  wikidata: Q975734
  wikipedia: Curry–Howard correspondence
---

## Summary

The Curry–Howard correspondence is the match between proofs in [[intuitionistic logic|Q11N8X99FK]] and programs in typed [[lambda calculus|BD756KR8FM]].
A proposition corresponds to a type, and a proof of the proposition corresponds to a program of that type.
Simplifying a proof corresponds to running the program.
It is the basis of proof assistants built on [[type theory|Q48KGV33AH]], where checking a proof means checking the type of a program.

## Explanations

### L1 human

The slogan is "propositions are types, and proofs are programs".
A proof of "if $A$ then $B$" is a function that turns any proof of $A$ into a proof of $B$.
A proof of "$A$ and $B$" is a pair made of a proof of $A$ and a proof of $B$.
For example, the program that takes $x$ and $y$ and returns $x$ has type $A \to (B \to A)$, and it is also a proof of that formula.
Curry noticed such a match for combinators, and Howard extended it to natural deduction.
