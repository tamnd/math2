---
tag: SDW79PBNWM
kind: concept
name: Stochastic dynamic programming
msc: [90C39, 90C40, "93E20"]
specializes: [R3FXF08WBH]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_dynamic_programming
same_as:
  wikidata: Q28137009
  wikipedia: Stochastic dynamic programming
---

## Summary

Stochastic dynamic programming is [[dynamic programming|R3FXF08WBH]] for decision problems in which the next state is random.
A decision is taken at each stage after the current state is seen.
The aim is to minimize an expected total cost or to maximize an expected total reward.
The optimal value satisfies a backward recursion, the [[Bellman equation|Z94Z6BY8JG]], in which an expectation over the random outcome appears.
It is the solution method for [[Markov decision processes|WCNHWTJXYD]] and for many models of inventory, finance and control.

## Explanations

### L1 human

You plan over several rounds, and after each choice chance decides where you land.
You cannot fix all your choices in advance, because the best choice in a later round depends on what chance did before.
So you work backwards: first find the best choice in the last round for every possible situation.
Then use these values to find the best choice in the round before, and so on.
For example, a gambler with a fixed number of bets left wants to know how much to stake.
The gambler can first solve the case of one bet left, for each amount of money, and work back from there.
