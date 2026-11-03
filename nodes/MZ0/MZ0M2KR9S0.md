---
tag: MZ0M2KR9S0
kind: concept
name: Modal mu-calculus
msc: [03B45, 03B70, 68Q60]
specializes: [C3RZY20ETK]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
same_as:
  wikidata: Q5275729
  wikipedia: Modal μ-calculus
---

## Summary

The modal $\mu$-calculus extends [[modal logic|C3RZY20ETK]] with a least fixed point operator $\mu$ and a greatest fixed point operator $\nu$.
Formulas are evaluated at the states of a labelled transition system, and fixed points express recursive properties such as reachability and invariance.
It contains [[computation tree logic|F6JA5C5BJX]] and [[linear temporal logic|RMJ56ZPA63]] by translation, so it serves as a common target logic for [[model checking|VNY0VXVZ53]].

## Explanations

### L1 human

Plain modal logic can only look a fixed number of steps ahead.
Fixed points let a formula refer to itself, like a recursive definition.
The formula $\mu X.\,(p \lor \lozenge X)$ says "either $p$ holds here, or one step leads to a state where this same formula holds".
The least solution of that equation is the set of states from which some path reaches a $p$-state.
Greatest fixed points describe properties that hold forever, such as "$p$ holds along every path".
