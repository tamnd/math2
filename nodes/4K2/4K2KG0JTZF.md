---
tag: 4K2KG0JTZF
kind: proof
name: Proof that isometries are injective
msc: ["54E40"]
proves: 02J4G4J4TJ
uses: [063W5JMY85, 0878DN3WCS, 0PVG1CRAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Definition
---

## Proof

1. Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$ be an [[isometry|0878DN3WCS]].
2. Let $x, y \in X$ with $f(x) = f(y)$.
3. A metric is $0$ on equal points, so $d_Y(f(x), f(y)) = 0$.
4. Since $f$ is an isometry, $d_X(x, y) = d_Y(f(x), f(y)) = 0$.
5. By the axiom of a metric, $x \ne y$ would give $d_X(x, y) > 0$. This contradicts step 4, so $x = y$.
6. Thus $f(x) = f(y)$ implies $x = y$, and $f$ is [[injective|0PVG1CRAJN]].

## Idea

Distinct points have positive distance, and an isometry keeps distances.
So the images of distinct points also have positive distance, and they are distinct.
