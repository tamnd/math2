---
tag: 36DXKAD2RZ
kind: concept
name: Dini derivative
msc: [26A24]
sources:
  - url: https://en.wikipedia.org/wiki/Dini_derivative
same_as:
  wikidata: Q831933
  wikipedia: Dini derivative
---

## Summary

The Dini derivatives of a real function at a point are the four one-sided upper and lower limits of its [[difference quotients|AZBDB5F4M4]].
Unlike the [[derivative|0F1WR9C83K]], they always exist, possibly as $+\infty$ or $-\infty$.
A function is differentiable at a point exactly when its four Dini derivatives there are equal and finite.
They are the main tool for proving differentiability almost everywhere, as in [[Lebesgue's theorem on monotone functions|1Y4N1DDQNR]].

## Explanations

### L1 human

At a corner or a wiggle, the slope of a function may fail to have a limit.
Dini derivatives still record what happens: the largest and smallest slopes seen from the right, and the largest and smallest seen from the left.
For $\abs{x}$ at $0$, the slopes from the right are all $1$ and the slopes from the left are all $-1$.
So the right Dini derivatives are $1$ and the left ones are $-1$.
