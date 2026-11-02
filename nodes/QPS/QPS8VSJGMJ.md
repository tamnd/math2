---
tag: QPS8VSJGMJ
kind: concept
name: Dynamic programming in continuous time
msc: [49L20, 49L12, "93E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_programming
---

## Summary

Dynamic programming in continuous time solves an optimal control problem by studying its [[value function|K6G0DRQ3CP]] for all initial times and states at once.
Its basis is Bellman's principle of optimality: the tail of an optimal trajectory is optimal for the problem that starts where the tail starts.
In infinitesimal form this principle becomes the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]].
It gives optimal controls in feedback form, which complements the open-loop necessary conditions of [[Pontryagin's maximum principle|7RPV2T29CF]].

## Explanations

### L1 human

To plan the cheapest trip, one can work backward from the destination.
If you know the cheapest remaining cost from every place at a later time, the best move now is easy to find.
Dynamic programming in continuous time applies this idea at every instant.
The result is a rule that tells you what to do in every situation, not just along one planned path.
