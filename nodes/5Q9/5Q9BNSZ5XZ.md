---
tag: 5Q9BNSZ5XZ
kind: definition
name: Epigraph
msc: [52A41, 26B25, 49J53]
defines: 8BJ5M76FSX
uses: [09CEDJYBKP, 0GSZ7B0CGR]
sources:
  - url: https://en.wikipedia.org/wiki/Epigraph_(mathematics)
---

## Definition

Let $X$ be a set and let $f \colon X \to [-\infty, +\infty]$ be a function with values in the [[extended real line|0GSZ7B0CGR]].
The *epigraph* of $f$ is the subset of the [[Cartesian product|09CEDJYBKP]] $X \times \R$ given by
$$\operatorname{epi} f = \set{(x, r) \in X \times \R : f(x) \le r}.$$

## Remarks

Only real numbers $r$ are used, so points $x$ with $f(x) = +\infty$ contribute nothing, and points with $f(x) = -\infty$ contribute the whole line $\set{x} \times \R$.
The *strict epigraph* uses $f(x) < r$ instead.
If $X$ is a real vector space, $f$ is convex if and only if $\operatorname{epi} f$ is a convex set.
If $X$ is a topological space, $f$ is lower semicontinuous if and only if $\operatorname{epi} f$ is closed in $X \times \R$.
The function is recovered as $f(x) = \inf \set{r \in \R : (x, r) \in \operatorname{epi} f}$, with $\inf \emptyset = +\infty$.

Example: for $f(x) = x^2$ on $\R$, the point $(1, 2)$ lies in $\operatorname{epi} f$, since $f(1) = 1 \le 2$.

Non-example: the point $(2, 1)$ does not lie in $\operatorname{epi} f$, since $f(2) = 4 > 1$.
