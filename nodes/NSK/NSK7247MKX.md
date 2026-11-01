---
tag: NSK7247MKX
kind: concept
name: Supermartingale
msc: [60G42, 60G44]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Martingale_(probability_theory)
---

## Summary

A supermartingale is an adapted, integrable [[stochastic process|0QH5ENKZM1]] whose [[conditional expectation|0TTDGTEFMN]] of a future value, given the present information, is at most the present value.
It models the fortune of a player in a game that is unfavourable or fair.
A process is a supermartingale exactly when its negative is a [[submartingale|6M852B4RA8]].
Non-negative supermartingales converge almost surely, a fact used throughout probability and potential theory.

## Explanations

### L1 human

A supermartingale tends to go down, or at least not up, on average.
It is the right model for your money in a casino, where every game is slightly in favour of the house.
Given what you know now, the expected value of your fortune later is at most what you hold now.
For example, bet one unit on each toss of a coin that lands heads with probability $0.45$, and win the unit on heads or lose it on tails.
Your fortune after each toss is a supermartingale, since each bet loses $0.1$ on average.
