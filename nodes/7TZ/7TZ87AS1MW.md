---
tag: 7TZ87AS1MW
kind: concept
name: Short-rate model
msc: [91G30, 60H10]
sources:
  - url: https://en.wikipedia.org/wiki/Short-rate_model
same_as:
  wikidata: Q4162534
  wikipedia: Short-rate model
---

## Summary

A short-rate model describes the whole term structure of interest rates through one process: the instantaneous interest rate $r_t$, called the short rate.
The short rate is modelled by a [[stochastic differential equation|B219G9SHJA]] under a [[risk-neutral measure|858BHBY2BD]].
The price of a zero-coupon bond is then the expected discount factor $\exp(-\int_t^T r_s \, ds)$.
The [[Vasicek|QXHQ57B0R2]], [[Cox–Ingersoll–Ross|NH54DP03BD]] and [[Hull–White|KA4EA7GTAF]] models are the classical examples.

## Explanations

### L1 human

Money in a bank account grows at an interest rate that changes over time.
A short-rate model treats today's very-short-term rate as a randomly moving number.
From its random path one gets the growth of the bank account and, by averaging, the prices of bonds of every maturity.
For example, if the short rate were constant at $3\%$, a bond paying $1$ in $10$ years would cost $e^{-0.3} \approx 0.74$ today.
