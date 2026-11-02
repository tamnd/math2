---
tag: A2MX36J5GD
kind: definition
name: Crisis
msc: [37G35, 37D45]
defines: N087STXZKG
uses: [D9TW46P19Y, 7FWX24X5MW, 9WKCZGG906, 0AA97XA70K, QN9X9BNKTX, NQDTTZ59X8]
sources:
  - url: https://en.wikipedia.org/wiki/Crisis_(dynamical_systems)
---

## Definition

Let $(\phi_\mu)$ be a one-parameter family of dynamical systems, flows or maps, with $\mu \in \R$.
Assume that for $\mu$ near $\mu_0$ the system has a chaotic [[attractor|7FWX24X5MW]] $A_\mu$.
A *crisis* at $\mu_0$ is a bifurcation at which $A_\mu$ changes discontinuously as $\mu$ crosses $\mu_0$.
The attractor is suddenly destroyed or suddenly jumps in size.
At a crisis, $A_{\mu_0}$ touches an unstable [[periodic orbit|0AA97XA70K]] or its stable manifold.
The crisis is a *boundary crisis* if this orbit lies on the boundary of the basin of $A_\mu$.
It is an *interior crisis* if this orbit lies inside the basin.

## Remarks

Example: the [[logistic map|QN9X9BNKTX]] $f_r(x) = r x (1 - x)$ at $r = 4$.
For $r = 4$, the interval $[0, 1]$ is invariant and carries a chaotic attractor.
The attractor contains the repelling fixed point $0$ and its preimage $1$, which lie on the boundary of the basin.
For $r > 4$, points near $1/2$ are mapped above $1$ and then escape to $-\infty$, so the attractor is destroyed: a boundary crisis.
After the crisis, typical orbits stay near the old attractor for a long time before escaping, a chaotic transient.
Non-example: a [[period-doubling bifurcation|NQDTTZ59X8]] of a periodic attractor is not a crisis, since the attractor changes continuously and is not chaotic.
Crises are a basic route by which [[strange attractors|9WKCZGG906]] appear or vanish in [[bifurcation theory|D9TW46P19Y]].
