---
tag: ZN7HJNR2AC
kind: concept
name: Doob's h-transform
msc: [60J45, 60J25]
sources:
  - url: https://en.wikipedia.org/wiki/Doob%27s_h-transform
same_as:
  wikidata: Q140753206
  wikipedia: Doob's h-transform
---

## Summary

Doob's h-transform changes the transition probabilities of a Markov process by weighting them with a positive excessive function $h$.
The new process, the h-process, behaves like the old one conditioned on an event described by $h$.
Typical events are leaving a domain at a given boundary point or never being killed.
It links positive harmonic functions, the Martin boundary, and conditioned processes.

## Explanations

### L1 human

Take a random motion and a positive function $h$ that never increases on average along the motion.
Tilt the motion so that moves towards places where $h$ is large become more likely, in proportion to $h$.
The tilted motion is the h-transform.
For example, Brownian motion on the half-line $x > 0$, tilted by $h(x) = x$, becomes Brownian motion conditioned never to hit $0$.
