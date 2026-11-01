---
tag: 34SN01NWPS
kind: definition
name: Moore space
msc: ["54E30"]
defines: 68MA0RM5P6
uses: [0CQHFPGJ45, 049PXYHW1T, 03HMJASQBQ, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Moore_space_(topology)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
For a family $\mathcal{G}$ of subsets of $X$ and a point $x \in X$, the *star* of $x$ in $\mathcal{G}$ is $\operatorname{st}(x, \mathcal{G}) = \bigcup \set{G \in \mathcal{G} : x \in G}$.
A *development* of $X$ is a sequence $\mathcal{G}_1, \mathcal{G}_2, \dots$ of [[open covers|049PXYHW1T]] of $X$ with the following property.
For every $x \in X$ and every open set $U$ with $x \in U$, there is $n$ with $\operatorname{st}(x, \mathcal{G}_n) \subseteq U$.
The space $X$ is *developable* if it has a development.
A *Moore space* is a developable space that is [[regular|03HMJASQBQ]] and [[Hausdorff|0S1FJ8VEX9]].

## Remarks

Every metric space $(X, d)$ is a Moore space.
Let $\mathcal{G}_n$ be the cover by all open balls of radius $1/n$.
Every ball of $\mathcal{G}_n$ that contains $x$ lies in the ball $B(x, 2/n)$, so $\operatorname{st}(x, \mathcal{G}_n) \subseteq B(x, 2/n)$, and this lies in $U$ for $n$ large.
A set $X$ with two points and the indiscrete topology is developable, with $\mathcal{G}_n = \set{X}$ for all $n$, because $X$ is the only open set containing a point.
It is not a Moore space, because it is not Hausdorff.
Some authors do not include regularity or the Hausdorff condition in the definition, so the word should be checked in each text.

## Explanations

### L1 human

A development is a sequence of open covers that get finer and finer around every point, like the covers by balls of radius $1/n$ in a metric space.
A Moore space is a well separated space with such a sequence.
