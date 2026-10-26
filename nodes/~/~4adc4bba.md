---
tag: ~4adc4bba
kind: definition
name: Line integral of a scalar field
msc: [26B12]
defines: ~334a61fa
uses: [~2abc903b, ~b0eec11e, ~8e762cda]
sources:
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Line integral of a scalar field
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Derivation
---

## Definition

Let $\gamma \colon [a, b] \to \mathbb{R}^n$ be a [[rectifiable curve|~b0eec11e]] with image $C$, and let $f \colon C \to \mathbb{R}$ be [[continuous|~8e762cda]].
For a partition $a = t_0 < t_1 < \dots < t_k = b$ and points $\tau_i \in [t_{i-1}, t_i]$, let $\Delta s_i$ be the length of the restriction of $\gamma$ to $[t_{i-1}, t_i]$.
The line integral of $f$ along $\gamma$ is the limit
$$\int_\gamma f \, ds = \lim \sum_{i=1}^{k} f(\gamma(\tau_i)) \, \Delta s_i,$$
taken as $\max_i (t_i - t_{i-1}) \to 0$.

## Remarks

The limit exists, and it does not depend on the choice of the points $\tau_i$.
For a $C^1$ curve, $\int_\gamma f \, ds = \int_a^b f(\gamma(t)) \, \|\gamma'(t)\| \, dt$. This is the [[parametric formula|~469b0136]].
For $f = 1$ the line integral is the length of $\gamma$. If $\gamma$ is a wire with linear density $f$, the line integral is its mass.
The value does not change under a reparametrisation of $\gamma$, in either direction.

## Explanations

### L1 human

Walk along the curve, and at each small step multiply the length of the step by the value of $f$ there.
The sum of these products, in the limit of small steps, is the line integral with respect to arc length.
