---
tag: F3STQVV22B
kind: definition
name: Intermittency
msc: [37G35, 37D45]
defines: W2FNJ4KBYT
uses: [D9TW46P19Y, 0AA97XA70K, MAP5J6HK0T, F5H8GW1XYS, NQDTTZ59X8, QN9X9BNKTX]
sources:
  - url: https://en.wikipedia.org/wiki/Intermittency
---

## Definition

Let $(\phi_\mu)$ be a one-parameter family of dynamical systems, flows or maps, with $\mu \in \R$.
Assume that for $\mu$ on one side of $\mu_0$ the system has a stable [[periodic orbit|0AA97XA70K]], and that it disappears or loses stability at $\mu_0$.
The system shows *intermittency* for $\mu$ just past $\mu_0$ if typical orbits alternate between two kinds of phases.

1. Laminar phases: long stretches of time during which the orbit stays close to the former periodic orbit.
2. Bursts: short irregular stretches, after which the orbit is reinjected near the former periodic orbit.

The *type* is I when the bifurcation at $\mu_0$ is a [[saddle-node bifurcation|MAP5J6HK0T]].
It is II for a subcritical [[Hopf|F5H8GW1XYS]] or Neimark–Sacker bifurcation, and III for a subcritical [[period-doubling bifurcation|NQDTTZ59X8]].

## Remarks

Example: the [[logistic map|QN9X9BNKTX]] $x \mapsto r x (1 - x)$ near $r_c = 1 + 2\sqrt{2}$.
At $r_c$ a stable and an unstable orbit of period $3$ are born in a saddle-node bifurcation of the third iterate.
For $r$ slightly below $r_c$, orbits pass slowly through the narrow gaps left between the graph of $f^3$ and the diagonal, so they look nearly periodic of period $3$.
Between these passages they move chaotically: this is type I intermittency.
For type I the mean length of the laminar phases grows like $(r_c - r)^{-1/2}$.
Non-example: just after a supercritical period-doubling bifurcation the new stable orbit of double period attracts nearby orbits, so there are no bursts.
Intermittency is a route to chaos studied in [[bifurcation theory|D9TW46P19Y]].
