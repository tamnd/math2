---
tag: VWBYEZAKEV
kind: definition
name: Min-entropy
msc: [94A17, 94A60]
defines: G47K6AJT8N
uses: [0X2J0VY6DN, 0D6J4B671D, AQHZ1HXXYB, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Min-entropy
---

## Definition

Let $X$ be a [[discrete random variable|0X2J0VY6DN]] with values in a countable set $\mathcal{X}$ and [[probability mass function|0D6J4B671D]] $p$.
The *min-entropy* of $X$ is
$$H_\infty(X) = -\log \max_{x \in \mathcal{X}} p(x).$$

## Remarks

The maximum exists, because the values $p(x)$ sum to $1$, so only finitely many of them exceed any given positive number.
So $H_\infty(X) \in [0, \infty)$, with $H_\infty(X) = 0$ exactly when some value has probability $1$.
For $X$ with finitely many values it is the limit of the [[Rényi entropy|AQHZ1HXXYB]] $H_\alpha(X)$ as $\alpha \to \infty$.
One has $H_\infty(X) \le H_2(X) \le 2 H_\infty(X)$ and $H_\infty(X) \le H(X)$, where $H$ is the [[Shannon entropy|Y86E072V0V]].

Example: for $p = (\frac12, \frac14, \frac14)$, $H_\infty(X) = -\log_2 \frac12 = 1$ bit, while $H(X) = 1.5$ bits.

Non-example: a random variable with a density on $\R$ has no largest point mass, so this definition does not apply to it.

In cryptography, a source is called a $k$-source when $H_\infty(X) \ge k$ in bits, that is, when $p(x) \le 2^{-k}$ for every $x$.

## Explanations

### L1 human

Min-entropy is minus the logarithm of the probability of the most likely value.
