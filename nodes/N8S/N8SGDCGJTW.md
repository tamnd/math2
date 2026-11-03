---
tag: N8SGDCGJTW
kind: concept
name: Operational semantics
msc: [68Q55, 68N15]
uses: [05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_semantics
same_as:
  wikidata: Q1930895
  wikipedia: Operational semantics
---

## Summary

Operational semantics gives meaning to a programming language by describing how its programs execute, as steps of an abstract machine on the program text.
The steps are given by inference rules that follow the syntax of the language.
In the small-step, or structural, style of Gordon Plotkin, the rules define single computation steps.
In the big-step, or natural, style of Gilles Kahn, they relate a program directly to its final result.
It is the standard tool for defining languages precisely and for proving properties such as type safety.

## Explanations

### L1 human

To explain what a program does, one can simply say how it runs.
Operational semantics writes down these running rules exactly, as a game of rewriting the program.
For example, the expression $(1 + 2) \cdot 4$ first steps to $3 \cdot 4$ and then to $12$.
A program that loops forever is one whose steps never end.
