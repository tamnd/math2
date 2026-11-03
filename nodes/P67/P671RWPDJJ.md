---
tag: P671RWPDJJ
kind: concept
name: Connective constant
msc: [82B41, 05A16, 60K35]
sources:
  - url: https://en.wikipedia.org/wiki/Connective_constant
same_as:
  wikidata: Q5161701
  wikipedia: Connective constant
---

## Summary

The connective constant of a lattice is the exponential growth rate of the number of [[self-avoiding walks|E2BVEB570S]] on it.
Let $c_n$ be the number of self-avoiding walks of $n$ steps from a fixed vertex.
Then $c_n$ grows like $\mu^n$, and $\mu$ is the connective constant.
It is a basic quantity in the study of polymers and of critical phenomena on lattices.
Its exact value is known for very few lattices, the main one being the hexagonal lattice.

## Explanations

### L1 human

Count the paths of $n$ steps on a grid that never visit a point twice.
On the square grid there are $4$ such paths of one step, $12$ of two steps and $36$ of three steps.
At each step a walk has at most $3$ new directions, but sometimes fewer, because it must avoid its own past.
So the number of paths grows like $\mu^n$ for some $\mu$ between $2$ and $3$, and this $\mu$ is the connective constant of the square grid.
Numerically it is about $2.638$.
