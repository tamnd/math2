---
tag: 1MGMQX43B8
kind: concept
name: Hilbert system
msc: [03B05, 03F03]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
same_as:
  wikidata: Q910361
  wikipedia: Hilbert system
---

## Summary

A Hilbert system is a proof system with many axiom schemas and very few rules of inference, often only modus ponens.
A proof is a finite list of formulas in which each formula is an axiom, a hypothesis, or follows from earlier ones by a rule.
Hilbert systems are simple to describe and to reason about, which makes them the standard tool for results about provability.
They are named after David Hilbert.

## Explanations

### L1 human

In a Hilbert system, almost all the work is done by the axioms.
The only move is modus ponens: from $\varphi$ and $\varphi \to \psi$, write down $\psi$.
A proof is then just a numbered list of lines, each justified by an axiom or by modus ponens.
For example, the formula $p \to p$ has a proof of five lines in the usual system.
Such proofs are easy to check but often hard to find, which is why [[natural deduction|6KT3BJZ7D1]] was invented.
