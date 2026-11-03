---
tag: 69VWJKXK74
kind: concept
name: Root locus
msc: [93B55, 93C05, 30C15]
sources:
  - url: https://en.wikipedia.org/wiki/Root_locus_analysis
same_as:
  wikidata: Q957693
  wikipedia: Root locus analysis
---

## Summary

The root locus of a feedback loop is the set of paths of the closed-loop poles in the [[complex plane|0CTE7A31XQ]].
The paths are traced as a gain $K$ grows from $0$ to $\infty$.
They start at the open-loop poles and end at the open-loop zeros or go off to infinity.
Simple rules let one sketch the locus by hand.
From it one chooses a gain that puts the closed-loop poles where the response is fast and well damped.

## Explanations

### L1 human

A feedback loop has a knob, the gain, and each setting of the knob gives a set of closed-loop poles that decide how the system behaves.
Turning the knob moves the poles, and the root locus is the picture of their paths.
Poles in the left half-plane mean a stable system, so one can see at which gain the loop becomes unstable.
For $G(s) = 1/(s(s + 2))$ the two poles start at $0$ and $-2$, meet at $-1$ when $K = 1$, and then move up and down the vertical line $\operatorname{Re} s = -1$.
