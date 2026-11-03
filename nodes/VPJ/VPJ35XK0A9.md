---
tag: VPJ35XK0A9
kind: concept
name: Gillespie algorithm
msc: [65C05, 60J28, "92E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Gillespie_algorithm
same_as:
  wikidata: Q5562121
  wikipedia: Gillespie algorithm
---

## Summary

The Gillespie algorithm, also called the stochastic simulation algorithm, draws exact sample paths of a well-mixed chemical system.
The law of these paths is given by the [[chemical master equation|VTE4ZCT4WJ]].
At each step it draws the waiting time to the next reaction from an [[exponential distribution|0E99F51GVB]].
Then it chooses which reaction occurs, in proportion to the propensities.
It is a [[Monte Carlo method|HWP11G3HTN]] for [[continuous-time Markov chains|TWQFE0FZZS]], and it is the standard tool to simulate gene expression and other small-number chemistry.

## Explanations

### L1 human

Imagine a box with a few molecules that react now and then.
Instead of solving equations for all probabilities, the algorithm plays the system forward one reaction at a time.
It asks two random questions: how long until the next reaction, and which reaction it is.
Faster reactions get picked more often, and the waiting time is short when many reactions are possible.
Repeating the run many times gives the spread of possible outcomes.
