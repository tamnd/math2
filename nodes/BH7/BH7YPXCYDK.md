---
tag: BH7YPXCYDK
kind: concept
name: Percolation theory
msc: [60K35, 82B43]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_theory
same_as:
  wikidata: Q900918
  wikipedia: Percolation theory
---

## Summary

Percolation theory studies the connected clusters of a random subgraph of a large graph, where each edge or vertex is kept independently with probability $p$.
Its main question is whether an infinite cluster appears.
On many graphs there is a sharp [[percolation threshold|MP8VSZK19A]]: below it all clusters are finite, above it an infinite cluster exists.
It is a basic model of a phase transition and of flow through a porous medium.

## Explanations

### L1 human

Take a huge square grid of pipes and block each pipe at random, keeping it open with probability $p$.
Pour water at one point and ask whether it can flow arbitrarily far.
If $p$ is small, the water stays in a small region; if $p$ is close to $1$, it can reach infinity with positive probability.
The change happens suddenly at a critical value of $p$, which for this grid is $1/2$, by [[Kesten's theorem|B8Y0ZRQP17]].
