---
tag: Q6GZN4JWJP
kind: concept
name: Belief propagation decoding
msc: [94B35, 62F15]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Belief_propagation
---

## Summary

Belief propagation decoding is an iterative message-passing decoder for codes defined by a sparse [[Tanner graph|GTDMNAMPD9]], such as [[low-density parity-check codes|JJH68RANFH]].
Variable nodes and check nodes repeatedly send each other estimates of the probability that a bit is $0$ or $1$.
These are usually log-likelihood ratios.
When the Tanner graph has no cycles, it computes exactly the bitwise [[posterior probabilities|0KJ7ZS8AJA]].
On graphs with cycles it is an approximation that works very well in practice.
It is the coding instance of belief propagation, the sum-product algorithm on [[graphical models|Q3FQAD1BXG]].

## Explanations

### L1 human

Each bit starts with an opinion from the channel: how much the received signal favours $0$ over $1$.
Each check then tells each of its bits what the other bits of the check suggest it should be, since their sum must be even.
Each bit combines the channel's opinion with the advice of its other checks and sends the result back.
On the erasure channel this becomes very simple: a check with exactly one unknown bit fixes that bit, and the process repeats.
For example, with the check $x_1 + x_2 + x_3 = 0$ and the received word $(0, ?, 1)$, the check sets $x_2 = 1$.
