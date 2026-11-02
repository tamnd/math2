---
tag: C5FG6ARWVV
kind: concept
name: Pseudorandom number generator
msc: [65C10, 11K45]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudorandom_number_generator
same_as:
  wikidata: Q1623338
  wikipedia: Pseudorandom number generator
---

## Summary

A pseudorandom number generator is a deterministic algorithm that produces a sequence of numbers meant to look like independent uniform random numbers.
It has a finite internal state, updated by a fixed map at each step.
An output function reads a number from the state.
Because the state space is finite, the sequence is eventually periodic, and the same seed always reproduces the same sequence.
Such generators supply the randomness of almost all Monte Carlo computations and simulations.

## Explanations

### L1 human

A computer cannot toss coins, but it can run a rule that scrambles a number again and again.
If the rule is good, the outputs pass statistical tests of randomness, even though each one is completely determined by the starting value, the seed.
A toy example is $s_{i+1} = 5 s_i + 1 \bmod 8$ with output $s_i/8$: from $s_0 = 0$ it gives $0, 1/8, 6/8, 7/8, 4/8, 5/8, 2/8, 3/8$ and then repeats.
Real generators work the same way with huge state spaces, so that the period is far longer than any computation.
Being reproducible is a feature: a simulation can be rerun exactly from its seed.
