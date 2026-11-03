---
tag: WDVJXWV3RF
kind: concept
name: Realization of a transfer function
msc: [93B15, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Realization_(systems)
same_as:
  wikidata: Q6554322
  wikipedia: Realization (systems)
---

## Summary

A realization of a [[transfer function|86JKV3TRFD]] is a state-space system $x' = Ax + Bu$, $y = Cx + Du$ whose transfer function is the given one.
It turns an input-output description into a model with internal states, which can be simulated, analysed and used for feedback design.
A transfer function has a realization exactly when it is a proper rational matrix, and its realizations are far from unique.
The smallest ones are the [[minimal realizations|3SNPPX5SAZ]].

## Explanations

### L1 human

A transfer function tells only how inputs become outputs; it says nothing about what happens inside.
A realization is a machine with internal memory, the state, that produces exactly the same input-output behaviour.
For example, $G(s) = 1/(s + 1)$ is realized by the single equation $x' = -x + u$ with output $y = x$.
Many other machines, with more internal states, have the same behaviour, just as many circuits can implement the same filter.
