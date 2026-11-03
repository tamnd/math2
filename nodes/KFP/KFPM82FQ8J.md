---
tag: KFPM82FQ8J
kind: concept
name: Weakly almost periodic function
msc: ["43A60", "46A03"]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Summary

A weakly almost periodic function on a topological group is a bounded continuous function with a special property.
Its translates form a relatively compact set for the weak topology of the space of bounded continuous functions.
The notion, due to Eberlein, weakens the uniform compactness that defines [[almost periodic functions|N9WKQ0MSEK]].
Every almost periodic function is weakly almost periodic, and on a locally compact group so is every continuous function vanishing at infinity.
The weakly almost periodic functions carry a unique invariant mean, which makes them a natural setting for mean ergodic theorems.

## Explanations

### L1 human

For an almost periodic function, the shifted copies stay close to finitely many functions in the uniform sense.
For a weakly almost periodic function one asks less: the shifted copies only have to cluster when they are tested against averages, not point by point uniformly.
A bump on $\Z$, which is $1$ at $0$ and $0$ elsewhere, is a typical example: its shifts run off to infinity and fade to $0$ in the weak sense.
A step that is $0$ on the negatives and $1$ on the rest of $\Z$ is not weakly almost periodic.
