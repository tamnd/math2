---
tag: 7TMGSPXKJ3
kind: concept
name: Chomsky normal form
msc: [68Q42, 68Q45]
specializes: [CTCY2R8Q77]
sources:
  - url: https://en.wikipedia.org/wiki/Chomsky_normal_form
same_as:
  wikidata: Q1076039
  wikipedia: Chomsky normal form
---

## Summary

A [[context-free grammar|CTCY2R8Q77]] is in Chomsky normal form when each rule either replaces a nonterminal by two nonterminals or by one terminal letter.
Every [[context-free language|Q56EWEQYE2]] has a grammar in this form.
The rigid shape makes parse trees binary, which simplifies proofs such as the pumping lemma and algorithms such as CYK parsing.

## Explanations

### L1 human

Chomsky normal form is a tidy way to write a context-free grammar.
Every rule either splits one placeholder into exactly two placeholders or turns it into one letter.
So every parse tree is a binary tree, with a single letter hanging under each leaf placeholder.
For example, the rules $S \to AB \mid AC$, $T \to AB \mid AC$, $C \to TB$, $A \to a$, $B \to b$ generate the words $a^n b^n$ with $n \ge 1$.
Here $T$ produces the same words as $S$, and $C$ produces $a^n b^{n+1}$.
