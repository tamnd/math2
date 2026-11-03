---
tag: Q0B06SRF2J
kind: definition
name: Joint entropy
msc: [94A17]
defines: DZWEWHZ20N
uses: [0X2J0VY6DN, 0DR81R1F2B, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Joint_entropy
---

## Definition

Let $X_1, \dots, X_n$ be [[discrete random variables|0X2J0VY6DN]] on a common probability space, with values in countable sets $\mathcal{X}_1, \dots, \mathcal{X}_n$.
Let $p(x_1, \dots, x_n) = P(X_1 = x_1, \dots, X_n = x_n)$ be their [[joint probability mass function|0DR81R1F2B]].
The *joint entropy* of $X_1, \dots, X_n$ is
$$H(X_1, \dots, X_n) = -\sum_{x_1 \in \mathcal{X}_1} \cdots \sum_{x_n \in \mathcal{X}_n} p(x_1, \dots, x_n) \log p(x_1, \dots, x_n) \in [0, \infty],$$
with the convention $0 \log 0 = 0$.

## Remarks

It is the [[Shannon entropy|Y86E072V0V]] of the random vector $(X_1, \dots, X_n)$, which is a discrete random variable with values in $\mathcal{X}_1 \times \cdots \times \mathcal{X}_n$.

Example: let $X$ be a fair bit and $Y = X$.
Then $p(0, 0) = p(1, 1) = \frac12$ and $p(0, 1) = p(1, 0) = 0$, so $H(X, Y) = 1$ bit, while $H(X) + H(Y) = 2$ bits.

Non-example: two random variables on different probability spaces have no joint mass function, so their joint entropy is not defined.
The joint entropy depends on the joint law, not only on the two marginal laws.

When the entropies are finite, $\max(H(X), H(Y)) \le H(X, Y) \le H(X) + H(Y)$, and the right inequality is an equality exactly when $X$ and $Y$ are independent.

## Explanations

### L1 human

Joint entropy is the entropy of several random variables viewed as one random vector.
