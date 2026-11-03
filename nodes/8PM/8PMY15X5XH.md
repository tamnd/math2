---
tag: 8PMY15X5XH
kind: concept
name: CYK algorithm
msc: [68Q45, 68Q42, 68W40]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/CYK_algorithm
same_as:
  wikidata: Q954821
  wikipedia: CYK algorithm
---

## Summary

The Cocke–Younger–Kasami (CYK) algorithm decides whether a word belongs to the language of a [[context-free grammar|CTCY2R8Q77]] in [[Chomsky normal form|7TMGSPXKJ3]].
It is a [[dynamic programming|R3FXF08WBH]] method that finds, for each substring of the word, the set of nonterminals that derive it.
It runs in time cubic in the length of the word, so the membership problem for [[context-free languages|Q56EWEQYE2]] is solvable in polynomial time.
It also yields parse trees, so it serves as a general parsing algorithm.

## Explanations

### L1 human

The algorithm fills a triangular table from short pieces of the word to long ones.
For each single letter it writes down which placeholders produce that letter.
For a longer piece it tries every way to cut it into two parts and checks whether a rule $A \to BC$ fits the two parts.
At the end the word is in the language exactly when the start symbol appears in the cell for the whole word.
