---
tag: D1T39KHPDN
kind: problem
name: Suslin's problem
msc: ["03E50", "03E35", "03E05"]
uses: [0316AYH1SC, MCDP25YMSE, 0GKJ78948V]
about: [MCDP25YMSE]
sources:
  - url: https://en.wikipedia.org/wiki/Suslin's_problem
same_as:
  wikidata: Q2296408
  wikipedia: Suslin's problem
history:
  posed_by: "Mikhail Suslin"
  first_stated: "1920"
---

## Problem

Let $(L, <)$ be a nonempty [[total order|0316AYH1SC]] with these properties:

1. $L$ has no least and no greatest element.
2. $L$ is dense: between any two elements there is a third.
3. $L$ is complete: each nonempty subset of $L$ that is bounded above has a least upper bound.
4. Each family of pairwise disjoint nonempty open intervals of $L$ is countable.

Must $L$ be order isomorphic to the real line $\R$?

## Remarks

The real line is characterised by clauses 1 to 3 together with separability: $L$ has a countable subset that meets each nonempty open interval.
So the question asks whether the countable chain condition, clause 4, can replace [[separability|0GKJ78948V]].
A counterexample is called a Suslin line, and Suslin's hypothesis says that no Suslin line exists.
The problem is independent of ZFC, if ZFC is consistent.
Jensen showed that the [[diamond principle|HFQSSB1Z23]], which holds in the constructible universe, implies that a Suslin line exists.
Solovay and Tennenbaum showed that Suslin's hypothesis is consistent, and it follows from [[Martin's axiom|Z8XMCCZFA4]] together with the failure of the continuum hypothesis.
A Suslin line exists if and only if a Suslin tree exists, that is, an [[Aronszajn tree|KKT4JYJEJJ]] in which each antichain is countable.

## Explanations

### L1 human

The real numbers form a line with no ends and no gaps, and a countable set, the rationals, is spread all through it.
Suslin asked whether a weaker condition can replace the countable dense set: that one can only fit countably many disjoint intervals into the line.
The answer turned out to be that the usual axioms of mathematics cannot decide the question.
In some models of set theory there are strange lines, Suslin lines, that pass this test but are not the real line.
