---
tag: NH54DP03BD
kind: concept
name: Cox–Ingersoll–Ross model
msc: [91G30, 60H10, 60J60]
specializes: [7TZ87AS1MW]
sources:
  - url: https://en.wikipedia.org/wiki/Cox%E2%80%93Ingersoll%E2%80%93Ross_model
same_as:
  wikidata: Q4385634
  wikipedia: Cox–Ingersoll–Ross model
---

## Summary

The Cox–Ingersoll–Ross (CIR) model is a [[short-rate model|7TZ87AS1MW]] in which the rate reverts to a long-run mean.
Its volatility is proportional to the square root of the rate.
It was introduced by John Cox, Jonathan Ingersoll and Stephen Ross in 1985.
The square root makes the noise vanish as the rate approaches zero, so the rate never becomes negative.
Bond prices have closed forms, and the same process models the variance in the [[Heston model|6PA46G33BB]].

## Explanations

### L1 human

The CIR model is like the Vasicek model, with one change: the random kicks get smaller when the rate is low.
Near zero the kicks almost vanish while the pull towards the long-run level stays, so the rate is pushed back up before it can go negative.
For example, at a rate of $1\%$ the kicks are only half as large as at a rate of $4\%$, since $\sqrt{0.01} = 0.1$ and $\sqrt{0.04} = 0.2$.
