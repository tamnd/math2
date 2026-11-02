---
tag: WEMJBN339R
kind: concept
name: Axiom of dependent choice
msc: ["03E25"]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_of_dependent_choice
same_as:
  wikidata: Q3303153
  wikipedia: Axiom of dependent choice
---

## Summary

The axiom of dependent choice, DC, allows a sequence of countably many choices.
Each choice may depend on the choices made before.
It is weaker than the full [[axiom of choice|0HTGB13FE2]] and stronger than the axiom of countable choice.
It is the form of choice that most of real analysis needs, and the [[precise statement|TPXEFSBQYB]] uses a binary relation with no dead ends.

## Explanations

### L1 human

Imagine a game where from every position there is at least one legal move.
Dependent choice says you can then play forever: there is an infinite sequence of positions, each one a legal move from the one before.
For a finite number of moves this needs no axiom, but an infinite run needs infinitely many choices made one after another.
For example, let $R$ be a relation on the real numbers such that each $x$ is related to at least one $y > x$.
Then DC gives a sequence $x_0 < x_1 < x_2 < \cdots$ in which each term is related to the next.
When there is no explicit rule that picks $y$ from $x$, the axiom is what makes the sequence exist.
