---
tag: 2ZTQX5M0TK
kind: statement
role: theorem
name: Lyapunov's convexity theorem
msc: [28B05, 46G10]
uses: [PS28BSAJKJ, VG2P7R91Z7, SV96KN4WR9, 02AS45T3H9, 0R6EWFKRCF]
about: [PS28BSAJKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_measure
---

## Statement

Let $(X, \Sigma)$ be a measurable space and let $\mu_1, \dots, \mu_n$ be finite real [[signed measures|VG2P7R91Z7]] on $\Sigma$.
Assume that each $\mu_i$ is [[non-atomic|SV96KN4WR9]], that is, its total variation $\abs{\mu_i}$ has no atoms.
Let $\mu \colon \Sigma \to \R^n$ be the [[vector measure|PS28BSAJKJ]] $\mu(E) = (\mu_1(E), \dots, \mu_n(E))$.
Then the range $\set{\mu(E) : E \in \Sigma}$ is a [[compact|0R6EWFKRCF]] [[convex|02AS45T3H9]] subset of $\R^n$.

## Remarks

A short proof considers the set $K$ of measurable $g \colon X \to [0, 1]$, compact in the weak-$*$ topology of $L^\infty(\abs{\mu_1} + \dots + \abs{\mu_n})$.
The map $g \mapsto \int g \, d\mu$ is linear and continuous, so its image is compact and convex, and it contains the range of $\mu$.
For a point $v$ of the image, the preimage of $v$ in $K$ is compact and convex and has an extreme point by the Krein–Milman theorem.
Non-atomicity forces such an extreme point to be an indicator function $\mathbf{1}_E$, so $v = \mu(E)$.

Example: for $n = 1$ and Lebesgue measure on $[0, 1]$, the range is $[0, 1]$, because $\lambda([0, t]) = t$.

Without non-atomicity the result fails: the Dirac measure $\delta_0$ has range $\{0, 1\}$, which is not convex.
The result also fails in infinite dimensions.
The vector measure $E \mapsto \mathbf{1}_E$ from the Borel sets of $[0, 1]$ to $L^2[0, 1]$ is non-atomic, but $\frac12 \mathbf{1}_{[0,1]}$ lies between $0$ and $\mathbf{1}_{[0,1]}$ and is not an indicator function.

## Explanations

### L1 human

Suppose several quantities are spread over a space without any point carrying a lump.
Then every proportion of these quantities can be cut out exactly by one piece of the space.
For instance, a cake with chocolate and cream spread smoothly can be cut so that one piece has exactly a third of the chocolate and exactly half of the cream.

### L2 human

The theorem is the basis of fair division results, such as the existence of exact divisions of a cake among several players.
In control theory it gives the bang-bang principle: the set of states reachable with measurable controls is already reached with controls taking only extreme values.
In economics it shows that non-atomic economies have convex aggregate behaviour.
