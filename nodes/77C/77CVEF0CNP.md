---
tag: 77CVEF0CNP
kind: definition
name: Point process
msc: [60G55, 60G57, 60D05]
defines: DNDKBVHS3H
uses: [0NFPJVJJHX, 0PNRKMRC55, 0MTNR28K60]
sources:
  - url: https://en.wikipedia.org/wiki/Point_process
---

## Definition

Let $E$ be a complete separable metric space with its Borel $\sigma$-algebra $\mathcal{B}(E)$.
A measure $\mu$ on $\mathcal{B}(E)$ is a *locally finite counting measure* if $\mu(B) \in \set{0, 1, 2, \ldots}$ for every bounded Borel set $B$.
Let $\mathcal{N}$ be the set of these measures, with the smallest $\sigma$-algebra that makes each map $\mu \mapsto \mu(B)$ measurable.
A *point process* on $E$ is a measurable map $N$ from a [[probability space|0NFPJVJJHX]] $(\Omega, \mathcal{F}, P)$ to $\mathcal{N}$.

## Remarks

So each $N(B)$, the number of points in $B$, is a [[random variable|0PNRKMRC55]].
The point process is *simple* if $N(\set{x}) \le 1$ for all $x \in E$, almost surely.
Its intensity measure is $\Lambda(B) = \mathbb{E}[N(B)]$.
Example: if $U_1, \ldots, U_n$ are random points of $[0, 1]$, then $N = \sum_{i=1}^n \delta_{U_i}$ is a point process; $N(B) = \#\set{i : U_i \in B}$ is a random variable with values in $\set{0, \ldots, n}$.
Non-example: $\sum_{k \ge 1} \delta_{1/k}$ is not a locally finite counting measure on $\R$, since it gives infinite mass to the bounded set $[0, 1]$.
The [[Poisson point process|0MTNR28K60]] with intensity $\Lambda$ is the point process with $N(B)$ Poisson of mean $\Lambda(B)$ and independent counts on disjoint sets.
