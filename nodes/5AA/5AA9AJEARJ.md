---
tag: 5AA9AJEARJ
kind: concept
name: Discrete-time dynamical system
msc: [37B02, 37C05, 37-01]
specializes: [BBZP1R872N]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_system
---

## Summary

A discrete-time dynamical system is a [[dynamical system|BBZP1R872N]] in which time advances in whole steps.
It is given by a single map $f$ of a space to itself, and the state after $n$ steps is the [[iterate|AYVTR2ES5B]] $f^n(x)$.
Such systems arise from sampling a continuous motion at regular times, from population models with generations, and from numerical methods.
Many basic phenomena of dynamics, such as chaos and period doubling, are already visible in maps of an interval.

## Explanations

### L1 human

Imagine pressing a button that changes the state of a system by a fixed rule, and pressing it again and again.
The sequence of states $x, f(x), f(f(x)), \dots$ is the orbit of the starting state.
For example, take the rule $f(x) = x^2$ on the real numbers and start at $x = 1/2$.
The orbit is $1/2, 1/4, 1/16, 1/256, \dots$, and it rushes to $0$.
Starting at $x = 2$ instead gives $2, 4, 16, 256, \dots$, which runs off to infinity.
