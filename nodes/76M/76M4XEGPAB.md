---
tag: 76M4XEGPAB
kind: definition
name: Tychonoff space
msc: [54D15]
defines: C5N2J2K6Z3
uses: [0CQHFPGJ45, 0NW6CH38YR, 0ZCK8DQYN1, 0X3WGX95FE, 03HMJASQBQ, 0NSR9V8TED, 01EY3VR7ZD]
sources:
  - url: https://en.wikipedia.org/wiki/Tychonoff_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
$X$ is *completely regular* when the following holds.
For every [[closed set|0ZCK8DQYN1]] $F \subseteq X$ and every point $x \in X \setminus F$, there is a [[continuous function|0X3WGX95FE]] $f \colon X \to [0, 1]$ with $f(x) = 0$ and $f(y) = 1$ for all $y \in F$.
$X$ is a *Tychonoff space* when it is completely regular and [[T1|0NW6CH38YR]].

## Remarks

In the definition, $T_1$ can be replaced by $T_0$, because a completely regular $T_0$ space is $T_1$.
A Tychonoff space is [[regular|03HMJASQBQ]] and Hausdorff: the sets $f^{-1}([0, 1/2))$ and $f^{-1}((1/2, 1])$ separate $x$ from $F$.
A space is Tychonoff if and only if it is homeomorphic to a subspace of a product $[0, 1]^I$.
By [[Urysohn's lemma|01EY3VR7ZD]], every [[normal|0NSR9V8TED]] $T_1$ space is Tychonoff.

Example: every metric space $(X, d)$ is Tychonoff.
For $x \notin F$ with $F$ closed, $d(x, F) > 0$, and $f(y) = \min\bigl(1, d(y, x) / d(x, F)\bigr)$ is continuous, equal to $0$ at $x$ and to $1$ on $F$.

Non-example: an infinite set $X$ with the [[cofinite topology|0B906ZBTMZ]] is $T_1$ but not completely regular.
Each continuous $f \colon X \to \R$ is constant: two distinct values would have disjoint open preimages, but two nonempty open sets of $X$ always meet.
So no $f$ separates a point $x$ from the closed set $\set{y}$ with $y \ne x$.

Notation: $T_{3\frac12}$.
