---
tag: DP1HXZGPCM
kind: concept
name: Formal grammar
msc: [68Q42, 68Q45, 03D05]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_grammar
same_as:
  wikidata: Q373045
  wikipedia: Formal grammar
---

## Summary

A formal grammar is a finite set of rewriting rules that produces strings over an [[alphabet|RABRP2KG81]].
Starting from a start symbol, one replaces parts of the current string by the rules until only terminal letters remain.
The strings obtained in this way form the [[formal language|5MFZ4VNY6D]] of the grammar.
Grammars give finite descriptions of infinite languages, and restrictions on the form of the rules sort languages into classes of different power.

## Explanations

### L1 human

A grammar is a recipe for building sentences.
Some symbols are placeholders, such as "sentence" or "noun", and the rules say how a placeholder may be replaced.
When no placeholder is left, the result is a finished sentence of the language.
For example, the two rules $S \to aSb$ and $S \to \varepsilon$ build $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aabb$.
These rules produce exactly the strings $a^n b^n$ with $n \ge 0$.
