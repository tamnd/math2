---
tag: B24T6DQCDR
kind: concept
name: Stochastic optimal control
msc: ["93E20", 49L20]
specializes: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_control
same_as:
  wikidata: Q7617811
  wikipedia: Stochastic control
---

## Summary

Stochastic optimal control is [[optimal control|T3V6ZNAMDN]] of systems driven by noise, usually modelled by a [[stochastic differential equation|B219G9SHJA]].
The controller chooses its action at each time from the information observed so far and minimises an expected cost.
Dynamic programming leads to a second-order [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]] for the value function.
The theory is used in engineering, in economics and in mathematical finance, for example in portfolio choice.

## Explanations

### L1 human

Think of steering a boat in gusty wind.
You cannot plan the whole path in advance, because the wind keeps pushing you off course.
Instead you decide at each moment what to do given where you are now.
A simple model is a position $X_t$ that moves with the chosen velocity $u_t$ plus a random [[Brownian|22735FGJV6]] kick.
The goal is to end near $0$ without spending too much effort.
The best rule turns out to be a feedback: push back towards $0$ in proportion to the current position.
