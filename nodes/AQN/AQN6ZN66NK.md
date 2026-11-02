---
tag: AQN6ZN66NK
kind: definition
name: Pi-system
msc: [28A05, 60A10]
defines: 4W9NM803BB
uses: [0SJ3RX9TXA, 0HBRW4E6G1, 04WSW8T3SY]
sources:
  - url: https://en.wikipedia.org/wiki/Pi-system
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]].
A *π-system* on $X$ is a nonempty family $\mathcal{P}$ of subsets of $X$ such that $A \cap B \in \mathcal{P}$ for all $A, B \in \mathcal{P}$, where $A \cap B$ is the [[intersection|0HBRW4E6G1]].

## Remarks

The family $\set{(-\infty, a] : a \in \R}$ is a π-system on $\R$, since $(-\infty, a] \cap (-\infty, b] = (-\infty, \min(a, b)]$.
The family $\set{[0, 1], [1, 2]}$ is not a π-system, since $[0, 1] \cap [1, 2] = \set{1}$ is not in it.
Every [[σ-algebra|04WSW8T3SY]] is a π-system.
By induction, a π-system is closed under all finite intersections.
The name is also written $\pi$-system.
