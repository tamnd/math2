---
tag: VYP60TA2EC
kind: definition
name: Hausdorff dimension
msc: [28A78, 28A80]
defines: SSNFTHZ6YJ
uses: [Q1TGZK8RN6, 0VKD1TP7F3, 0QF1MZ9FRG, 0BXNDZFQME]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_dimension
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]], and for $s \ge 0$ let $\mathcal{H}^s$ be the $s$-dimensional [[Hausdorff measure|Q1TGZK8RN6]] on $X$.
The *Hausdorff dimension* of a set $A \subseteq X$ is
$$\dim_H A = \inf \set{ s \ge 0 : \mathcal{H}^s(A) = 0 },$$
with the convention $\inf \emptyset = \infty$.

## Remarks

If $\mathcal{H}^s(A) < \infty$ and $t > s$, then $\mathcal{H}^t(A) = 0$.
So $\mathcal{H}^s(A) = \infty$ for $s < \dim_H A$ and $\mathcal{H}^s(A) = 0$ for $s > \dim_H A$.
At $s = \dim_H A$ the value can be $0$, positive and finite, or $\infty$.
Equivalently, $\dim_H A = \sup \set{s \ge 0 : \mathcal{H}^s(A) = \infty}$, with $\sup \emptyset = 0$.

Example: the middle-thirds [[Cantor set|0BXNDZFQME]] $C$ has $\dim_H C = \log 2 / \log 3$.
At the $k$-th step, $C$ is covered by $2^k$ intervals of length $3^{-k}$, so $\mathcal{H}^s_{3^{-k}}(C) \le 2^k 3^{-ks}$, which equals $1$ for $s = \log 2 / \log 3$.
This gives $\dim_H C \le \log 2 / \log 3$; the matching lower bound needs a separate argument.

A dense set can have dimension $0$: $\Q$ is dense in $\R$, yet $\dim_H \Q = 0$.
Each point has $\mathcal{H}^s$ measure $0$ for $s > 0$, and $\mathcal{H}^s$ is countably subadditive.

For subsets of $\R^n$, one has $\dim_H A \le n$, and every nonempty open set has dimension $n$.

## Explanations

### L1 human

The Hausdorff dimension is the exponent $s$ at which the $s$-dimensional size of a set drops from infinite to zero.
It measures how a set fills space at small scales.
