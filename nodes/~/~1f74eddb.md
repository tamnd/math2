---
tag: ~1f74eddb
kind: definition
name: Topological embedding
aliases: [embedding]
msc: [54C25]
defines: ~113e1385
uses: [~0e10d672, ~74712f5b, 0PVG1CRAJN, 0Q3F20XB0A]
sources:
  - url: https://en.wikipedia.org/wiki/Embedding
    locator: General topology
---

## Definition

Let $X$ and $Y$ be [[topological spaces|~77bfcc55]].
A function $f \colon X \to Y$ is a topological embedding when $f$ is [[injective|0PVG1CRAJN]] and the map $X \to f(X)$, $x \mapsto f(x)$, is a [[homeomorphism|~0e10d672]].
Here the [[image|0Q3F20XB0A]] $f(X)$ has the [[subspace topology|~74712f5b]] of $Y$.

## Remarks

Each embedding is continuous, because the [[inclusion of a subspace is continuous|~79793fa7]].
The inclusion of a subspace is an embedding. The map $\mathbb{R} \to \mathbb{R}^2$, $x \mapsto (x, 0)$, is an embedding.
The map $t \mapsto (\cos t, \sin t)$ from $[0, 2\pi)$ to $\mathbb{R}^2$ is continuous and injective, but not an embedding.
A continuous injective map from a [[compact space|~68153d33]] to a [[Hausdorff space|~a1fe0c25]] is an embedding.

## Explanations

### L1 human

An embedding puts a copy of $X$ inside $Y$ without changing its shape.
An injective continuous map can still bring the ends of the space together in the limit. Then it is not an embedding.
