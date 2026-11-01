---
tag: TWQFE0FZZS
kind: concept
name: Continuous-time Markov chain
msc: [60J27]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous-time_Markov_chain
same_as:
  wikidata: Q176720
  wikipedia: Continuous-time Markov chain
---

## Summary

A continuous-time Markov chain is a process with values in a countable set that jumps between states at random times and has the [[Markov property|0B77KZCQ51]].
It stays in each state for an [[exponentially distributed|0E99F51GVB]] time, and then jumps according to fixed probabilities.
Its law is described by a rate matrix $Q$, and on a finite set its transition probabilities form the [[matrix exponential|020M04FN1H]] $e^{tQ}$.
Queues, birth–death processes and the Poisson process are standard examples.

## Explanations

### L1 human

A discrete-time [[Markov chain|0G48PYM96Q]] moves at each tick of a clock.
A continuous-time chain instead waits a random amount of time in each state before it moves.
The waiting time has no memory: having waited a while does not make a jump more or less likely soon.
For example, a machine that breaks down at rate $a$ and is repaired at rate $b$ is a chain on two states, working and broken.
In the long run it is working a fraction $b/(a + b)$ of the time.
