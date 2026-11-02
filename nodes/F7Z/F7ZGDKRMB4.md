---
tag: F7ZGDKRMB4
kind: definition
name: Epsilon-net of a set system
msc: [52C45, 68U05, 05D05]
defines: V2SBN1FNQV
uses: [0C21Q694AG]
sources:
  - url: https://en.wikipedia.org/wiki/Ε-net_(computational_geometry)
---

## Definition

Let $X$ be a finite nonempty set, let $\mathcal{R}$ be a [[family of subsets|0C21Q694AG]] of $X$, called ranges, and let $0 < \varepsilon \le 1$.
A set $N \subseteq X$ is an *$\varepsilon$-net* of $(X, \mathcal{R})$ if every range $R \in \mathcal{R}$ with $\abs{R} \ge \varepsilon \abs{X}$ satisfies $R \cap N \ne \emptyset$.

## Remarks

Example: let $X = \set{1, 2, \dots, 100}$, let $\mathcal{R}$ be the sets of the form $\set{a, a+1, \dots, b}$, and let $\varepsilon = 1/10$.
The set $N = \set{10, 20, \dots, 100}$ is an $\varepsilon$-net.
Indeed, a range with at least $10$ elements consists of at least $10$ consecutive integers, so it contains a multiple of $10$.

Non-example: for the same $X$ and $\mathcal{R}$, the set $N' = \set{20, 40, \dots, 100}$ is not a $1/10$-net.
The range $\set{1, \dots, 19}$ has $19 \ge 10$ elements but misses $N'$.

The same notion is used for a probability measure $\mu$ on a set $X$: then $N$ is an $\varepsilon$-net if it meets every range $R$ with $\mu(R) \ge \varepsilon$.
The case above is $\mu$ equal to the uniform measure on a finite $X$.
