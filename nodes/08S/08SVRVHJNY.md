---
tag: 08SVRVHJNY
kind: definition
name: Topological embedding
msc: [54C25]
defines: 00ZG9Y9TR4
uses: [05GZ11PWRY, 0D5YHQGDJY, 0PVG1CRAJN, 0Q3F20XB0A]
sources:
  - url: https://en.wikipedia.org/wiki/Embedding
    locator: General topology
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CNQXVBHCX]].
A function $f \colon X \to Y$ is a topological embedding when $f$ is [[injective|0PVG1CRAJN]] and the map $X \to f(X)$, $x \mapsto f(x)$, is a [[homeomorphism|05GZ11PWRY]].
Here the [[image|0Q3F20XB0A]] $f(X)$ has the [[subspace topology|0D5YHQGDJY]] of $Y$.

## Remarks

Each embedding is continuous, because the [[inclusion of a subspace is continuous|065J822CKN]].
The inclusion of a subspace is an embedding. The map $\mathbb{R} \to \mathbb{R}^2$, $x \mapsto (x, 0)$, is an embedding.
The map $t \mapsto (\cos t, \sin t)$ from $[0, 2\pi)$ to $\mathbb{R}^2$ is continuous and injective, but not an embedding.
A continuous injective map from a [[compact space|0QPHW703PV]] to a [[Hausdorff space|0MXB4CKHFW]] is an embedding.

## Explanations

### L1 human

An embedding puts a copy of $X$ inside $Y$ without changing its shape.
An injective continuous map can still bring the ends of the space together in the limit. Then it is not an embedding.
