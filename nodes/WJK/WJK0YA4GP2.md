---
tag: WJK0YA4GP2
kind: concept
name: Provability logic
msc: [03F45, 03B45]
specializes: [C3RZY20ETK]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
same_as:
  wikidata: Q260168
  wikipedia: Provability logic
---

## Summary

Provability logic is the [[modal logic|C3RZY20ETK]] in which $\square\varphi$ is read as "$\varphi$ is provable" in a formal theory such as Peano arithmetic.
Its main system $\mathrm{GL}$ is the normal modal logic given by Löb's axiom $\square(\square p \to p) \to \square p$.
By Solovay's theorem, $\mathrm{GL}$ proves exactly the modal laws of provability in Peano arithmetic, so questions about provability become finite combinatorics of Kripke frames.

## Explanations

### L1 human

Gödel showed that a formal theory can talk about its own proofs.
Provability logic collects the general laws of "it is provable that" into a small modal system.
One law is "if $p$ is provable, then it is provable that $p$ is provable", the formula $\square p \to \square\square p$.
"If $p$ is provable, then $p$" is not a law of the system.
With $p$ the false sentence $0 = 1$, it says that the theory is consistent, and by Gödel's second incompleteness theorem the theory cannot prove this.
