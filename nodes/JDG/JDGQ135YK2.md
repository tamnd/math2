---
tag: JDGQ135YK2
kind: statement
role: theorem
name: Carathéodory's criterion
msc: [28A12]
uses: [BJ314H17HC, WD1AJ2X325, 0XPR1E85W0, 02BH3MCBQB]
about: [BJ314H17HC]
sources:
  - url: https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_criterion
same_as:
  wikidata: Q5037750
  wikipedia: Carathéodory's criterion
---

## Statement

Let $n \ge 1$ and let $\lambda^*$ be Lebesgue [[outer measure|BJ314H17HC]] on [[Euclidean space|0XPR1E85W0]] $\R^n$.
That is, $\lambda^*(A)$ is the infimum of $\sum_k \operatorname{vol}(R_k)$ over all countable covers of $A$ by open boxes $R_k$.
Call $E \subseteq \R^n$ Lebesgue measurable if for every $\varepsilon > 0$ there is an [[open set|02BH3MCBQB]] $U \supseteq E$ with $\lambda^*(U \setminus E) < \varepsilon$.
Then $E$ is Lebesgue measurable if and only if
$$\lambda^*(A) = \lambda^*(A \cap E) + \lambda^*(A \setminus E) \quad \text{for every } A \subseteq \R^n.$$

## Remarks

The inequality $\le$ always holds by subadditivity, so only $\ge$ has content, and only for $A$ with $\lambda^*(A) < \infty$.
If $E$ is Lebesgue measurable, approximate $E$ from outside by an open set, and use that open sets split every $A$ additively.
Conversely, apply the splitting identity to bounded parts of $E$ and to open covers chosen close to $\lambda^*$.
For example, a closed box $E$ splits every $A$ additively, in line with its being measurable.
The criterion is useful because the splitting condition makes sense for any outer measure $\mu^*$ on any set $X$.
For any outer measure, the sets $E$ with $\mu^*(A) = \mu^*(A \cap E) + \mu^*(A \setminus E)$ for all $A \subseteq X$ form a $\sigma$-algebra, and $\mu^*$ restricted to it is a complete measure.

## Explanations

### L1 human

A set is well behaved for length, area or volume exactly when it cuts every other set cleanly.
Cutting cleanly means the outer measure of any set $A$ is the sum of the outer measures of the part of $A$ inside $E$ and the part outside $E$.
This test needs no topology, so it can be used in any setting where an outer measure is available.

### L2 human

In a measure theory course this splitting condition is often taken as the definition of a measurable set.
With it, Carathéodory's construction turns an outer measure into a complete measure; this gives Lebesgue measure, Lebesgue–Stieltjes measures and Hausdorff measures.
The same construction is the heart of the proof of the [[Carathéodory extension theorem|Q8EXG7EKYW]].
The theorem above shows that for $\R^n$ this abstract notion agrees with the geometric one of approximation by open sets.
