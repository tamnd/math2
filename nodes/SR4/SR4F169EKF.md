---
tag: SR4F169EKF
kind: concept
name: Wright–Fisher model
msc: [92D10, 92D15, 60J10]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_drift
---

## Summary

The Wright–Fisher model is the basic stochastic model of [[genetic drift|AFJ02FJ1KR]] in a population of constant size with non-overlapping generations.
Each generation is formed by sampling gene copies with replacement from the previous generation.
It is named after Sewall Wright and Ronald Fisher.
Its large population limit is a diffusion, which leads to [[Kimura's diffusion approximation|2DEPWNNN63]].

## Explanations

### L1 human

Imagine a population of $10$ gene copies, $3$ of type $A$ and $7$ of type $a$.
To make the next generation, pick a parent at random $10$ times, allowing the same parent to be picked again, and copy its type.
The new number of $A$ copies is random, with mean $3$.
Repeating this, the number of $A$ copies wanders until it hits $0$ or $10$, and then it stays there forever.
