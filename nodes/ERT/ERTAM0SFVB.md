---
tag: ERTAM0SFVB
kind: concept
name: Normal function
msc: ["03E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_function
same_as:
  wikidata: Q7051810
  wikipedia: Normal function
---

## Summary

A normal function is a function from [[ordinals|0YSCSX5YZC]] to ordinals that is strictly increasing and continuous at limit ordinals.
The [[precise definition|PXTF18X433]] asks that the value at a limit be the supremum of the earlier values.
Each normal function has arbitrarily large fixed points, and this fixed-point lemma is the engine behind the [[Veblen function|JQFAE9S2F4]] and many ordinal notations.

## Explanations

### L1 human

A normal function climbs through the ordinals without jumps at limit points.
At a limit stage, its value is exactly the place that the earlier values were approaching.
For example, $\alpha \mapsto \omega + \alpha$ is normal: at $\omega$ its value is $\omega + \omega$, the limit of $\omega + 1, \omega + 2, \ldots$.
The function $\alpha \mapsto \alpha + 1$ is not normal, because at $\omega$ it jumps to $\omega + 1$ while the earlier values approach only $\omega$.
Because a normal function never skips a limit, it must eventually catch its own argument, and it has fixed points.
