---
tag: TBBDP94GDN
kind: definition
name: Space form
msc: [53C20, 53C21]
defines: 1VM1AQT956
uses: [7CBT4SM83Y, 1X42JAA349, B4QR306D8G]
sources:
  - url: https://en.wikipedia.org/wiki/Space_form
---

## Definition

Let $n \ge 2$ and let $K$ be a real number.
A *space form* of curvature $K$ is a Riemannian manifold $(M, g)$ of dimension $n$ such that:

1. $M$ is connected.
2. $M$ is complete as a metric space for the [[Riemannian distance|B4QR306D8G]].
3. The [[sectional curvature|1X42JAA349]] of every 2-plane at every point of $M$ equals $K$.

## Remarks

Example: the flat torus $\R^2 / \Z^2$ with the metric induced from $\R^2$ is connected and compact, hence complete, and its sectional curvature is $0$ everywhere.
So it is a space form of curvature $0$.

Non-example: the open unit disc in $\R^2$ with the Euclidean metric is connected and flat, but the Cauchy sequence $(1 - 1/k, 0)$ has no limit in the disc.
It fails clause 2.

The simply connected space forms are the sphere of radius $1/\sqrt{K}$ for $K > 0$, Euclidean space $\R^n$ for $K = 0$, and hyperbolic space of curvature $K$ for $K < 0$.
Some authors call only these three models space forms.
