---
tag: EVF180QJXY
kind: concept
name: C0-semigroup
msc: [47D06, 34G10]
sources:
  - url: https://en.wikipedia.org/wiki/C0-semigroup
same_as:
  wikidata: Q846542
  wikipedia: C0-semigroup
---

## Summary

A $C_0$-semigroup, or strongly continuous semigroup, is a family $T(t)$, $t \ge 0$, of bounded linear operators on a [[Banach space|06GZ956657]] that behaves like $e^{tA}$.
It satisfies $T(0) = I$ and $T(t + s) = T(t) T(s)$, and $T(t) x \to x$ as $t \to 0$ for each vector $x$.
Its generator $A$ is in general an unbounded operator, and $u(t) = T(t) u_0$ solves $u' = A u$.
$C_0$-semigroups give the solutions of linear evolution equations such as the heat equation, transport equations and Markov processes.

## Explanations

### L1 human

Let $T(t)$ be the map that takes a state now to the state after time $t$.
Running for $s$ and then for $t$ is the same as running for $t + s$, which is the semigroup law.
For the transport equation $u_t = u_s$ on the line, $T(t)$ shifts a profile: $(T(t) f)(s) = f(s + t)$.
Strong continuity says that a short shift barely changes the profile, measured in the chosen norm.
For a matrix $A$, $T(t) = e^{tA}$ is the simplest example.
