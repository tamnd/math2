---
tag: WS9A6N2Y0F
kind: concept
name: Mean-field game
msc: [91A16, 35Q89, 49N80]
sources:
  - url: https://en.wikipedia.org/wiki/Mean-field_game_theory
same_as:
  wikidata: Q15883550
  wikipedia: Mean-field game theory
---

## Summary

A mean-field game is a differential game with a very large number of small, identical players.
Each player reacts only to the distribution of all the others.
In the limit of infinitely many players, a Nash equilibrium is described by a coupled system of two partial differential equations.
A [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]] backward in time gives the optimal strategy of one player.
A [[Fokker–Planck equation|FVQWR7NS00]] forward in time gives the evolution of the distribution of players.
The theory was introduced independently by Jean-Michel Lasry and Pierre-Louis Lions and by Minyi Huang, Roland Malhamé and Peter Caines.

## Explanations

### L1 human

Think of a crowd leaving a stadium: each person chooses a path to the exit, and the best path depends on where everyone else goes.
No single person changes the crowd, but the crowd shapes every choice.
An equilibrium is a crowd movement in which nobody can do better by changing their own path, given the movement of the crowd.
Mean-field games compute such equilibria by treating the crowd as a continuous density.
The same idea models traders in a market, drivers in traffic and firms competing for a resource.
