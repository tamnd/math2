---
tag: 9PXSRZEDPY
kind: concept
name: NK model
msc: [92D15]
specializes: [6AEH5ZDDBQ]
sources:
  - url: https://en.wikipedia.org/wiki/NK_model
same_as:
  wikidata: Q6954615
  wikipedia: NK model
---

## Summary

The NK model is a family of random [[fitness landscapes|6AEH5ZDDBQ]] on binary strings of length $N$ whose ruggedness is tuned by a parameter $K$.
Each site contributes to fitness through a random function of its own state and of the states of $K$ other sites.
With $K = 0$ the landscape is smooth with a single peak; with $K = N - 1$ it is completely random with many peaks.
It is a standard model of epistasis in evolution and is also used in the study of organisations and optimisation.

## Explanations

### L1 human

Think of a genome as $N$ switches, each on or off.
Each switch adds a random score that depends on itself and on $K$ other switches it interacts with.
When switches do not interact, you can improve each one alone and reach the best setting.
When every switch interacts with all others, changing one switch reshuffles everything, and the landscape has many local peaks where climbing gets stuck.
