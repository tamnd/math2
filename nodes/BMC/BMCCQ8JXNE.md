---
tag: BMCCQ8JXNE
kind: concept
name: Prolongation of a section to a jet bundle
msc: [58A20]
sources:
  - url: https://en.wikipedia.org/wiki/Jet_bundle
---

## Summary

Let $s$ be a section of a fiber bundle.
Its $k$-th prolongation is the section $j^k s$ of the [[jet bundle|HC3VBBCJQP]] that sends each point $p$ to the [[$k$-jet|1QE0Z0756D]] of $s$ at $p$.
It lifts a section to a section that also records all derivatives up to order $k$.
A section of the jet bundle that arises in this way is called holonomic.
Prolongations let one write a differential equation as the condition that $j^k s$ takes values in a given subset of the jet bundle.

## Explanations

### L1 human

Take a function $u = s(x)$ of one variable.
Its first prolongation is the curve $x \mapsto (x, s(x), s'(x))$ in the space with coordinates $(x, u, u_x)$.
For $s(x) = x^2$ this curve is $x \mapsto (x, x^2, 2x)$.
Not every curve $x \mapsto (x, u(x), p(x))$ in that space is a prolongation: the third coordinate must be the derivative of the second.
That is the whole point of prolongation: it ties the slope coordinate to the actual slope.
