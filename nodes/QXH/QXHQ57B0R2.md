---
tag: QXHQ57B0R2
kind: concept
name: Vasicek model
msc: [91G30, 60H10]
specializes: [7TZ87AS1MW]
sources:
  - url: https://en.wikipedia.org/wiki/Vasicek_model
same_as:
  wikidata: Q2331759
  wikipedia: Vasicek model
---

## Summary

The Vasicek model is a [[short-rate model|7TZ87AS1MW]] in which the short rate is an [[Ornstein–Uhlenbeck process|HZM2ASCDY4]].
It was introduced by Oldřich Vašíček in 1977.
The rate is pulled back towards a long-run mean and receives Gaussian noise of constant size.
Bond prices have closed forms, but the rate can become negative.

## Explanations

### L1 human

In the Vasicek model the interest rate is like a ball on a spring that is randomly kicked.
The spring pulls it back towards a long-run level $b$, and the kicks have a fixed typical size $\sigma$.
If the rate is above $b$ it tends to fall, and if it is below $b$ it tends to rise.
For example, with $b = 4\%$ and a current rate of $6\%$, the expected rate in the future moves down towards $4\%$.
Because the kicks do not shrink near zero, the rate can go below zero.
