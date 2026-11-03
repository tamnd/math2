---
tag: CF5Y39BPB0
kind: concept
name: Separation logic
msc: [68Q60, 03B70, 03B47]
uses: [H1M6RSBJ5H]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_logic
same_as:
  wikidata: Q3257964
  wikipedia: Separation logic
---

## Summary

Separation logic is an extension of [[Hoare logic|H1M6RSBJ5H]] for reasoning about programs that use pointers and mutable memory.
It was developed around 2000 by John C. Reynolds, Peter O'Hearn, Samin Ishtiaq and Hongseok Yang.
Its key connective is the separating conjunction $P * Q$, which says that memory splits into two disjoint parts, one satisfying $P$ and the other $Q$.
The frame rule then extends a proof about the memory that a command touches to any larger memory.
This makes proofs local and scalable.

## Explanations

### L1 human

Programs that change memory through pointers are hard to reason about, because two names may point to the same cell.
Separation logic describes memory as a collection of cells and lets one say "these cells and those cells are different".
The assertion $x \mapsto 3 * y \mapsto 4$ says that $x$ points to a cell holding $3$, $y$ points to a cell holding $4$, and the two cells are distinct.
Then a write through $x$ cannot change what $y$ points to, and the logic uses this fact automatically.
