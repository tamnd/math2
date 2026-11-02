---
tag: ESVYD9CZ8C
kind: concept
name: Intuitionistic type theory
msc: ["03B38", "03F55", "03F50"]
specializes: [Q48KGV33AH]
uses: [Q48KGV33AH, Q11N8X99FK, A77FER1Q5H]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_type_theory
same_as:
  wikidata: Q6059147
  wikipedia: Intuitionistic type theory
---

## Summary

Intuitionistic type theory is the dependent [[type theory|Q48KGV33AH]] introduced by Per Martin-Löf from the 1970s on, also called Martin-Löf type theory.
It is a foundation of constructive mathematics based on [[intuitionistic logic|Q11N8X99FK]].
Through the [[Curry–Howard correspondence|A77FER1Q5H]], its types are also propositions, and its terms are both proofs and programs.
It is the basis of proof assistants such as Agda, and it is close to the systems behind Coq and Lean.

## Explanations

### L1 human

In this theory, a statement is a type, and a proof of the statement is an element of that type.
Types can depend on numbers or other data, as in "lists of length $n$".
A proof of "for every $n$ there is $m$ with $P(n, m)$" is a function that sends each $n$ to a pair: a number $m$ and a proof of $P(n, m)$.
So every proof of existence is also a program that computes the witness.
Checking a proof is the same as checking that a program has the right type.
