---
tag: QR92EZDTKF
kind: concept
name: Horn clause
msc: ["03B05", "03B70", "08C15"]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
same_as:
  wikidata: Q933932
  wikipedia: Horn clause
---

## Summary

A Horn clause is a disjunction of literals in which at most one literal is unnegated.
Such a clause can be read as a rule: "if all of these hold, then that holds".
With no unnegated literal, it is a constraint: "these do not all hold".
Satisfiability of a [[conjunctive normal form|0B3D4C8YF2]] made of Horn clauses can be decided in polynomial time, unlike general [[satisfiability|QN7M1JCGT9]].
Horn clauses are the basis of logic programming, and their first-order universal forms axiomatize [[universal Horn classes|9A4CYWXPEA]] and [[quasivarieties|WRXEKT4NQS]].

## Explanations

### L1 human

The clause $\neg p \vee \neg q \vee r$ says the same as "if $p$ and $q$, then $r$".
Rules of this shape can be chained: from known facts one keeps deriving new facts until nothing changes.
This is why Horn formulas are easy to solve, while clauses such as $p \vee q$, which allow a choice, make satisfiability hard in general.
A clause with no positive literal, such as $\neg p \vee \neg q$, says "not both $p$ and $q$".
