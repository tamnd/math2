---
tag: H0NDB85RCD
kind: concept
name: Conditioned Brownian motion
msc: [60J65, 60J45]
sources:
  - url: https://en.wikipedia.org/wiki/Doob%27s_h-transform
---

## Summary

A conditioned Brownian motion in a domain is the Doob h-transform of Brownian motion killed on leaving the domain, for a positive harmonic function $h$.
Take for $h$ the Poisson kernel or the Martin kernel with pole at a boundary point.
Then the process is Brownian motion conditioned to leave the domain at that point.
Conditioned Brownian motion gives probabilistic proofs of boundary limit theorems, such as Fatou-type theorems and the relative Fatou theorem.

## Explanations

### L1 human

Run a Brownian particle inside a region, but only keep the runs that leave the region at one chosen boundary point.
The resulting random motion is drawn towards that point and eventually exits there.
A standard example is Brownian motion on the half-line conditioned never to reach $0$: it is pushed away from $0$ and drifts off to infinity.
