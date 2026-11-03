---
tag: SDQDMXED93
kind: definition
name: Conditional entropy
msc: [94A17]
defines: F3ZNDD6GG7
uses: [0X2J0VY6DN, 0DR81R1F2B, 0ZN9EZTEM6, Y86E072V0V, DZWEWHZ20N]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_entropy
---

## Definition

Let $X$ and $Y$ be [[discrete random variables|0X2J0VY6DN]] on a common probability space, with values in countable sets $\mathcal{X}$ and $\mathcal{Y}$.
Let $p(x, y) = P(X = x, Y = y)$ be their [[joint mass function|0DR81R1F2B]] and $p(x) = P(X = x)$.
For $p(x) > 0$, let $p(y \mid x) = p(x, y) / p(x)$ be the [[conditional distribution|0ZN9EZTEM6]] of $Y$ given $X = x$.
The *conditional entropy* of $Y$ given $X$ is
$$H(Y \mid X) = -\sum_{x, y \,:\, p(x, y) > 0} p(x, y) \log p(y \mid x) \in [0, \infty].$$

## Remarks

Grouping the terms by $x$ gives $H(Y \mid X) = \sum_{x : p(x) > 0} p(x) \, H(Y \mid X = x)$, where $H(Y \mid X = x)$ is the [[Shannon entropy|Y86E072V0V]] of the law $p(\cdot \mid x)$.
If $H(X) < \infty$, the chain rule $H(X, Y) = H(X) + H(Y \mid X)$ holds, where $H(X, Y)$ is the [[joint entropy|DZWEWHZ20N]].

Example: let $X$ be a fair bit, and let $Y = X$ with probability $\frac34$ and $Y = 1 - X$ with probability $\frac14$, independently of $X$.
Then for each $x$ the law of $Y$ given $X = x$ has masses $\frac34, \frac14$, so $H(Y \mid X) = H_b(\frac14) \approx 0.811$ bits.

Non-example: $H(Y \mid X)$ is not the entropy of a conditional law given one fixed value $x$; the quantity $H(Y \mid X = x)$ can be larger than $H(Y)$, while the average $H(Y \mid X)$ never is.

One has $0 \le H(Y \mid X) \le H(Y)$, with $H(Y \mid X) = 0$ exactly when $Y = f(X)$ almost surely for some function $f$, and, when $H(Y) < \infty$, $H(Y \mid X) = H(Y)$ exactly when $X$ and $Y$ are independent.

## Explanations

### L1 human

Conditional entropy is the entropy of $Y$ that is left after $X$ is revealed, averaged over the values of $X$.
