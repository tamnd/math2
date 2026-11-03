---
tag: JWQQEZ1W00
kind: concept
name: Fixed-point combinator
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_combinator
same_as:
  wikidata: Q2976255
  wikipedia: Fixed-point combinator
---

## Summary

A fixed-point combinator is a closed lambda term $Y$ such that $Y\, F$ is a [[fixed point|R6QVS6P21N]] of $F$ for every term $F$.
This means that $Y\, F$ and $F\, (Y\, F)$ are equal under [[beta conversion|Y9B9CVY6SJ]].
Fixed-point combinators exist in the untyped [[lambda calculus|BD756KR8FM]], the best known being Curry's $Y$ and Turing's $\Theta$.
They make recursion possible in a language that has no names for functions.
They do not exist in the simply typed lambda calculus, which is strongly normalizing.

## Explanations

### L1 human

To define the factorial, one usually writes a function that calls itself by name.
The lambda calculus has no names, so this seems impossible.
The trick is to write a function $F$ that takes "the factorial" as an extra input and uses it for the recursive call.
The real factorial is then a fixed point of $F$: plugging it in gives it back.
A fixed-point combinator produces this fixed point automatically, for any $F$.
