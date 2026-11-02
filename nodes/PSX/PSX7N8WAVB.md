---
tag: PSX7N8WAVB
kind: definition
name: Riemannian distance
msc: [53C20, 53B20]
defines: B4QR306D8G
uses: [7CBT4SM83Y, Q61VFHCH2J, 0TH78S7GBZ, 0QF1MZ9FRG, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Riemannian_manifold
---

## Definition

Let $(M, g)$ be a connected [[Riemannian manifold|7CBT4SM83Y]] with [[Riemannian metric|Q61VFHCH2J]] $g$.
For a piecewise smooth curve $\gamma \colon [a, b] \to M$, its [[length|0TH78S7GBZ]] is
$$L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}(\gamma'(t), \gamma'(t))} \, dt.$$
The *Riemannian distance* between points $p, q \in M$ is the [[infimum|0QF1MZ9FRG]]
$$d_g(p, q) = \inf \set{ L(\gamma) : \gamma \text{ is a piecewise smooth curve from } p \text{ to } q }.$$

## Remarks

Example: on $\R^n$ with the Euclidean metric $g = \sum_i dx_i^2$, the straight segment from $p$ to $q$ has length $\abs{q - p}$, and no curve is shorter, so $d_g(p, q) = \abs{q - p}$.

Non-example: if $M$ is not connected, two points in different components are joined by no curve.
Then the infimum is over the empty set, and $d_g$ is not a finite distance.
Some authors then set $d_g(p, q) = \infty$.

The function $d_g$ is a [[metric|0VKD1TP7F3]] on $M$, and the topology it induces is the given topology of $M$.
Positivity $d_g(p, q) > 0$ for $p \ne q$ is the nontrivial part; it follows by comparing $g$ with a Euclidean metric in a chart.
The infimum need not be attained: in $\R^2 \setminus \set{0}$ with the Euclidean metric, $d_g((-1, 0), (1, 0)) = 2$, but every curve between these points avoiding $0$ is longer than $2$.
