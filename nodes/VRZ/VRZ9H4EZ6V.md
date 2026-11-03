---
tag: VRZ9H4EZ6V
kind: concept
name: L
msc: [68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/L_(complexity)
same_as:
  wikidata: Q1192782
  wikipedia: L (complexity)
---

## Summary

L is the [[complexity class|ESPYW94XGR]] of decision problems that a deterministic Turing machine can solve with logarithmic [[space|FDNFGKEEJR]].
The machine reads its input freely but may only write a fixed number of counters or pointers into the input.
L lies inside [[P|GVT2NKN37K]], and it is the smallest of the standard space classes.
It is also called LOGSPACE.

## Explanations

### L1 human

Imagine a reader who can look at any part of a huge document but may only take notes on a few small slips of paper.
Each slip holds one number, such as a position in the document or a count.
L is the class of yes-or-no questions that such a reader can answer.
For example, checking that a string of brackets is balanced only needs one counter for the current depth.
