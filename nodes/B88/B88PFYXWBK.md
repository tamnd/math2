---
tag: B88PFYXWBK
kind: concept
name: Infinite compositions of functions
msc: [40A30, 30D05]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_compositions_of_analytic_functions
---

## Summary

An infinite composition is the limit of the finite compositions $f_1 \circ f_2 \circ \cdots \circ f_n$, or of $f_n \circ \cdots \circ f_1$, of a sequence of functions.
It extends [[function composition|0THBK9V825]] to infinitely many factors, in the same way as a series extends a finite sum.
Continued fractions, nested radicals and power towers are all infinite compositions.
Iteration of a single function is the special case where all $f_n$ are equal.

## Explanations

### L1 human

Feed a starting value into $f_n$, feed the result into $f_{n-1}$, and so on down to $f_1$.
Doing this for larger and larger $n$ gives a sequence of numbers, and the infinite composition is its limit when it exists.
For example, the continued fraction $\cfrac{1}{2 + \cfrac{1}{2 + \cdots}}$ comes from composing the maps $w \mapsto \frac{1}{2 + w}$ and evaluating at $0$.
