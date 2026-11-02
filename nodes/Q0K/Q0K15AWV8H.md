---
tag: Q0K15AWV8H
kind: concept
name: Linear congruential generator
msc: [65C10, 11K45]
specializes: [C5FG6ARWVV]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_congruential_generator
same_as:
  wikidata: Q1190228
  wikipedia: Linear congruential generator
---

## Summary

A linear congruential generator is a [[pseudorandom number generator|C5FG6ARWVV]] whose state is an integer modulo $m$, updated by an affine map $x \mapsto (ax + c) \bmod m$.
It is one of the oldest and simplest generators, and its period and lattice structure can be analysed completely with elementary number theory.
Its weaknesses, such as short periods of the low-order bits and points lying on few hyperplanes, made it a classic lesson in generator design.

## Explanations

### L1 human

Take a number, multiply it by a fixed number, add another fixed number, and keep only the remainder after division by a modulus $m$.
Repeat, and divide each result by $m$ to get numbers between $0$ and $1$.
With $m = 8$, multiplier $5$ and increment $1$, starting from $0$, the states are $0, 1, 6, 7, 4, 5, 2, 3$ and then the cycle repeats.
In practice $m$ is huge, such as $2^{64}$, so that the cycle is far longer than any computation.
The same simplicity that makes the generator fast also makes its patterns easy to detect, so it is no longer the default choice in serious simulations.
