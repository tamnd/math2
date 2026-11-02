---
tag: WS62STR57F
kind: definition
name: Linear and stable summation methods
msc: [40C99, 40D05]
defines: N6Z14G81VF
uses: [X80DZEXQDQ]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $M$ be a [[summability method|X80DZEXQDQ]].
Write $M\left(\sum a_n\right)$ for the $M$-sum of an $M$-summable series $\sum_{n \ge 0} a_n$ with terms in $\mathbb{K}$.

1. $M$ is *linear* if, whenever $\sum a_n$ and $\sum b_n$ are $M$-summable and $\lambda, \mu \in \mathbb{K}$, the series $\sum (\lambda a_n + \mu b_n)$ is $M$-summable and $M\left(\sum (\lambda a_n + \mu b_n)\right) = \lambda M\left(\sum a_n\right) + \mu M\left(\sum b_n\right)$.
2. $M$ is *stable* if, for every sequence $(a_n)_{n \ge 0}$, the series $a_0 + a_1 + a_2 + \cdots$ is $M$-summable if and only if $a_1 + a_2 + \cdots$ is $M$-summable, and then $M(a_0 + a_1 + a_2 + \cdots) = a_0 + M(a_1 + a_2 + \cdots)$.

## Remarks

Example: ordinary summation of convergent series is linear and stable, by the limit rules for sums and because shifting the partial sums by $a_0$ does not affect convergence.
Cesàro summation is also linear and stable.
Non-example: zeta function regularization assigns $1 + 1 + 1 + \cdots$ the value $\zeta(0) = -\frac12$; stability would give $x = 1 + x$ for this value, so this method is not stable.
In terms of the partial sums $s_n$, linearity says that $D_M$ is a vector space and $M$ is a linear map on it.

## Explanations

### L1 human

Linear means sums and multiples are respected; stable means the first term can be split off.
