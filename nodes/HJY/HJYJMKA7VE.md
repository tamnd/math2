---
tag: HJYJMKA7VE
kind: definition
name: Cauchy filter
msc: ["54E15", 54A20]
defines: WZC4J62B1G
uses: [A54T86KS63, FVFFKNKEDF, 15PF73BKY6]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_space
---

## Definition

Let $(X, \mathcal{U})$ be a [[uniform space|A54T86KS63]] and let $\mathcal{F}$ be a [[filter|15PF73BKY6]] on $X$.
The filter $\mathcal{F}$ is a *Cauchy filter* if for every [[entourage|FVFFKNKEDF]] $U \in \mathcal{U}$ there is a set $A \in \mathcal{F}$ with $A \times A \subseteq U$.
The uniform space is *complete* if every Cauchy filter on $X$ converges to a point of $X$.

## Remarks

The neighbourhood filter $\mathcal{N}_x$ of a point $x$ is a Cauchy filter.
Given an entourage $U$, choose a symmetric entourage $V$ with $V \circ V \subseteq U$ and let $A = V[x]$, a member of $\mathcal{N}_x$.
For $y, z \in A$ one has $(y, x) \in V$ and $(x, z) \in V$, so $(y, z) \in V \circ V \subseteq U$.
On $\R$ with its usual uniformity, the filter of sets that contain some interval $[n, \infty)$ is not a Cauchy filter.
For $U = \set{(x, y) : \abs{x - y} < 1}$, every member contains two points at distance $1$, so no member $A$ has $A \times A \subseteq U$.
In a metric space, a sequence is a [[Cauchy sequence|0PWX18FM4G]] if and only if the filter of its tails is a Cauchy filter.
Every convergent filter is a Cauchy filter.

## Explanations

### L1 human

A Cauchy filter is a filter with members as small as one likes, in the sense of the uniform structure.
It is the right replacement for Cauchy sequences in spaces where sequences are not enough.
