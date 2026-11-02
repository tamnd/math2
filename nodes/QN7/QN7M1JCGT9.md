---
tag: QN7M1JCGT9
kind: concept
name: Satisfiability
msc: [03B05, 03B10]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
same_as:
  wikidata: Q1350299
  wikipedia: Satisfiability
---

## Summary

A formula is satisfiable when some interpretation makes it true.
In [[propositional logic|09K9MWD2QQ]] an interpretation is an assignment of truth values to the variables.
In [[predicate logic|086QKPF0A6]] it is a [[structure|983GZBQYT4]] with an assignment of its elements to the free variables.
Satisfiability is dual to validity: a formula is valid exactly when its negation is not satisfiable.

## Explanations

### L1 human

A formula is satisfiable when it is possible to make it true.
For example, $p \land \neg q$ is satisfiable: take $p$ true and $q$ false.
The formula $p \land \neg p$ is not satisfiable, since $p$ cannot be true and false at once.
Deciding satisfiability of propositional formulas is the SAT problem, a central problem of computer science.
