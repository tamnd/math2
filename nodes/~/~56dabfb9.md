---
tag: ~56dabfb9
kind: definition
name: Compact set
aliases: [compact-subset]
msc: [54D30]
defines: ~4b593eaa
uses: [~68153d33, ~74712f5b]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Compactness of subsets
---

## Definition

Let $X$ be a [[topological space|~77bfcc55]] and let $K \subseteq X$.
The set $K$ is compact when $K$, with the [[subspace topology|~74712f5b]], is a [[compact space|~68153d33]].

## Remarks

By [[compactness via open covers|~6bb86ae8]], $K$ is compact exactly when each [[cover|~a2a4fe18]] of $K$ by open sets of $X$ has a finite subcover.
Each finite subset of $X$ is compact. The empty set is compact.
In $\mathbb{R}$, the interval $[0, 1]$ is compact, but $(0, 1)$ and $[0, \infty)$ are not. The [[Heine–Borel theorem|~207cb5fd]] describes the compact subsets of $\mathbb{R}^n$.

## Explanations

### L1 human

A compact set behaves in many ways like a finite set.
For example, a continuous real function on a compact set is bounded and attains its maximum, as a function on a finite set does.
