---
tag: CTCY2R8Q77
kind: concept
name: Context-free grammar
msc: [68Q42, 68Q45]
specializes: [DP1HXZGPCM]
sources:
  - url: https://en.wikipedia.org/wiki/Context-free_grammar
same_as:
  wikidata: Q338047
  wikipedia: Context-free grammar
---

## Summary

A context-free grammar is a [[formal grammar|DP1HXZGPCM]] in which every rule replaces a single nonterminal symbol by a string.
The replacement does not depend on the symbols around the nonterminal, which is why the grammar is called context-free.
Context-free grammars describe nested structure, such as balanced brackets and arithmetic expressions.
They are the standard tool for the syntax of programming languages and for parsing.

## Explanations

### L1 human

In a context-free grammar each rule has one placeholder on the left, such as $E \to E + E$.
Any copy of that placeholder may be replaced at any time, whatever stands next to it.
A derivation can be drawn as a tree: each placeholder is a node, and its children are the symbols that replace it.
For example, $E \to E + E$, $E \to (E)$ and $E \to x$ produce expressions such as $(x + x) + x$.
