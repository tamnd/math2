---
tag: ED0SZS1VED
kind: concept
name: Barrier
msc: [31B20, 31B25, 35J25]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Summary

A barrier at a boundary point $\xi$ of a bounded open set is a [[superharmonic function|X4V2S56YQQ]] that vanishes at $\xi$.
It is positive at every other point of the closure.
Barriers are the local test for whether the [[Perron method|AEZ7PPCNQS]] gives the right boundary value at $\xi$.
A boundary point is regular for the [[Dirichlet problem|8D56GQ4AG8]] if and only if it has a barrier.
Simple geometric conditions, such as an exterior ball or an exterior cone at $\xi$, produce explicit barriers.

## Explanations

### L1 human

A barrier is a superharmonic function that dips down to zero exactly at the chosen boundary point.
It acts like a funnel that forces the Perron solution to approach the boundary value at that point.
In $\R^3$, suppose a closed ball with centre $y$ and radius $R$ meets the closure of the set only at $\xi$.
Then the function $\frac{1}{R} - \frac{1}{\abs{x - y}}$ is a barrier at $\xi$.
