---
tag: AYVTR2ES5B
kind: concept
name: Iterated function
msc: [37B02, 26A18, 37-01]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function
same_as:
  wikidata: Q5254619
  wikipedia: Iterated function
---

## Summary

An iterated function is a map of a set to itself composed with itself a given number of times.
The $n$-th iterate $f^n$ applies $f$ exactly $n$ times.
Iterates are the basic objects of discrete-time dynamics: the state after $n$ steps is $f^n$ of the initial state.
They also appear in [[fixed-point iteration|K6ZF91051B]], fractals and the study of functional equations.

## Explanations

### L1 human

Apply a function, then apply it again to the result, and keep going.
The $n$-th iterate is what one gets after $n$ rounds.
For $f(x) = x + 3$, the iterate $f^n$ is $x \mapsto x + 3n$.
For $f(x) = 2x$, the iterate $f^n$ is $x \mapsto 2^n x$.
Pressing the cosine key of a calculator many times, in radian mode, computes iterates of $\cos$, and the display settles near $0.739$.
