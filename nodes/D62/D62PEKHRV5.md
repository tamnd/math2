---
tag: D62PEKHRV5
kind: concept
name: Equilibrium of a difference equation
msc: [39A05, 37C25]
specializes: [R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed_point_(mathematics)
---

## Summary

An equilibrium of an autonomous difference equation $x_{n+1} = f(x_n)$ is a point $x^*$ with $f(x^*) = x^*$, that is, a [[fixed point|R6QVS6P21N]] of $f$.
Starting there, the solution stays there forever, so equilibria are the constant solutions.
They are the discrete-time analogue of the [[equilibrium points|0N8NGKDZDZ]] of differential equations.
The first question about a nonlinear difference equation is usually where its equilibria are and whether nearby solutions approach them.

## Explanations

### L1 human

A difference equation tells you how a state changes from one time step to the next.
An equilibrium is a state that the rule leaves unchanged.
On a graph of $f$, the equilibria are where the graph crosses the line $y = x$.
For the population rule $x_{n+1} = 2 x_n (1 - x_n)$, the equilibria are $0$ and $1/2$: a population of $1/2$ stays at $1/2$.
