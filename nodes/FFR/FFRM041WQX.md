---
tag: FFRM041WQX
kind: definition
name: Hausdorff content
msc: [28A78]
defines: VDTEARFVMB
uses: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_dimension
    locator: Hausdorff content
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]], and let $s > 0$.
For $U \subseteq X$, let $\operatorname{diam} U = \sup \set{d(x, y) : x, y \in U}$, with $\operatorname{diam} \emptyset = 0$.
The *$s$-dimensional Hausdorff content* of a set $E \subseteq X$ is
$$\mathcal{H}^s_\infty(E) = \inf \set{\sum_{i=1}^{\infty} (\operatorname{diam} U_i)^s : E \subseteq \bigcup_{i=1}^{\infty} U_i}.$$
The infimum is over all countable covers $(U_i)$ of $E$ by subsets of $X$.

## Remarks

The map $\mathcal{H}^s_\infty$ is an [[outer measure|BJ314H17HC]] on $X$.
It has the same null sets as the [[Hausdorff measure|Q1TGZK8RN6]] $\mathcal{H}^s$, so $\dim_H E = \inf \set{s > 0 : \mathcal{H}^s_\infty(E) = 0}$, with the convention $\inf \emptyset = \infty$.
Example: in $\R$, $\mathcal{H}^{1}_\infty([0,1]) = 1$.
The cover by $[0,1]$ itself gives at most $1$, and any countable cover has total diameter at least the Lebesgue measure $1$.
Non-example of additivity: in $\R$ with $s = 1/2$, each of $[0,1]$ and $[1,2]$ has content $1$.
Indeed, a cover that uses a set of diameter at least $1$ has total at least $1$.
In a cover with all diameters below $1$, one has $(\operatorname{diam} U_i)^{1/2} \ge \operatorname{diam} U_i$, and the diameters add up to at least $1$.
But the single set $[0,2]$ covers their union, so the union has content at most $\sqrt 2 < 2$.
