---
tag: 9GNAAHQJY6
kind: definition
name: Convergence of filters
msc: [54A20]
defines: 70M1VAPFN0
uses: [15PF73BKY6, 0CQHFPGJ45, 0ZCY0Z80B6, 0W4CN9E2W5]
sources:
  - url: https://en.wikipedia.org/wiki/Filters_in_topology
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]], let $\mathcal{F}$ be a [[filter|15PF73BKY6]] on $X$, and let $x \in X$.
Let $\mathcal{N}(x)$ be the filter of [[neighbourhoods|0ZCY0Z80B6]] of $x$.
The filter $\mathcal{F}$ *converges* to $x$, written $\mathcal{F} \to x$, if $\mathcal{N}(x) \subseteq \mathcal{F}$.
Then $x$ is a *limit* of $\mathcal{F}$.

## Remarks

For a map $f \colon S \to X$ from a set $S$ and a filter $\mathcal{G}$ on $S$, the *image filter* is $f(\mathcal{G}) = \set{B \subseteq X : f^{-1}(B) \in \mathcal{G}}$.
One says that $f(s) \to x$ along $\mathcal{G}$ if $f(\mathcal{G}) \to x$.

Example: let $(x_n)$ be a sequence in $X$, and let $\mathcal{F}$ be the family of sets $B \subseteq X$ that contain $x_n$ for all large $n$.
Then $\mathcal{F}$ is a filter, and $\mathcal{F} \to x$ if and only if the sequence [[converges|0W4CN9E2W5]] to $x$, since both mean that each neighbourhood of $x$ contains $x_n$ for all large $n$.

Example: the neighbourhood filter $\mathcal{N}(x)$ converges to $x$, and so does the principal filter $\set{B : x \in B}$.

Non-example: in $\R$, let $\mathcal{F}$ be the filter of sets that contain an interval $[n, \infty)$.
For each $x \in \R$, the neighbourhood $(x - 1, x + 1)$ contains no such interval, so $\mathcal{F}$ does not converge to $x$.

A space is [[Hausdorff|0S1FJ8VEX9]] if and only if every filter on it has at most one limit.
