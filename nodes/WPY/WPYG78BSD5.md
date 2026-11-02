---
tag: WPYG78BSD5
kind: concept
name: Stochastic difference equation
msc: [39A50, 62M10]
sources:
  - url: https://en.wikipedia.org/wiki/Autoregressive_model
---

## Summary

A stochastic difference equation is a difference equation driven by random inputs, such as $X_{n+1} = f(X_n, \xi_{n+1})$ with a sequence of random noise terms $\xi_n$.
Its solution is a [[stochastic process|0QH5ENKZM1]] in discrete time rather than a single sequence.
The [[autoregressive model|2JC96FMGA1]] of time series analysis and the [[random walk|04VZE3FZXF]] are the basic linear examples.
When the noise terms are independent of each other and of the start, the solution is a [[Markov chain|0G48PYM96Q]].

## Explanations

### L1 human

A deterministic recursion computes the next state from the present one by a fixed rule.
A stochastic recursion also adds a fresh random shock at each step.
For example, $X_{n+1} = \tfrac{1}{2} X_n + \xi_{n+1}$ with independent coin-flip shocks $\xi_n = \pm 1$ keeps pulling the state toward $0$ while the shocks push it around.
One then studies averages, spreads and long-run distributions instead of exact values.
