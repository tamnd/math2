---
tag: HB7J6SYG00
kind: definition
name: Parallel tempering
msc: [82M31, 65C05, 65C40]
defines: 30VRYRVGDN
uses: [ZGNBR2SPZ0, GYNMZ9201M, CTGN6CK1ZS, MKHF449E22]
sources:
  - url: https://en.wikipedia.org/wiki/Parallel_tempering
---

## Definition

Let $S$ be a finite set of configurations with energy $H \colon S \to \R$, and let $\pi_\beta(x) \propto e^{-\beta H(x)}$ be the [[Boltzmann distribution|GYNMZ9201M]] at inverse temperature $\beta$.
Fix inverse temperatures $0 < \beta_1 < \beta_2 < \dots < \beta_M$.
*Parallel tempering* is the Markov chain on $S^M$, with states $(x_1, \dots, x_M)$, whose steps are of two kinds.

1. Local moves: for each $i$, update $x_i$ by a Markov chain that leaves $\pi_{\beta_i}$ invariant.
2. Swap moves: choose $i \in \set{1, \dots, M - 1}$ and propose to exchange $x_i$ and $x_{i+1}$; accept the exchange with probability
$$\min\Big(1, \exp\big((\beta_i - \beta_{i+1}) (H(x_i) - H(x_{i+1}))\big)\Big).$$

## Remarks

Both kinds of moves leave the product measure $\pi_{\beta_1} \otimes \dots \otimes \pi_{\beta_M}$ invariant.
For the swap, the ratio of the product weights after and before is as follows.
$$\frac{\pi_{\beta_i}(x_{i+1}) \pi_{\beta_{i+1}}(x_i)}{\pi_{\beta_i}(x_i) \pi_{\beta_{i+1}}(x_{i+1})} = e^{(\beta_i - \beta_{i+1})(H(x_i) - H(x_{i+1}))},$$
so the rule of clause 2 is the [[Metropolis rule|MKHF449E22]] for a symmetric proposal, and it satisfies [[detailed balance|CTGN6CK1ZS]].
Hence the marginal of $x_M$ is $\pi_{\beta_M}$, and averages of $x_M$ estimate thermal averages at the lowest temperature.
Example: let the hotter copy $x_i$ have the lower energy.
Then $\beta_i - \beta_{i+1} < 0$ and $H(x_i) - H(x_{i+1}) < 0$, so the exponent is positive and the swap is always accepted.
In this way low-energy states move towards the cold end.
Non-example: accepting every swap would break the invariance, because a high-energy state from the hot copy would be pushed into the cold copy too often.
The temperatures must be close enough that the energy distributions of neighbouring copies overlap; otherwise almost all swaps are rejected.

## Explanations

### L1 human

Each copy samples its own temperature, and the swap rule is chosen so that this stays true after exchanges.
