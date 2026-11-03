---
tag: H1M6RSBJ5H
kind: concept
name: Hoare logic
msc: [68Q60, 03B70]
uses: [086QKPF0A6, N8SGDCGJTW]
sources:
  - url: https://en.wikipedia.org/wiki/Hoare_logic
same_as:
  wikidata: Q1375924
  wikipedia: Hoare logic
---

## Summary

Hoare logic is a formal system for proving that imperative programs are correct.
C. A. R. Hoare introduced it in 1969, building on earlier work of Robert W. Floyd.
Its statements are Hoare triples $\set{P}\, C\, \set{Q}$: if the precondition $P$ holds before the command $C$ runs and $C$ terminates, then the postcondition $Q$ holds afterwards.
It has one axiom or rule for each construct of the language, so a proof follows the structure of the program.
It is sound for the [[operational semantics|N8SGDCGJTW]] of the language, and it is the ancestor of most program verification methods.

## Explanations

### L1 human

A Hoare triple is a promise about a piece of code: "if this is true before, then that is true after".
For example, $\set{x = 1}\ x := x + 1\ \set{x = 2}$ says that adding one to a variable equal to $1$ makes it equal to $2$.
Hoare logic gives rules to combine such promises for small pieces into promises for whole programs.
For a loop, one finds an invariant, a statement that stays true each time round the loop.
