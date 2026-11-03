---
tag: HFD162F9PH
kind: concept
name: Ambiguous grammar
msc: [68Q42, 68Q45]
specializes: [CTCY2R8Q77]
sources:
  - url: https://en.wikipedia.org/wiki/Ambiguous_grammar
same_as:
  wikidata: Q1917459
  wikipedia: Ambiguous grammar
---

## Summary

A [[context-free grammar|CTCY2R8Q77]] is ambiguous when some word it generates has two different parse trees.
Ambiguity matters because the parse tree carries the meaning of a word, for example the order in which operations are applied.
Some ambiguous grammars can be replaced by unambiguous ones for the same language, but some [[context-free languages|Q56EWEQYE2]] are inherently ambiguous.
Whether a given context-free grammar is ambiguous is undecidable.

## Explanations

### L1 human

A grammar is ambiguous if one sentence can be built in two structurally different ways.
With the rules $E \to E - E$ and $E \to x$, the word $x - x - x$ can be grouped as $(x - x) - x$ or as $x - (x - x)$.
These two readings give different values, so a compiler must know which one is meant.
Rewriting the grammar as $E \to E - x$ and $E \to x$ forces the first grouping and removes the ambiguity.
