---
tag: 8NT5CFG2ZR
kind: concept
name: Lévy process
msc: [60G51, 60J25]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Lévy_process
same_as:
  wikidata: Q1557613
  wikipedia: Lévy process
---

## Summary

A Lévy process is a stochastic process that starts at $0$ and has independent and stationary increments, with paths continuous in probability.
It is the continuous-time analogue of a random walk.
Brownian motion and the Poisson process are the two basic examples, and every Lévy process combines a drift, a Brownian part and jumps.
The law of each $X_t$ is [[infinitely divisible|BX3V3NYM1Y]], and the [[Lévy–Khintchine representation|Q82B4H4Z4J]] describes all of them.

## Explanations

### L1 human

A Lévy process moves by random increments that do not remember the past and do not depend on the clock.
What happens between time $1$ and time $2$ has the same law as what happens between time $5$ and time $6$, and the two pieces are independent.
The path may move continuously, like Brownian motion, or jump, like a counter of random clicks.
For example, the number of radioactive decays up to time $t$ is a Poisson process, a Lévy process that jumps by $1$.
