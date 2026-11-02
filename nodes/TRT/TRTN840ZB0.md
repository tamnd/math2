---
tag: TRTN840ZB0
kind: concept
name: Ill-posedness of real Laplace inversion
msc: [44A10, 47A52, 65R30]
sources:
  - url: https://en.wikipedia.org/wiki/Well-posed_problem
---

## Summary

Recovering a function $f$ from the values of its [[Laplace transform|0V49JEZW06]] $F(s)$ at real points $s > 0$ is an ill-posed problem in the sense of Hadamard.
The solution is unique, but it does not depend continuously on the data.
Transforms that are very close can come from functions that are far apart.
So small errors in measured values of $F$ can produce large errors in the computed $f$, and numerical inversion needs regularisation.
The problem fails the stability condition in the definition of a [[well-posed problem|W09B9NZ9B5]].

## Explanations

### L1 human

The Laplace transform smooths a function a great deal: it averages $f$ against the slowly varying weights $e^{-s t}$.
Fast wiggles in $f$ almost cancel in these averages, so they leave nearly no trace in $F$.
For example, $e^{-t} \sin(n t)$ has size about $1/2$ for every $n$, but its transform $n/((s+1)^2 + n^2)$ shrinks to $0$ as $n$ grows.
So from a slightly noisy $F$ one cannot tell whether such wiggles are present, and inversion becomes unstable.
