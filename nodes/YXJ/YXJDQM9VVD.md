---
tag: YXJDQM9VVD
kind: definition
name: Limiting subdifferential
msc: [49J52, 49J53]
defines: W7WDXEQH65
uses: [0GSZ7B0CGR, 033RZ32T4Q, 0G9EKM0E15, 9C5WXYYQEK]
sources:
  - url: https://en.wikipedia.org/wiki/Subderivative
---

## Definition

Let $f \colon \R^n \to (-\infty, +\infty]$ be a function with values in the [[extended real line|0GSZ7B0CGR]], and let $\bar x \in \R^n$ with $f(\bar x)$ finite.

1. A vector $v \in \R^n$ is a *regular subgradient* of $f$ at a point $x$ with $f(x)$ finite if
$$\liminf_{y \to x, \ y \ne x} \frac{f(y) - f(x) - \ip{v}{y - x}}{\abs{y - x}} \ge 0,$$
where $\liminf$ is the [[limit inferior|033RZ32T4Q]].
The set of these vectors is the *regular subdifferential* $\hat\partial f(x)$.
2. The *limiting subdifferential* $\partial f(\bar x)$ is the set of vectors $v \in \R^n$ for which there are [[sequences|0G9EKM0E15]] $x_k \to \bar x$ and $v_k \to v$ with $f(x_k) \to f(\bar x)$ and $v_k \in \hat\partial f(x_k)$ for all $k$.

## Remarks

Taking $x_k = \bar x$ and $v_k = v$ shows that $\hat\partial f(\bar x) \subseteq \partial f(\bar x)$.
If $f$ is differentiable near $\bar x$ with continuous gradient, then $\partial f(\bar x) = \set{\nabla f(\bar x)}$.
If $f$ is convex, both sets equal the [[subdifferential|9C5WXYYQEK]] of convex analysis.
If $\bar x$ is a local minimum of $f$, then $0 \in \hat\partial f(\bar x) \subseteq \partial f(\bar x)$.
Other names are the Mordukhovich subdifferential and the basic subdifferential.

Example: $f(x) = -\abs{x}$ on $\R$ and $\bar x = 0$.
For $x > 0$ the function is differentiable with derivative $-1$, so $\hat\partial f(x) = \set{-1}$; for $x < 0$, $\hat\partial f(x) = \set{1}$.
Hence $\set{-1, 1} \subseteq \partial f(0)$, and in fact $\partial f(0) = \set{-1, 1}$.

Non-example: the vector $v = 0$ for the same function.
It is not a regular subgradient at $0$, since $(f(y) - f(0) - 0)/\abs{y} = -1$ for all $y \ne 0$.
It is not a limit of regular subgradients at nearby points either, since these are all $\pm 1$.
So $0 \notin \partial f(0)$, although $0$ lies in the Clarke generalized gradient $[-1, 1]$.
