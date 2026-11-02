---
tag: QB6EZ3HP73
kind: definition
name: Simple function
msc: [28A20]
defines: 7WMBX7M4P6
uses: [YYNCJSR0PJ, N4KDT83V3S, 0RCQZ36MME]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_function
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]].
A *simple function* on $X$ is a [[measurable function|YYNCJSR0PJ]] $s \colon X \to \R$ whose image $s(X)$ is a finite set.

## Remarks

Equivalently, $s = \sum_{k=1}^{n} a_k \mathbf{1}_{A_k}$ for some $n \ge 0$, real numbers $a_k$ and sets $A_k \in \Sigma$, where $\mathbf{1}_{A_k}$ is the [[indicator function|0RCQZ36MME]] of $A_k$.
The sets $A_k$ can be chosen pairwise disjoint, with distinct values $a_k$.
For a measure $\mu$ and $a_k \ge 0$, the integral is $\int s \, d\mu = \sum_k a_k \mu(A_k)$, with $0 \cdot \infty = 0$.
Example: on $\R$ with the Borel sets, $s = 3 \cdot \mathbf{1}_{[0, 1]} - \mathbf{1}_{\Q}$ is simple; its values are $-1$, $0$, $2$ and $3$.
Non-example: $x \mapsto x$ on $[0, 1]$ is measurable but has infinitely many values.
Every measurable $f \colon X \to [0, \infty]$ is the pointwise limit of a non-decreasing sequence of nonnegative simple functions.
Some authors drop the measurability condition, or allow complex values.
