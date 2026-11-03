---
tag: 3QKZC4PA42
kind: definition
name: Volatility smile
msc: [91G20, 91G70]
defines: 2TYE23YVS5
uses: [XNA12XG7ZK, FFT8TF6QP2]
sources:
  - url: https://en.wikipedia.org/wiki/Volatility_smile
---

## Definition

Fix an asset and a maturity $T > 0$.
For each strike $K > 0$ let $\sigma_{\mathrm{imp}}(K, T)$ be the [[implied volatility|XNA12XG7ZK]] of the European option with strike $K$ and maturity $T$.
The *volatility smile* at maturity $T$ is the function $K \mapsto \sigma_{\mathrm{imp}}(K, T)$.
The function $(K, T) \mapsto \sigma_{\mathrm{imp}}(K, T)$ of both variables is the *implied volatility surface*.

## Remarks

Example: if market prices of index options give $\sigma_{\mathrm{imp}} = 0.30$ at $K = 80$, $0.20$ at $K = 100$ and $0.17$ at $K = 120$, the smile at that maturity is decreasing, which is called a skew.
Non-example of a non-flat smile: if all prices come from the [[Black–Scholes model|FFT8TF6QP2]] with volatility $\sigma$, then $\sigma_{\mathrm{imp}}(K, T) = \sigma$ for all $K$, and the smile is a horizontal line.
The smile is often drawn against the moneyness $K / S$ or the log-moneyness $\ln(K / F)$, where $F$ is the forward price, instead of $K$.
A U-shaped graph is called a smile, and a monotone one is called a skew or smirk.
