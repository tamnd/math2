---
tag: 0K0GE6BCYW
kind: definition
name: Path-connected space
aliases: [pathwise-connected-space]
msc: [54D05]
defines: 0WB6DH499T
uses: [0CNQXVBHCX, 0SY9ECQ19Q]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Path connectedness
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]].
A path in $X$ from $x$ to $y$ is a [[continuous map|0SY9ECQ19Q]] $\gamma \colon [0, 1] \to X$ with $\gamma(0) = x$ and $\gamma(1) = y$.
The space $X$ is path-connected when $X$ is nonempty and for all $x, y \in X$ there is a path in $X$ from $x$ to $y$.
A subset of $X$ is path-connected when it is path-connected in the [[subspace topology|0D5YHQGDJY]].

## Remarks

Some authors do not require $X$ to be nonempty.
Each convex subset of $\mathbb{R}^n$ is path-connected: use the segment $\gamma(t) = (1 - t)x + ty$.
[[Path-connected spaces are connected|0ZMT1GP4KM]]. The [[topologist's sine curve|0K3T4A659R]] is connected but not path-connected.

## Explanations

### L1 human

A space is path-connected when you can walk from each point to each other point along a continuous path inside the space.
This is a concrete way to show that a space is in one piece.
