---
tag: YW5P7NEKR4
kind: concept
name: Topology of uniform convergence
msc: [54C35, "54E35"]
specializes: [0YVKNB7V5F]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
---

## Summary

The topology of uniform convergence is the topology on a set of functions into a metric space in which convergence means [[uniform convergence|08VZ57PT26]].
It comes from the uniform metric, which measures the largest distance between the values of two functions.
It is finer than the [[topology of pointwise convergence|FVGB8ZP67B]].
On continuous maps, uniform limits stay continuous, which is why this topology is so useful.

## Explanations

### L1 human

Two functions are close in this topology when their graphs stay close everywhere at once.
A band of fixed width around the graph of $f$ must contain the whole graph of $g$.
For example, $f_n(x) = x / n$ on $[0, 1]$ converges uniformly to $0$, since $\abs{f_n(x)} \le 1/n$ for all $x$.
But $f_n(x) = x^n$ on $[0, 1)$ does not, because near $x = 1$ the values stay close to $1$.
