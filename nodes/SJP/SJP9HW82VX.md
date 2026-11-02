---
tag: SJP9HW82VX
kind: concept
name: Hamilton–Jacobi–Bellman equation
msc: [49L12, 49L20]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton–Jacobi–Bellman_equation
same_as:
  wikidata: Q3302775
  wikipedia: Hamilton–Jacobi–Bellman equation
---

## Summary

The Hamilton–Jacobi–Bellman equation is a first-order partial differential equation for the [[value function|K6G0DRQ3CP]] of an [[optimal control|T3V6ZNAMDN]] problem.
It is the continuous-time form of the principle of [[dynamic programming|QPS8VSJGMJ]]: an optimal strategy stays optimal from every later state.
A solution gives the optimal cost from every starting point and, through a pointwise minimization, an optimal feedback control.
In general the value function is not differentiable, and the equation is understood in the sense of [[viscosity solutions|H1ERJ3T75T]].

## Explanations

### L1 human

Think of the cheapest cost to reach the end of a journey from each place and each time.
If you know this cost everywhere, the best move now is the one that leads to the place with the smallest remaining cost plus the cost of the move.
The Hamilton–Jacobi–Bellman equation writes this idea as an equation for the cost function.
It is the counterpart of [[Pontryagin's maximum principle|7RPV2T29CF]], which describes one optimal path instead of all optimal costs.
