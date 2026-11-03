---
tag: Z94Z6BY8JG
kind: concept
name: Bellman equation
msc: [90C39, 90C40, 49L20]
sources:
  - url: https://en.wikipedia.org/wiki/Bellman_equation
same_as:
  wikidata: Q1430750
  wikipedia: Bellman equation
---

## Summary

The Bellman equation describes the optimal value of a sequential decision problem from a given state.
This value is the best, over all actions, of the immediate reward plus the discounted expected optimal value of the next state.
It is the recurrence at the heart of [[dynamic programming|R3FXF08WBH]], named after Richard Bellman.
For discounted Markov decision processes the [[value function|K6G0DRQ3CP]] is its unique bounded solution, and optimal policies choose actions that attain the maximum.
Its continuous-time analogue is the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]].

## Explanations

### L1 human

To plan the best route home, it is enough to know the best remaining route from every crossroad.
Then at each crossroad you pick the next street that minimizes "this street plus the best route from its end".
The Bellman equation writes this self-consistency as an equation for the unknown "best value from here".
For a game that pays $1$ every round forever with discount factor $\gamma < 1$, the value $V$ satisfies $V = 1 + \gamma V$, so $V = 1/(1 - \gamma)$.
