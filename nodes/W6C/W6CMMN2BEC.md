---
tag: W6CMMN2BEC
kind: definition
name: Shannon entropy
msc: [94A17, 60A10]
defines: Y86E072V0V
uses: [0X2J0VY6DN, 0D6J4B671D, 04DXAFN2ES, FS87BNZS9X, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_(information_theory)
---

## Definition

Let $X$ be a [[discrete random variable|0X2J0VY6DN]] with values in a countable set $\mathcal{X}$ and [[probability mass function|0D6J4B671D]] $p(x) = P(X = x)$.
Let $b > 1$ be a real number, the base of the logarithm.
The *Shannon entropy* of $X$ in base $b$ is
$$H_b(X) = -\sum_{x \in \mathcal{X}} p(x) \log_b p(x) \in [0, \infty],$$
with the convention $0 \log_b 0 = 0$.

## Remarks

Each term $-p(x) \log_b p(x)$ is non-negative, so the sum is well defined, possibly $+\infty$ when $\mathcal{X}$ is infinite.
It is the [[expected value|0WQNRCNY3M]] $H_b(X) = E[I(X)]$ of the [[information content|FS87BNZS9X]] $I(x) = -\log_b p(x)$.
The entropy depends only on the law of $X$, so one also writes $H(p)$ or $H(p_1, \dots, p_n)$.
Base $2$ gives the unit bit, base $e$ the unit nat; one has $H_b(X) = H_e(X) / \ln b$ with the [[natural logarithm|04DXAFN2ES]] $\ln$.

Example: if $X$ takes the values $u, v, w$ with probabilities $\frac12, \frac14, \frac14$, then $H_2(X) = \frac12 \cdot 1 + \frac14 \cdot 2 + \frac14 \cdot 2 = \frac32$ bits.

Non-example: a continuous random variable with density $f$ is not discrete, so this formula gives it no Shannon entropy.
The analogue $-\int f \log f$ is the [[differential entropy|B4PNYNYVKK]], which can be negative.

If $\mathcal{X}$ has $n$ elements, then $0 \le H_b(X) \le \log_b n$, with $H_b(X) = 0$ exactly when $X$ is almost surely constant and $H_b(X) = \log_b n$ exactly when $X$ is uniform.
The [[characterization of Shannon entropy|3TERJ5C8QK]] shows that the formula is forced by a few natural axioms.

## Explanations

### L1 human

Write down how surprising each outcome is, $-\log p(x)$, and take the average over the outcomes.
Rare outcomes are very surprising but happen rarely; the entropy balances the two.
