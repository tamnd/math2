---
tag: 8M31QKB0GW
kind: concept
name: Admissible control
msc: [49J15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
---

## Summary

An admissible control is an input function that is allowed in a given control problem.
It takes values in the prescribed control set, and it is regular enough for the state equation to make sense.
It also steers the state from the initial point to the target within the time horizon.
The cost of an optimal control problem is minimized over the admissible controls only.
The [[definition|8GETTS41P6]] gives the conditions for a [[control system|ZPDTVZQN5K]] driven by an ordinary differential equation.

## Explanations

### L1 human

A control problem fixes the rules of the game before asking for the best strategy.
The rules say which values the control may take, for example a throttle between $0$ and $1$.
They also say which goal must be reached, for example arriving at a given place at a given time.
A control that obeys all the rules is admissible.
For $x' = u$ with $\abs{u} \le 1$, starting at $x(0) = 0$ and required to reach $x(1) = \tfrac12$, the constant control $u = \tfrac12$ is admissible, while $u = 1$ overshoots and is not.
