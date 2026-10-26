---
tag: ~ff8fcf9f
kind: definition
name: Arc length
msc: [26A42, 53A04]
defines: ~8ea782a1
uses: [~de6fd15c]
sources:
  - url: https://en.wikipedia.org/wiki/Arc_length
    locator: Definition
---

## Definition

Let $\gamma \colon [a, b] \to \mathbb{R}^n$ be continuous.
The arc length of $\gamma$ is
$$L(\gamma) = \sup_{P} \sum_{i=1}^{k} \| \gamma(t_i) - \gamma(t_{i-1}) \|,$$
where the supremum runs over all [[partitions|~de6fd15c]] $P = (t_0, \dots, t_k)$ of $[a, b]$.
The curve $\gamma$ is rectifiable if $L(\gamma) < \infty$.

## Remarks

Each sum is the length of a polygonal path through points of the curve. Adding points does not decrease this length.
If $\gamma$ is continuously differentiable, then $L(\gamma) = \int_a^b \| \gamma'(t) \| \, dt$.
For the graph of a $C^1$ function $f$ on $[a, b]$, this gives $L = \int_a^b \sqrt{1 + f'(x)^2} \, dx$.
Some continuous curves are not rectifiable, for example the graph of the [[Weierstrass function|~c4cfb464]].

## Explanations

### L1 human

The arc length of a curve is the length of a string laid along it.
We approximate the curve by straight segments and take the best approximation.
