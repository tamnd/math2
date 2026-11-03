---
tag: NVWZK33A7T
kind: definition
name: Følner sequence
msc: ["43A07", "20F65"]
defines: 6WZR80CPBD
uses: [G5S1M9, 0ME21QN125]
sources:
  - url: https://en.wikipedia.org/wiki/Følner_sequence
---

## Definition

Let $G$ be a countable [[group|G5S1M9]].
For $g \in G$ and $F \subseteq G$, let $gF = \set{gx : x \in F}$, and let $\triangle$ denote the [[symmetric difference|0ME21QN125]].
A *(left) Følner sequence* in $G$ is a sequence $(F_n)_{n \ge 1}$ of finite nonempty subsets of $G$ such that
$$\lim_{n \to \infty} \frac{\abs{gF_n \triangle F_n}}{\abs{F_n}} = 0 \quad \text{for every } g \in G.$$

## Remarks

Example: in $G = \Z$, take $F_n = \set{0, 1, \ldots, n-1}$.
For $k \in \Z$ and $n \ge \abs{k}$, the sets $k + F_n$ and $F_n$ differ in exactly $2\abs{k}$ points.
So the ratio is $2\abs{k}/n$, which tends to $0$, and $(F_n)$ is a Følner sequence.
In the same way the cubes $\set{0, \ldots, n-1}^d$ form a Følner sequence in $\Z^d$.

Non-example: in $G = \Z$, the singletons $F_n = \set{n}$ do not form a Følner sequence.
For $g = 1$, the sets $1 + F_n = \set{n+1}$ and $F_n$ are disjoint, so the ratio is $2$ for every $n$.

A countable group has a Følner sequence if and only if it satisfies the [[Følner condition|82R5XGCART]].
For a [[locally compact group|AHV05ZBCYW]] $G$ with left [[Haar measure|VY0HXD3GC4]] $m$, one uses compact sets $F_n$ with $m(F_n) > 0$.
The condition is then $m(gF_n \triangle F_n)/m(F_n) \to 0$ for every $g \in G$.
Often the convergence is asked to be uniform for $g$ in compact sets.
