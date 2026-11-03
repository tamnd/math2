---
tag: WSKT3PQ5E1
kind: definition
name: Information content
msc: [94A17]
defines: FS87BNZS9X
uses: [0X2J0VY6DN, 0D6J4B671D, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Information_content
---

## Definition

Let $X$ be a [[discrete random variable|0X2J0VY6DN]] with values in a countable set $\mathcal{X}$ and [[probability mass function|0D6J4B671D]] $p$.
Let $b > 1$ be the base of the logarithm.
For $x \in \mathcal{X}$ with $p(x) > 0$, the *information content* (or *self-information*) of the outcome $x$ is
$$I_X(x) = -\log_b p(x) = \log_b \frac{1}{p(x)}.$$

## Remarks

The value is in $[0, \infty)$, and it is $0$ exactly when $p(x) = 1$.
Base $2$ gives bits, base $e$ with the [[natural logarithm|04DXAFN2ES]] gives nats.
The composite $I_X(X)$ is a random variable, and its expected value is the [[Shannon entropy|Y86E072V0V]] of $X$.

Example: if $X$ is the result of a fair die, then $p(6) = \frac16$ and $I_X(6) = \log_2 6 \approx 2.585$ bits.

Non-example: an outcome $x$ with $p(x) = 0$ has no information content in this definition, since $\log_b 0$ is not a real number; some authors set it to $+\infty$.

If $X$ and $Y$ are independent, then $I_{(X, Y)}(x, y) = I_X(x) + I_Y(y)$, because $p_{(X,Y)}(x, y) = p_X(x) p_Y(y)$.

## Explanations

### L1 human

Information content is minus the logarithm of the probability of what happened.
