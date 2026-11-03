---
tag: TKMY3F6KSA
kind: concept
name: Calculus of constructions
msc: [03B38, 03B40, 68V15]
uses: [SVNYKTGQ48, M6W6ZB4PPX, FRK1ZGYB7X]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_constructions
same_as:
  wikidata: Q858320
  wikipedia: Calculus of constructions
---

## Summary

The calculus of constructions is a typed lambda calculus introduced by Thierry Coquand and Gérard Huet.
It combines the polymorphism of [[System F|SVNYKTGQ48]], type operators, and [[dependent types|M6W6ZB4PPX]] in one system, and it sits at the top of Barendregt's [[lambda cube|FRK1ZGYB7X]].
It is strongly normalizing, and as a logic it is a higher-order intuitionistic logic in which proofs are terms.
With inductive types added it became the basis of the proof assistant Coq, now called Rocq.

## Explanations

### L1 human

The calculus of constructions is a single small language for writing both programs and proofs.
Terms can depend on types, types can depend on types, and types can depend on terms.
It has a special type $\mathsf{Prop}$ whose elements are propositions, and a proof of a proposition is a term of that proposition.
For example, the statement "for every proposition $P$, $P$ implies $P$" is the type $\Pi P{:}\mathsf{Prop}.\, P \to P$, and the term $\lambda P{:}\mathsf{Prop}.\, \lambda x{:}P.\, x$ proves it.
