---
tag: SVNYKTGQ48
kind: concept
name: System F
msc: [03B40, 03B38, 68N18]
uses: [2DP940895E]
sources:
  - url: https://en.wikipedia.org/wiki/System_F
same_as:
  wikidata: Q2552799
  wikipedia: System_F
---

## Summary

System F, also called the polymorphic lambda calculus or second-order lambda calculus, extends the [[simply typed lambda calculus|2DP940895E]] with quantification over types.
It was introduced independently by Jean-Yves Girard in logic and by John C. Reynolds in programming languages.
A term of type $\forall \alpha.\, \tau$ works uniformly for every type $\alpha$, which models generic programs.
Girard proved that every typed term of System F is strongly normalizing, and under the Curry–Howard correspondence it matches second-order intuitionistic propositional logic.

## Explanations

### L1 human

In the simply typed calculus there is one identity function for each type: one for numbers, one for truth values, and so on.
System F has a single identity $\Lambda \alpha.\, \lambda x{:}\alpha.\, x$ of type $\forall \alpha.\, \alpha \to \alpha$.
To use it on numbers, one first passes the type of numbers as an argument, and then the number.
Types become things that a program can take as input.
Natural numbers, pairs and lists can all be encoded in pure System F with such types.
