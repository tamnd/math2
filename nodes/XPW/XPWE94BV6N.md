---
tag: XPWE94BV6N
kind: concept
name: Contraction semigroup
msc: [47D06, 47D03]
specializes: [EVF180QJXY]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
---

## Summary

A contraction semigroup is a [[strongly continuous semigroup|EVF180QJXY]] $(T(t))_{t \ge 0}$ of operators on a Banach space with $\norm{T(t)} \le 1$ for every $t \ge 0$.
It describes a linear evolution that never increases the norm of the state.
The [[Lumer–Phillips theorem|Z2N8MPD8DH]] says that its generators are exactly the densely defined m-dissipative operators.
Heat flows, diffusions and unitary groups restricted to $t \ge 0$ give contraction semigroups.

## Explanations

### L1 human

A semigroup moves a state forward in time: $T(t)x$ is the state at time $t$ when the start is $x$.
For a contraction semigroup, the size of the state can only shrink or stay the same.
The heat semigroup is an example: the total squared temperature of a rod with ends kept at zero goes down with time.
On the real line, $T(t)x = e^{-t}x$ is a contraction semigroup, while $T(t)x = e^{t}x$ is not.
Every strongly continuous semigroup with $\norm{T(t)} \le M e^{\omega t}$ becomes a contraction semigroup after rescaling and a change of norm, which is why contractions are a central case.
