---
tag: ZFTNJ2YREG
kind: concept
name: Black–Scholes equation
msc: [35Q91, 91G20]
sources:
  - url: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_equation
same_as:
  wikidata: Q17005676
  wikipedia: Black–Scholes equation
---

## Summary

The Black–Scholes equation is the linear parabolic equation $V_t + \frac{1}{2}\sigma^2 S^2 V_{SS} + r S V_S - r V = 0$ for the price $V(S, t)$ of a financial option.
It assumes that the price $S$ of the underlying asset follows [[geometric Brownian motion|D48DR46B97]] with volatility $\sigma$.
It also assumes that money earns the constant interest rate $r$.
It is solved backward in time from the payoff at expiry.
A change of variables, starting with $x = \log S$ and reversing time, turns it into the [[heat equation|VP2HN86VAG]].

## Explanations

### L1 human

An option is a contract whose value at a future date $T$ depends on the price of a stock then.
The equation says how much the option is worth today.
The key idea is that a portfolio of the option and the stock can be kept free of risk, so it must grow at the rate $r$.
For a call option with strike $K$, the final value is $\max(S - K, 0)$, and the equation gives the Black–Scholes formula for earlier times.
