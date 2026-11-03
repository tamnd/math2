---
tag: 6FZNDKFPHD
kind: definition
name: Greeks
msc: [91G20, 91G60]
defines: JBCDG4B9NW
uses: [09EGC6F8PT, FFT8TF6QP2, ZFTNJ2YREG]
sources:
  - url: https://en.wikipedia.org/wiki/Greeks_(finance)
---

## Definition

Let $V(S, t, \sigma, r)$ be the price of a derivative security given by a pricing model, such as the [[Black–Scholes model|FFT8TF6QP2]].
Here $S > 0$ is the price of the underlying asset, $t$ is the time, $\sigma > 0$ is the volatility and $r$ is the risk-free interest rate.
Assume $V$ has the [[partial derivatives|09EGC6F8PT]] below.
The *Greeks* of $V$ are:

1. delta $\Delta = \dfrac{\partial V}{\partial S}$;
2. gamma $\Gamma = \dfrac{\partial^2 V}{\partial S^2}$;
3. vega $\mathcal{V} = \dfrac{\partial V}{\partial \sigma}$;
4. theta $\Theta = \dfrac{\partial V}{\partial t}$;
5. rho $\rho = \dfrac{\partial V}{\partial r}$.

## Remarks

Example: in the Black–Scholes model a European call with strike $K$ and maturity $T$ has price $C = S N(d_1) - K e^{-r(T - t)} N(d_2)$.
Here $N$ is the standard normal distribution function, $d_1 = \dfrac{\ln(S/K) + (r + \sigma^2/2)(T - t)}{\sigma \sqrt{T - t}}$ and $d_2 = d_1 - \sigma\sqrt{T - t}$.
Differentiation gives $\Delta = N(d_1)$, which lies in $(0, 1)$, and $\Gamma = \dfrac{N'(d_1)}{S \sigma \sqrt{T - t}} > 0$.
Non-example: at expiry $t = T$ the call price is $\max(S - K, 0)$, which has no derivative in $S$ at $S = K$, so the delta is not defined there.
For any price $V$ that solves the [[Black–Scholes equation|ZFTNJ2YREG]], the Greeks satisfy $\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma + r S \Delta - r V = 0$.
Higher-order Greeks, such as $\partial^2 V / \partial S \, \partial \sigma$, are also in use.
