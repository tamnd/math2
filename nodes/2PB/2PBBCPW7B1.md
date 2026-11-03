---
tag: 2PBBCPW7B1
kind: definition
name: Rényi entropy
msc: [94A17]
defines: AQHZ1HXXYB
uses: [0X2J0VY6DN, 0D6J4B671D, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy
---

## Definition

Let $X$ be a [[discrete random variable|0X2J0VY6DN]] with values in a finite set $\mathcal{X}$ and [[probability mass function|0D6J4B671D]] $p$.
Let $\alpha \ge 0$ with $\alpha \ne 1$.
The *Rényi entropy of order $\alpha$* of $X$ is
$$H_\alpha(X) = \frac{1}{1 - \alpha} \log \sum_{x \in \mathcal{X} \,:\, p(x) > 0} p(x)^\alpha.$$

## Remarks

For $\alpha = 0$ the sum counts the points of positive mass, so $H_0(X) = \log \abs{\set{x : p(x) > 0}}$, the Hartley entropy.
As $\alpha \to 1$, $H_\alpha(X)$ tends to the [[Shannon entropy|Y86E072V0V]] $H(X)$, and one sets $H_1(X) = H(X)$.
For $\alpha = 2$ one gets the collision entropy $H_2(X) = -\log \sum_x p(x)^2$, where $\sum_x p(x)^2$ is the probability that two independent copies of $X$ agree.
As $\alpha \to \infty$, $H_\alpha(X)$ tends to the min-entropy $-\log \max_x p(x)$.
The map $\alpha \mapsto H_\alpha(X)$ is non-increasing, and it is constant exactly when $X$ is uniform on its support.

Example: for $p = (\frac12, \frac14, \frac14)$ in base $2$, $H_0 = \log_2 3 \approx 1.585$, $H_1 = 1.5$, $H_2 = -\log_2 (\frac14 + \frac1{16} + \frac1{16}) = \log_2 \frac83 \approx 1.415$, and $H_\infty = 1$.

Non-example: the formula at $\alpha = 1$ itself is $\frac{1}{0} \log 1$, which has no value; the order $1$ is defined only as a limit.

For a countably infinite $\mathcal{X}$ the same formula is used, but the sum may diverge for $\alpha < 1$.

## Explanations

### L1 human

The Rényi entropy of order $\alpha$ is a logarithm of the $\alpha$-th power sum of the probabilities, scaled so that the uniform law on $n$ points always gets $\log n$.
