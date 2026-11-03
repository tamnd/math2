---
tag: B7XZ76EX1T
kind: concept
name: Partially observable Markov decision process
msc: [90C40, "93E20", "93E11"]
specializes: [WCNHWTJXYD]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process
same_as:
  wikidata: Q176814
  wikipedia: Partially observable Markov decision process
---

## Summary

A partially observable Markov decision process is a [[Markov decision process|WCNHWTJXYD]] in which the controller does not see the state.
It sees only a random observation whose law depends on the state, so it must act on its knowledge of where the system might be.
This knowledge is summarized by a belief, a probability distribution on the states, which is updated by [[Bayes' theorem|0NM6E9VW04]] after each action and observation.
The model covers robot navigation, medical decisions and machine maintenance under noisy measurements.

## Explanations

### L1 human

Imagine steering a robot in a building where you never see its exact position; you only get blurry sensor readings.
After each move and each reading you keep a list of how likely each position is, and you update it like a detective.
Good decisions are based on this list, not on a single guess.
A [[hidden Markov model|HJVM390354]] is the same picture without decisions; a partially observable Markov decision process adds the actions and rewards.
