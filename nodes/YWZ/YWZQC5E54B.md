---
tag: YWZQC5E54B
kind: concept
name: Rate of convergence
msc: [40A05, 65B99]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_of_convergence
same_as:
  wikidata: Q1783502
  wikipedia: Rate of convergence
---

## Summary

The rate of convergence of a convergent sequence measures how fast its distance to the limit shrinks.
One compares the error at step $k+1$ with a power of the error at step $k$.
The exponent is the order of convergence, such as linear or quadratic.
It is the standard way to compare iterative methods in numerical analysis.
Two examples are [[fixed-point iteration|K6ZF91051B]] and [[Newton's method|07EXVNF9VP]].

## Explanations

### L1 human

Two sequences can have the same limit and still approach it at very different speeds.
With linear convergence, each step multiplies the error by about the same factor, so one gains correct digits at a steady pace.
With quadratic convergence, each error is about the square of the previous error, so the number of correct digits roughly doubles at each step.
For example, $2^{-k}$ tends to $0$ linearly, while $2^{-2^k}$ tends to $0$ quadratically.
