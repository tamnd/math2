---
tag: ~dfeacff3
kind: definition
name: Closed set
msc: [54A05]
defines: ~7275853d
uses: [~77bfcc55, ~159c5927, 0B1FSS1VZW]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_set
    locator: Definition
---

## Definition

Let $X$ be a [[topological space|~77bfcc55]].
A subset $F$ of $X$ is closed in $X$ when its [[complement|0B1FSS1VZW]] $X \setminus F$ is [[open|~159c5927]] in $X$.

## Remarks

The sets $\emptyset$ and $X$ are both open and closed.
A set can be neither open nor closed: $[0, 1)$ in $\mathbb{R}$ is an example.
In a metric space, $F$ is closed if and only if it [[contains the limits of its convergent sequences|~26824759]].

## Explanations

### L1 human

Closed is not the opposite of open. A closed set is a set whose outside is open.
The interval $[0, 1]$ is closed in $\mathbb{R}$, because its outside $(-\infty, 0) \cup (1, \infty)$ is open.
