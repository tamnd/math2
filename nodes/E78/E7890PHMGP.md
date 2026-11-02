---
tag: E7890PHMGP
kind: concept
name: Functional square root
msc: [39B12, 26A18]
specializes: [27C6J3YNZY]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_square_root
same_as:
  wikidata: Q3890203
  wikipedia: Functional square root
---

## Summary

A functional square root of a map $f$ is a map $g$ with $g(g(x)) = f(x)$ for all $x$.
It is the [[iterative root|27C6J3YNZY]] of order $2$, and it is often called a half-iterate of $f$.
It answers the question of what it means to apply $f$ half a time.
Functional square roots of the exponential function and of other simple maps have a long history in iteration theory.

## Explanations

### L1 human

Squaring a number has an inverse question: which number squared gives the result?
For maps, the analogue of squaring is applying the map twice.
A functional square root of $f$ is a map that, done twice, has the same effect as $f$ done once.
For $f(x) = x + 2$ one root is $g(x) = x + 1$; for $f(x) = 4x$ two roots are $2x$ and $-2x$.
