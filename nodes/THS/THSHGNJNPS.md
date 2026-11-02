---
tag: THSHGNJNPS
kind: concept
name: Differential game
msc: [91A23, 49N70]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_game
same_as:
  wikidata: Q1973196
  wikipedia: Differential game
---

## Summary

A differential game is a game in which several players steer a common state through a [[control system|ZPDTVZQN5K]].
The state obeys a differential equation driven by all their controls.
Each player has a cost or payoff that depends on the resulting trajectory, and the players have different goals.
With one player it is an [[optimal control|T3V6ZNAMDN]] problem.
The two-player zero-sum case leads to the [[Hamilton–Jacobi–Isaacs equation|WHTBZ3K4FB]], and pursuit problems are the classical examples.

## Explanations

### L1 human

Picture a cat chasing a mouse in a field.
Both move continuously, and each changes direction at every instant in reaction to the other.
The cat wants to catch the mouse quickly, the mouse wants to escape or at least delay capture.
A differential game is the mathematical model of such a contest: the positions obey differential equations, and each player chooses its control as time runs.
In a simple version, both move in the plane with bounded speed, the cat faster, and the payoff is the time to capture.
