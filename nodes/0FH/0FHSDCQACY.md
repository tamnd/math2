---
tag: 0FHSDCQACY
kind: statement
role: proposition
name: Epsilon-delta uniform continuity
msc: ["54E40"]
uses: [063W5JMY85, 06JYPJ4WHH]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Definition of uniform continuity
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Other characterizations
---

## Statement

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$ be a function.
Then the following two conditions are equivalent:

1. For each real $\varepsilon > 0$ there is a real $\delta > 0$ such that $d_Y(f(x), f(y)) < \varepsilon$ for all $x, y \in X$ with $d_X(x, y) < \delta$.
2. For all sequences $(x_n)$ and $(y_n)$ in $X$ with $d_X(x_n, y_n) \to 0$, also $d_Y(f(x_n), f(y_n)) \to 0$.

The map $f$ is uniformly continuous when it satisfies these conditions.

## Remarks

Condition 1 is the epsilon-delta definition of uniform continuity. Here $\delta$ depends only on $\varepsilon$, not on the points.
Each uniformly continuous map is continuous. The converse fails: $x \mapsto x^2$ on $\mathbb{R}$ is continuous but not uniformly continuous. Take $x_n = n + 1/n$ and $y_n = n$; then $x_n^2 - y_n^2 > 2$.
On a compact space, each continuous map to a metric space is uniformly continuous: this is the [[Heine–Cantor theorem|06B8BNJCD6]].
Each [[Lipschitz map|0TMZ21WKCN]] is uniformly continuous.

## Explanations

### L1 human

For a uniformly continuous map, one input tolerance $\delta$ works in the whole space.
The map $x \mapsto x^2$ gets steeper and steeper, so near large $x$ you need a smaller and smaller $\delta$, and no single $\delta$ works.
