---
tag: HJPPRZ29YE
kind: concept
name: Stochastic ordering
msc: ["60E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_ordering
same_as:
  wikidata: Q475164
  wikipedia: Stochastic ordering
---

## Summary

A stochastic ordering compares two random variables through their distributions, not through their values.
The basic one is the usual stochastic order.
In it, $X$ is stochastically smaller than $Y$ when $X$ is less likely than $Y$ to exceed every threshold.
Equivalently, there is a [[coupling|HTR7J0W66V]] of the two laws in which $X \le Y$ holds pointwise.
Other orders, such as the convex order and the hazard rate order, compare variability or ageing.
They are used in reliability theory, queueing, economics and decision theory.

## Explanations

### L1 human

One lottery is stochastically better than another if, for every amount of money, it is at least as likely to pay that amount or more.
For example, a waiting time with an [[exponential|0E99F51GVB]] law of rate $2$ is stochastically smaller than one with rate $1$, because $e^{-2t} \le e^{-t}$ for all $t \ge 0$.
Two bell curves centred at $0$ with different spreads are not comparable in this order.
Each one is more likely than the other to exceed some thresholds.
