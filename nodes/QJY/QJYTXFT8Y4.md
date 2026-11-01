---
tag: QJYTXFT8Y4
kind: concept
name: Bounded mean oscillation
msc: [30H35, 42B35]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
same_as:
  wikidata: Q796341
  wikipedia: Bounded mean oscillation
---

## Summary

A locally integrable function has bounded mean oscillation if its average deviation from its own mean, over every cube, is bounded by one constant.
The space BMO of such functions contains $L^\infty$ and also some unbounded functions such as $\log \abs{x}$.
It is the dual of the real Hardy space $H^1$, by Fefferman's theorem.
It is the natural replacement for $L^\infty$ in the theory of singular integrals.

## Explanations

### L1 human

Take any cube, compute the average of $f$ on it, and measure how far $f$ is from that average on the cube, on average.
If this number stays below a fixed bound for all cubes, large and small, then $f$ is in BMO.
A bounded function is always in BMO, because it can never be far from its averages.
The function $\log \abs{x}$ is unbounded, but rescaling only adds a constant to it, so its oscillation looks the same at every scale and stays bounded.
The function $f(x) = x$ on $\R$ is not in BMO: on $[0, L]$ its mean deviation is $L/4$, which grows without bound.
