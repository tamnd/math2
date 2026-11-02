---
tag: JKQP7AFZ0E
kind: definition
name: Separable Banach space
msc: [46B99, 54D65]
defines: AH45GS6RCR
uses: [06GZ956657, 0Z2P41SVDP, 0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_space
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$.
The space $X$ is *separable* if it is [[separable|0Z2P41SVDP]] as a metric space.
That is, there is a countable subset $D \subseteq X$ that is [[dense|0BSJSX7ME2]] in $X$.

## Remarks

Equivalently, there is a countable set $S \subseteq X$ whose linear span is dense in $X$.
Indeed, finite combinations of elements of $S$ with rational (or Gaussian rational) coefficients then form a countable dense set.
Example: $\ell^1$ is separable.
The finitely supported sequences with rational entries form a countable set $D$.
For $x \in \ell^1$ and $\varepsilon > 0$, choose $N$ with $\sum_{n > N} \abs{x_n} < \varepsilon/2$.
Then choose rational $q_n$ with $\sum_{n \le N} \abs{x_n - q_n} < \varepsilon/2$.
Then $(q_1, \ldots, q_N, 0, \ldots) \in D$ is within $\varepsilon$ of $x$.
Non-example: $\ell^\infty$ is not separable.
For each subset $A$ of $\N$ its indicator sequence $\mathbf{1}_A$ lies in $\ell^\infty$, and $\norm{\mathbf{1}_A - \mathbf{1}_B}_\infty = 1$ for $A \ne B$.
The open balls of radius $1/2$ around these uncountably many points are disjoint, so no countable set meets them all.
If the dual $X^*$ is separable, then $X$ is separable; the converse fails, as $X = \ell^1$ with $X^* = \ell^\infty$ shows.
