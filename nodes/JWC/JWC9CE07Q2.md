---
tag: JWC9CE07Q2
kind: concept
name: PSPACE-completeness
msc: [68Q17, 68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/PSPACE-complete
same_as:
  wikidata: Q905967
  wikipedia: PSPACE-complete
---

## Summary

A decision problem is PSPACE-complete when it lies in [[PSPACE|T9NTRY93ZT]] and every problem in PSPACE reduces to it by a [[polynomial-time reduction|V0K79AD81V]].
These are the hardest problems in PSPACE.
The truth of quantified Boolean formulas is the standard example, and many questions about winning strategies in games are PSPACE-complete.
A PSPACE-complete problem in P would give $\mathrm{P} = \mathrm{PSPACE}$, and one in NP would give $\mathrm{NP} = \mathrm{PSPACE}$.

## Explanations

### L1 human

Some problems need little memory but seem to need a huge amount of time.
Deciding whether the first player can force a win in the game of Hex on an $n \times n$ board is a typical case.
The PSPACE-complete problems are the hardest of these: a fast method for one would give a fast method for every problem solvable with polynomial memory.
They are believed to be even harder than the NP-complete problems.
