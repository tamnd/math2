---
tag: E2BVEB570S
kind: concept
name: Self-avoiding walk
msc: [82B41, 60K35, 05A16]
sources:
  - url: https://en.wikipedia.org/wiki/Self-avoiding_walk
same_as:
  wikidata: Q7448025
  wikipedia: Self-avoiding walk
---

## Summary

A self-avoiding walk is a path on a lattice that never visits the same point twice.
Counting such walks and describing a typical long one are hard problems, much harder than for [[random walks|04VZE3FZXF]].
The growth rate of their number is the connective constant of the lattice.
Self-avoiding walks are a model of long polymer molecules, which cannot occupy the same place twice.

## Explanations

### L1 human

Draw a path on squared paper along the grid lines, one unit step at a time, and never come back to a corner you have visited.
That path is a self-avoiding walk.
On the square grid there are $4$ walks of one step, $12$ of two steps and $36$ of three steps.
The number grows roughly like $\mu^n$ for some number $\mu$ between $2$ and $3$.
