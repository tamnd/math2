---
tag: FDN6HFS4KM
kind: definition
name: Implied volatility
msc: [91G20, 91G70]
defines: XNA12XG7ZK
uses: [FFT8TF6QP2, JBCDG4B9NW, 6QHFMX4ZHV]
sources:
  - url: https://en.wikipedia.org/wiki/Implied_volatility
---

## Definition

Consider a European call option with strike $K > 0$ and time to maturity $\tau > 0$.
The underlying asset has price $S > 0$ and pays no dividends, and $r$ is the risk-free rate.
Let $C_{\mathrm{BS}}(\sigma)$ be the call price in the [[Black–Scholes model|FFT8TF6QP2]] with volatility $\sigma > 0$.
Let $C$ be an observed call price with $\max(S - K e^{-r\tau}, 0) < C < S$.
The *implied volatility* of $C$ is the unique $\sigma_{\mathrm{imp}} > 0$ such that $C_{\mathrm{BS}}(\sigma_{\mathrm{imp}}) = C$.

## Remarks

The value exists and is unique because $\sigma \mapsto C_{\mathrm{BS}}(\sigma)$ is continuous and strictly increasing on $(0, \infty)$.
Its derivative is the vega $S N'(d_1) \sqrt{\tau} > 0$ (see [[Greeks|JBCDG4B9NW]]), and its limits are $\max(S - K e^{-r\tau}, 0)$ as $\sigma \to 0$ and $S$ as $\sigma \to \infty$.
Example: if $C = C_{\mathrm{BS}}(0.2)$, then the implied volatility is $0.2$ by uniqueness.
Non-example: a price $C \ge S$ has no implied volatility, since every Black–Scholes call price is below $S$; such a price also allows arbitrage.
By [[put–call parity|6QHFMX4ZHV]], a European put with the same strike and maturity has the same implied volatility as the call.
In practice $\sigma_{\mathrm{imp}}$ is computed numerically, for example by Newton's method using the vega.
