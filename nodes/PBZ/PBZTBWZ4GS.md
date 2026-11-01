---
tag: PBZTBWZ4GS
kind: concept
name: Recurrence and transience of states
msc: [60J10]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete-time_Markov_chain
---

## Summary

A state of a [[Markov chain|0G48PYM96Q]] is recurrent if the chain, started there, returns to it with probability one, and transient otherwise.
A recurrent state is visited infinitely often, while a transient state is visited only finitely often, almost surely.
Recurrent states are further split into positive recurrent and null recurrent, according to whether the mean return time is finite.
In an irreducible chain all states have the same type, which decides whether a [[stationary distribution|0KRH5157WP]] exists.

## Explanations

### L1 human

Imagine a walker moving at random between rooms and ask whether she surely comes back to the room where she started.
If yes, the room is recurrent, and she will in fact come back again and again forever.
If there is a positive chance that she never returns, the room is transient, and after some last visit she leaves for good.
The fair coin walk on the integers comes back to $0$ for sure, while a walk that steps right with probability $2/3$ drifts away and may never return.
