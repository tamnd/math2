---
tag: WCNHWTJXYD
kind: concept
name: Markov decision process
msc: [90C40, "93E20", 60J20]
specializes: [0G48PYM96Q]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_decision_process
same_as:
  wikidata: Q176789
  wikipedia: Markov decision process
---

## Summary

A Markov decision process is a model of sequential decisions under uncertainty.
At each step a controller sees the current state, chooses an action and collects a reward.
Then the system moves to a random next state whose law depends only on the current state and action.
The aim is a rule for choosing actions, a policy, that makes the expected total reward as large as possible.
It is the basic model of [[stochastic dynamic programming|SDW79PBNWM]] and of reinforcement learning.

## Explanations

### L1 human

Think of a [[Markov chain|0G48PYM96Q]] in which, at each step, you may turn a knob that changes the transition probabilities.
Each turn of the knob also pays you something now, and it shapes where you will be later.
For example, a machine is either working or broken; each day you may repair it at a cost or leave it, and a working machine earns money but may break.
Repairing costs money today but makes tomorrow better.
A Markov decision process asks how to weigh present rewards against future ones in the best way.
