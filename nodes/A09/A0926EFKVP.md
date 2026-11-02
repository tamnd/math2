---
tag: A0926EFKVP
kind: definition
name: Hausdorff measure
msc: [28A78, 28A80]
defines: Q1TGZK8RN6
uses: [0VKD1TP7F3, 0KW3PN547K, 0QF1MZ9FRG, BJ314H17HC, 3T6WG315GC, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_measure
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]], and let $\operatorname{diam} U$ be the [[diameter|0KW3PN547K]] of a set $U \subseteq X$.
Let $s \ge 0$, with the convention $(\operatorname{diam} U)^0 = 1$ for every $U$.
For $A \subseteq X$ and $\delta > 0$, let
$$\mathcal{H}^s_\delta(A) = \inf \set{ \sum_{i=1}^\infty (\operatorname{diam} U_i)^s : A \subseteq \bigcup_{i=1}^\infty U_i, \ \operatorname{diam} U_i \le \delta },$$
where the [[infimum|0QF1MZ9FRG]] runs over all countable covers of $A$ by sets $U_i \subseteq X$ of diameter at most $\delta$.
The *$s$-dimensional Hausdorff measure* of $A$ is
$$\mathcal{H}^s(A) = \lim_{\delta \to 0} \mathcal{H}^s_\delta(A) = \sup_{\delta > 0} \mathcal{H}^s_\delta(A).$$

## Remarks

The limit exists in $[0, \infty]$ because $\mathcal{H}^s_\delta(A)$ grows as $\delta$ decreases.
The map $\mathcal{H}^s$ is a [[metric outer measure|3T6WG315GC]], so all Borel sets are measurable and its restriction to them is a measure.
Some authors multiply by a constant so that $\mathcal{H}^n$ equals [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$; without it, $\mathcal{H}^n$ is a constant multiple of Lebesgue measure.

Example: $\mathcal{H}^0$ is counting measure.
On $\R$, $\mathcal{H}^1$ is Lebesgue measure: covers by intervals realize the infimum, and the length of an interval is its diameter.

Non-example: the quantity without the limit $\delta \to 0$, the Hausdorff content $\mathcal{H}^s_\infty$ with no bound on diameters, is not a measure on Borel sets.
In $\R^2$ with $s = 1$, the segments $A = [0, 1] \times \set{0}$ and $B = [0, 1] \times \set{1}$ each have content $1$.
But $A \cup B$ lies in the unit square, of diameter $\sqrt 2$, so its content is at most $\sqrt 2 < 2$.

## Explanations

### L1 human

Cover the set by small pieces, add the $s$-th powers of their sizes, and take the best cover.
Letting the pieces become arbitrarily small gives the $s$-dimensional size of the set.
