---
tag: BBZP1R872N
kind: concept
name: Dynamical system
msc: [37B02, 37C10, 37-01]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_system
same_as:
  wikidata: Q638328
  wikipedia: Dynamical system
---

## Summary

A dynamical system is a space of states together with a rule that moves each state forward in time.
Time can be discrete, as in the repeated application of one map, or continuous, as in the solutions of an autonomous differential equation.
The rule must be consistent: waiting for time $s$ and then for time $t$ is the same as waiting for time $s + t$.
Dynamical systems model planets, populations, chemical reactions and many other processes, and their study asks what happens in the long run.

## Explanations

### L1 human

Think of a state as a snapshot of a system, such as the position and speed of a pendulum.
The dynamical system tells where the snapshot will be after any amount of time.
The set of all snapshots, the phase space, is often pictured as a landscape on which each point moves along a path.
A simple example is the map $x \mapsto x/2$ on the real line, with time counted in whole steps.
After $n$ steps the state $x$ has become $x / 2^n$, so every state drifts to $0$.
