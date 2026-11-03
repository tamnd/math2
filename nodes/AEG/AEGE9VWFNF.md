---
tag: AEGE9VWFNF
kind: definition
name: Prospect theory
msc: [91B06, 91B16]
defines: AYBBDD0BYY
uses: [8C2N37XPJ8, 0A7KV2WB7A, 07Q7CNM5WF, 0GCM7B6PBK]
sources:
  - url: https://en.wikipedia.org/wiki/Prospect_theory
---

## Definition

A prospect is a list $(x_1, p_1; \dots; x_n, p_n)$ of outcomes $x_i \in \R$ with probabilities $p_i \ge 0$ such that $p_1 + \cdots + p_n = 1$.
The outcomes are gains ($x_i > 0$) or losses ($x_i < 0$) relative to a reference point.
A *prospect theory* evaluation is given by two functions.

1. A strictly increasing value function $v \colon \R \to \R$ with $v(0) = 0$. It is [[concave|0GCM7B6PBK]] on $[0, \infty)$ and [[convex|07Q7CNM5WF]] on $(-\infty, 0]$. It is steeper for losses than for gains: $v(-x) < -v(x)$ for $x > 0$.
2. A probability weighting function $\pi \colon [0, 1] \to [0, 1]$ that is [[increasing|0A7KV2WB7A]], with $\pi(0) = 0$ and $\pi(1) = 1$.

The value of the prospect is
$$V = \sum_{i=1}^{n} \pi(p_i)\, v(x_i).$$
The prospect with the larger value $V$ is chosen.

## Remarks

A standard parametric choice is $v(x) = x^{0.88}$ for $x \ge 0$ and $v(x) = -2.25\,(-x)^{0.88}$ for $x < 0$, the estimates of Tversky and Kahneman from 1992.
With $\pi(p) = p$, the coin flip $(100, 1/2; -100, 1/2)$ gets $V = \tfrac12 (100^{0.88} - 2.25 \cdot 100^{0.88}) < 0$, so it is refused, as loss aversion predicts.
A value function with $v(-x) = -v(x)$ for all $x$, such as $v(x) = x$, is not steeper for losses, so it fails clause 1.
If $\pi(p) = p$ and $v$ is concave everywhere, the formula is an expected utility of the change in wealth.
The formula above is the 1979 form for prospects that mix gains and losses.
For prospects with only gains or only losses, Kahneman and Tversky first set aside the sure part of the outcome.
Cumulative prospect theory, of 1992, applies the weights to cumulative probabilities of ranked outcomes, which keeps the choices consistent with first-order stochastic dominance.
