---
tag: JFP48QARQS
kind: concept
name: Greibach normal form
msc: [68Q42, 68Q45]
specializes: [CTCY2R8Q77]
sources:
  - url: https://en.wikipedia.org/wiki/Greibach_normal_form
same_as:
  wikidata: Q1499325
  wikipedia: Greibach normal form
---

## Summary

A [[context-free grammar|CTCY2R8Q77]] is in Greibach normal form when the right side of each rule starts with a terminal letter followed only by nonterminals.
Every [[context-free language|Q56EWEQYE2]] without the empty word has a grammar in this form.
With a special rule for the empty word, every context-free language has one.
In such a grammar each derivation step produces exactly one letter of the word.
This form turns a grammar into a pushdown automaton that reads one letter per move.
It also shows that left recursion can always be removed.

## Explanations

### L1 human

In Greibach normal form each rule writes one letter first and then some placeholders.
So a nonempty word of length $n$ is built in exactly $n$ steps, one letter per step, from left to right.
For example, the rules $S \to aSB$, $S \to aB$, $B \to b$ build $S \Rightarrow aSB \Rightarrow aaBB \Rightarrow aabB \Rightarrow aabb$.
They generate the words $a^n b^n$ with $n \ge 1$.
