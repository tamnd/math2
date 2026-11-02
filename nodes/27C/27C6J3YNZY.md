---
tag: 27C6J3YNZY
kind: concept
name: Iterative root
msc: [39B12, 26A18]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_square_root
---

## Summary

An iterative root of order $n$ of a map $f$ is a map $g$ whose $n$-th [[iterate|AYVTR2ES5B]] is $f$, that is, $g \circ g \circ \cdots \circ g = f$ with $n$ factors.
It is the analogue for composition of the $n$-th root of a number.
Iterative roots may fail to exist, and when they exist there are often many of them.
The search for them is one of the classical problems of iteration theory.

## Explanations

### L1 human

Think of $f$ as a step of a process, and ask for a smaller step $g$ such that $n$ small steps make one big step.
For $f(x) = x + 3$, the map $g(x) = x + 1$ is an iterative root of order $3$, since three shifts by $1$ make a shift by $3$.
For $f(x) = 8x$, the map $g(x) = 2x$ is an iterative root of order $3$.
Some maps have no nice root: no continuous map $g$ of the real line satisfies $g(g(x)) = -x$.
