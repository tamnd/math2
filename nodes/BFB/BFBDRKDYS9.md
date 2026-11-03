---
tag: BFBDRKDYS9
kind: definition
name: Channel capacity
msc: [94A40, 94A24, 94A17]
defines: J7MZ2XQP9M
uses: [B9C5RBFATB, A83CYGDXFG, 0D6J4B671D]
sources:
  - url: https://en.wikipedia.org/wiki/Channel_capacity
---

## Definition

Let $(\mathcal{X}, W, \mathcal{Y})$ be a discrete memoryless [[channel|B9C5RBFATB]].
For a [[probability mass function|0D6J4B671D]] $p$ on $\mathcal{X}$, let $X$ have law $p$ and let $Y$ be the output, so that $\Pr(X = x, Y = y) = p(x) W(y \mid x)$.
Let $I(X; Y)$ be their [[mutual information|A83CYGDXFG]] in bits.
The *capacity* of the channel is
$$C = \max_{p} I(X; Y),$$
where the maximum runs over all probability mass functions $p$ on $\mathcal{X}$.

## Remarks

The maximum exists, since $I(X; Y)$ is a continuous function of $p$ on the compact simplex of probability vectors.
One has $0 \le C \le \min(\log_2 \abs{\mathcal{X}}, \log_2 \abs{\mathcal{Y}})$.
With natural logarithms the capacity is measured in nats.
Example: for the noiseless binary channel, $W(y \mid x) = 1$ if $y = x$, one has $I(X; Y) = H(X) \le 1$.
The uniform input reaches $1$, so $C = 1$ bit.
Non-example: the largest output entropy $\max_p H(Y)$ is not the capacity.
If $W(y \mid x) = 1/2$ for all $x, y \in \set{0,1}$, then $H(Y) = 1$, but $Y$ is independent of $X$, so $I(X; Y) = 0$ and $C = 0$.
The noisy-channel coding theorem gives $C$ its operational meaning as the largest reliable rate.
