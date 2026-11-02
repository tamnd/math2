---
tag: K6G0DRQ3CP
kind: concept
name: Value function
msc: [49L20, 49L12, "93E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Value_function
same_as:
  wikidata: Q65929180
  wikipedia: Value function
---

## Summary

The value function of an optimal control problem gives the optimal cost as a function of the initial time and the initial state.
It is the central object of dynamic programming: it satisfies the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]], in the [[viscosity|H1ERJ3T75T]] sense when it is not smooth.
Its gradient, where it exists, is the costate of [[Pontryagin's maximum principle|7RPV2T29CF]] up to sign.
In economics the same notion appears as the indirect utility or the optimal value of a maximization problem.

## Explanations

### L1 human

Imagine a map that shows, at each place and each time, the least cost to finish a journey from there.
That map is the value function.
If you know it, you can always choose the move that leads to the cheapest remaining cost.
For example, if you can walk at speed at most $1$ and pay the distance to the origin that is left at time $T$, the value at $(t, x)$ is $\max(\abs{x} - (T - t), 0)$.
