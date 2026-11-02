---
tag: 6KT3BJZ7D1
kind: concept
name: Natural deduction
msc: [03F03, 03B05]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
same_as:
  wikidata: Q1572108
  wikipedia: Natural deduction
---

## Summary

Natural deduction is a proof system whose rules mimic the way mathematicians reason.
Each connective has introduction rules, which say how to prove a formula with it, and elimination rules, which say how to use such a formula.
Assumptions can be made for a while and then discharged, as in "suppose $\varphi$; then ...; hence $\varphi \to \psi$".
It was introduced by Gerhard Gentzen, and independently by Stanisław Jaśkowski, and it is a basic system of [[proof theory|N4EDJNMTEF]].

## Explanations

### L1 human

To prove "if $A$ then $B$", you usually assume $A$ and show $B$.
Natural deduction turns this habit into a formal rule, called implication introduction.
Likewise, to prove "$A$ and $B$" you prove $A$ and prove $B$, and from "$A$ and $B$" you may conclude $A$.
Proofs are drawn as trees, with the assumptions at the leaves and the conclusion at the root.
Compared with a [[Hilbert system|1MGMQX43B8]], proofs are shorter and closer to ordinary arguments.
