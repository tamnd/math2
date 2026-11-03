---
tag: PZZA8SEXYC
kind: concept
name: Bond percolation
msc: [82B43, 60K35]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_theory
---

## Summary

Bond percolation is the random subgraph of a [[graph|00C0BR7D7H]] obtained by keeping each edge independently with probability $p$ and deleting it otherwise.
The kept edges are called open, and the [[connected components|0JG9W3KA6B]] of the open subgraph are the open clusters.
It is the basic model of [[percolation theory|BH7YPXCYDK]], and its main question is whether an infinite open cluster exists.
On many infinite graphs the answer changes at a [[percolation threshold|MP8VSZK19A]], which makes bond percolation a simple model of a phase transition.
See the [[definition|YF01ZBHZEB]].

## Explanations

### L1 human

Think of a grid of pipes in which each pipe is blocked or open at random, independently of the others.
Each pipe is open with the same probability $p$.
Water poured in at one point flows through the open pipes and wets a region, the open cluster of that point.
For a path $a - b - c$ with two pipes, water goes from $a$ to $c$ only when both pipes are open, which has probability $p^2$.
On the infinite square grid, the cluster of a point is infinite with positive probability exactly when $p > 1/2$, by [[Kesten's theorem|B8Y0ZRQP17]].
