---
tag: MPN10SB26R
kind: concept
name: Autoregressive conditional heteroskedasticity
msc: [62M10, 91G70, 62P20]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity
same_as:
  wikidata: Q180752
  wikipedia: Autoregressive conditional heteroskedasticity
---

## Summary

An autoregressive conditional heteroskedasticity (ARCH) model is a [[time series|EA3MF4VTEH]] model with a changing variance.
The [[conditional variance|0VGPX25NXQ]] of today's shock depends on the squares of past shocks.
It describes series whose volatility changes over time and comes in clusters, which is typical of financial returns.
The model was introduced by Robert Engle, and its extension GARCH also lets past conditional variances enter the equation.
It is a basic example of [[heteroscedasticity|D8VX6XQ3TT]] in time.

## Explanations

### L1 human

Stock prices move calmly for a while and then wildly for a while.
An ARCH model captures this: after a big move, the next move is likely to be big too, in either direction.
The size of the noise today is computed from how large the recent noises were.
For example, in an ARCH(1) model the variance today is $\alpha_0 + \alpha_1 \varepsilon_{t-1}^2$, so a large surprise yesterday raises the uncertainty today.
