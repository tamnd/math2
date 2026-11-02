---
tag: CQMK4YPE1J
kind: concept
name: Mollifier
msc: ["46E35", 46F10, 42B35]
specializes: [HS65DW0HXH]
sources:
  - url: https://en.wikipedia.org/wiki/Mollifier
same_as:
  wikidata: Q2318637
  wikipedia: Mollifier
---

## Summary

A mollifier is a smooth, nonnegative [[bump function|HS65DW0HXH]] with integral $1$, supported in the unit ball.
Rescaling it gives a family $\varphi_\varepsilon$ that concentrates at the origin as $\varepsilon \to 0$.
[[Convolution|2Z29JN3VES]] with $\varphi_\varepsilon$ turns a rough function into a [[smooth function|0V33BNKZ9S]] that is close to it.
Mollifiers are the standard tool to approximate functions, prove density results and regularize distributions.

## Explanations

### L1 human

Think of a mollifier as a small smooth blob of total mass $1$.
Convolving a function with the blob replaces each value by a weighted average of the nearby values.
This blurs away corners and jumps, and the result is infinitely differentiable.
If the blob is made narrower, the averages are taken over smaller regions, and the blurred function gets closer to the original one.
A standard blob on the line is $c \, e^{-1/(1 - x^2)}$ for $\abs{x} < 1$ and $0$ elsewhere.
