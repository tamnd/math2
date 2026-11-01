---
tag: A02K3MKQ3Q
kind: definition
name: Metropolis–Hastings algorithm
msc: [65C05, 60J22, 65C40]
defines: MKHF449E22
uses: [033TJBZDG0, 0F462493EA, CTGN6CK1ZS, 0KRH5157WP, ZGNBR2SPZ0]
sources:
  - url: https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm
---

## Definition

Let $S$ be a countable set and let $\pi$ be a probability distribution on $S$ with $\pi(x) > 0$ for all $x \in S$.
Let $Q = (Q(x, y))_{x, y \in S}$ be a [[transition matrix|0F462493EA]], the *proposal*, such that $Q(x, y) > 0$ if and only if $Q(y, x) > 0$.
For $x \ne y$ with $Q(x, y) > 0$, the *acceptance probability* is
$$\alpha(x, y) = \min\left(1, \frac{\pi(y) \, Q(y, x)}{\pi(x) \, Q(x, y)}\right).$$
The *Metropolis–Hastings chain* is the [[Markov chain|033TJBZDG0]] $(X_n)$ built as follows.
Given $X_n = x$, draw $Y$ from $Q(x, \cdot)$.
With probability $\alpha(x, Y)$ set $X_{n+1} = Y$; otherwise set $X_{n+1} = x$.
Its transition matrix has $P(x, y) = Q(x, y) \, \alpha(x, y)$ for $y \ne x$ and $P(x, x) = 1 - \sum_{y \ne x} P(x, y)$.

## Remarks

For $x \ne y$, $\pi(x) P(x, y) = \min\left(\pi(x) Q(x, y), \pi(y) Q(y, x)\right)$, which is symmetric in $x$ and $y$.
So $P$ satisfies [[detailed balance|CTGN6CK1ZS]] with respect to $\pi$, and $\pi$ is a [[stationary distribution|0KRH5157WP]].
Only the ratio $\pi(y)/\pi(x)$ is used, so $\pi$ may be known up to a constant factor.
Example: if $Q$ is symmetric, $\alpha(x, y) = \min(1, \pi(y)/\pi(x))$; this special case is the Metropolis algorithm.
Non-example: the chain that always accepts the proposal has transition matrix $Q$, whose stationary law is in general not $\pi$; it skips the acceptance step.
The chain is a [[Markov chain Monte Carlo|ZGNBR2SPZ0]] method when it is also irreducible.
The same construction works on general state spaces with densities in place of $\pi$ and $Q$.
