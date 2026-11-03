---
tag: 9DMSG5HAQX
kind: concept
name: Algorithm
msc: [68W01, 68Q10]
sources:
  - url: https://en.wikipedia.org/wiki/Algorithm
same_as:
  wikidata: Q8366
  wikipedia: Algorithm
---

## Summary

An algorithm is a finite, precise list of instructions that transforms an input into an output by a sequence of elementary steps.
Each step is determined by the instructions and the current data, and for every admissible input the process stops after finitely many steps.
Algorithms are the objects that computer science designs and analyses, and the [[Turing machine|758EYCN27B]] gives one standard way to make the notion mathematically exact.

## Explanations

### L1 human

A recipe is a good picture: a fixed list of steps that anyone can follow mechanically, without insight.
Long division, taught in school, is an algorithm: it works for every pair of numbers and always ends.
The [[Euclidean algorithm|0TRNT4X7J0]] is another: replace the pair $(a, b)$ by $(b, a \bmod b)$ until the second number is $0$.
For $(12, 8)$ it gives $(8, 4)$ and then $(4, 0)$, so the greatest common divisor is $4$.
