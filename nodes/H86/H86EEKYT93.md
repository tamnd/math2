---
tag: H86EEKYT93
kind: definition
name: Monte Carlo method in statistical physics
msc: [82M31, 65C05, 65C40]
defines: DR0E829VX6
uses: [ZGNBR2SPZ0, GYNMZ9201M, 0KRH5157WP, CTGN6CK1ZS, MKHF449E22, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_method_in_statistical_mechanics
---

## Definition

Let $S$ be a finite set of configurations, let $H \colon S \to \R$ be an energy function, and let $\beta > 0$ be the inverse temperature.
Let $\pi(\sigma) = e^{-\beta H(\sigma)} / Z$ with $Z = \sum_{\tau \in S} e^{-\beta H(\tau)}$ be the [[Boltzmann distribution|GYNMZ9201M]], and let $A \colon S \to \R$ be an observable.
A *Monte Carlo method* for the thermal average $\langle A \rangle = \sum_\sigma A(\sigma) \pi(\sigma)$ consists of:

1. an irreducible Markov chain $(X_t)_{t \ge 0}$ on $S$ with transition matrix $P$ and [[stationary distribution|0KRH5157WP]] $\pi$, often checked by [[detailed balance|CTGN6CK1ZS]]: $\pi(\sigma) P(\sigma, \tau) = \pi(\tau) P(\tau, \sigma)$ for all $\sigma, \tau$;
2. the estimator $\bar A_n = \frac{1}{n} \sum_{t = t_0 + 1}^{t_0 + n} A(X_t)$, where $t_0 \ge 0$ is a number of discarded initial steps.

## Remarks

For an irreducible chain on a finite set with stationary distribution $\pi$, the ergodic theorem for Markov chains gives $\bar A_n \to \langle A \rangle$ almost surely as $n \to \infty$, for every starting state.
The Markov chain avoids computing $Z$, since only ratios $\pi(\tau)/\pi(\sigma) = e^{-\beta (H(\tau) - H(\sigma))}$ appear.
Example: the [[Metropolis algorithm|MKHF449E22]] for the [[Ising model|R0KGM32QN6]] picks a uniform random site, proposes to flip its spin, and accepts with probability $\min(1, e^{-\beta \Delta H})$, where $\Delta H$ is the energy change.
The proposal is symmetric, so $\pi(\sigma) P(\sigma, \tau) = \frac{1}{\abs{V}} \min(\pi(\sigma), \pi(\tau))$ for a single flip, where $V$ is the set of sites.
This is symmetric in $\sigma, \tau$, which checks detailed balance.
Non-example: averaging $A$ over uniform samples from $S$ estimates the average at infinite temperature, not $\langle A \rangle$.
Its chain has the uniform stationary distribution, so clause 1 fails for $\beta > 0$ unless $H$ is constant.
The error of $\bar A_n$ is proportional to $\sqrt{\tau / n}$, where $\tau$ is the integrated autocorrelation time of $A$; near a critical point $\tau$ becomes large, which motivates cluster algorithms.

## Explanations

### L1 human

The method replaces a sum over all configurations by an average along a random walk in configuration space.
The walk is built so that it spends time in each configuration in proportion to its Boltzmann weight.
