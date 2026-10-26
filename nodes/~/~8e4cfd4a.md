---
tag: ~8e4cfd4a
kind: definition
name: Conditional convergence
aliases: [conditionally-convergent-series]
msc: [40A05]
defines: ~8ebd64c5
uses: [~b727755f, ~2aabc312]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_convergence
    locator: Definition
---

## Definition

Let $(a_n)$ be a real sequence.
The series $\sum a_n$ converges conditionally if $\sum a_n$ [[converges|~b727755f]] and $\sum |a_n|$ diverges.

## Remarks

So a convergent series converges either [[absolutely|~2aabc312]] or conditionally, and not both.
The [[alternating harmonic series|~18f79025]] converges conditionally.
By the [[Riemann rearrangement theorem|~74543509]], the terms of a conditionally convergent series can be reordered to give any real sum.

## Explanations

### L1 human

A conditionally convergent series converges only because its positive and negative terms cancel.
The positive terms alone add up to $+\infty$, and the negative terms alone add up to $-\infty$.
