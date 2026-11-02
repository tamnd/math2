---
tag: A4P47SGE4S
kind: definition
name: Prolongation of a section to a jet bundle
msc: [58A20]
defines: BMCCQ8JXNE
uses: [HC3VBBCJQP, 1QE0Z0756D, CX4M8K61AB, GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Jet_bundle
---

## Definition

Let $\pi \colon E \to M$ be a smooth [[fiber bundle|CX4M8K61AB]], let $k \ge 0$, and let $\pi_k \colon J^k\pi \to M$ be its $k$-th [[jet bundle|HC3VBBCJQP]].
Let $s \colon U \to E$ be a smooth local section of $\pi$ over an open set $U \subseteq M$.
The *$k$-th prolongation* of $s$ is the map
$$j^k s \colon U \to J^k\pi, \qquad p \mapsto j^k_p s,$$
where $j^k_p s$ is the [[$k$-jet|1QE0Z0756D]] of $s$ at $p$.
It is a smooth local section of $\pi_k$.

A local section $\sigma$ of $\pi_k$ is *holonomic* if $\sigma = j^k s$ for some local section $s$ of $\pi$.

## Remarks

In adapted coordinates $(x^i, u^\alpha, u^\alpha_I)$, if $s$ has components $s^\alpha(x)$, then
$$j^k s(x) = \Big(x^i,\ s^\alpha(x),\ \frac{\partial^{\abs{I}} s^\alpha}{\partial x^I}(x)\Big)_{1 \le \abs{I} \le k}.$$
If $\sigma = j^k s$, then $s = \pi_{k,0} \circ \sigma$, so $s$ is determined by $\sigma$.

Example: for $\pi \colon \R \times \R \to \R$ and $s(x) = x^2$, the first prolongation is $j^1 s(x) = (x, x^2, 2x)$.

Non-example: the section $\sigma(x) = (x, 0, 1)$ of $J^1\pi \to \R$ for the same bundle is not holonomic.
If $\sigma = j^1 s$, then $s = \pi_{1,0} \circ \sigma = 0$, so $j^1 s(x) = (x, 0, 0) \ne \sigma(x)$.

A [[partial differential equation|GC5BDZ6QBC]] of order $k$ for sections of $\pi$ can be given as a subset $\mathcal{R} \subseteq J^k\pi$.
A local section $s$ is a solution exactly when $j^k s$ takes its values in $\mathcal{R}$.
