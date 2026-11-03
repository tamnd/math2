---
tag: VNY0VXVZ53
kind: concept
name: Model checking
msc: [68Q60, 03B44, 03B70]
sources:
  - url: https://en.wikipedia.org/wiki/Model_checking
same_as:
  wikidata: Q1569697
  wikipedia: Model checking
---

## Summary

Model checking is the problem of deciding whether a finite model of a system satisfies a specification written in a temporal logic.
The model is usually a finite [[Kripke structure|NGHWZ9Y7ZV]], and the specification a formula of [[linear temporal logic|RMJ56ZPA63]], [[computation tree logic|F6JA5C5BJX]] or the [[modal mu-calculus|MZ0M2KR9S0]].
It is a fully automatic method of verification: when the property fails, the algorithm can return a counterexample run.

## Explanations

### L1 human

Write down every state a program or a circuit can be in, and the moves between states.
Write the property you want, for example "two processes are never in the critical section at once", in a temporal logic.
A model checker then explores the states and either confirms the property or prints a run that breaks it.
The main obstacle is that the number of states grows exponentially with the number of components, the state explosion problem.
