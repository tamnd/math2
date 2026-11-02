---
tag: THCM7DWHNY
kind: concept
name: Resistance form
msc: ["31E05", "31C25", "28A80"]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_on_fractals
---

## Summary

A resistance form is a quadratic energy form on functions on a set which behaves like the energy of an electrical network.
It was introduced by Jun Kigami.
It gives a common frame to energies on finite networks, on intervals and on fractals such as the Sierpiński gasket.
Each resistance form defines a metric, the resistance metric.
It generalizes the [[effective resistance|XAE5YJ3H68]] between two nodes of a network.
Under mild conditions a resistance form is also a [[Dirichlet form|MH20Q2N1AH]].
So it gives a Laplacian, a heat equation and a diffusion process on the set.

## Explanations

### L1 human

Think of a network of wires that joins some points, and put a voltage $u(x)$ at each point $x$.
The energy of $u$ is the heat produced by the currents, a sum of terms $c \, (u(x) - u(y))^2$ over the wires.
A resistance form keeps the main features of this energy but allows infinitely many points, such as all points of a fractal.
The effective resistance between two points $x$ and $y$ is then the largest value of $(u(x) - u(y))^2$ among voltages of energy $1$.
On the interval $[0, 1]$ with energy $\int_0^1 u'(s)^2 \, ds$, this resistance between $x$ and $y$ is just $\abs{x - y}$, like a uniform wire.
