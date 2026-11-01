---
tag: 0F1AVGX26N
kind: definition
name: Closed and exact forms
msc: [58A12]
defines: 0ZV14XRNF0
uses: [0QHTX7WQEY, 004FRCXH6M, 0MTENFBW3Q, 05R9NF2J49, 0GDNHS9J2X]
sources:
  - url: https://en.wikipedia.org/wiki/Exterior_derivative
    locator: Closed and exact forms
  - url: https://en.wikipedia.org/wiki/Closed_and_exact_differential_forms
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Closed_and_exact_differential_forms
    locator: Vector field analogies
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, and let $\omega$ be a [[differential k-form|0QHTX7WQEY]] on $U$ with $C^1$ coefficients, where $k \ge 1$.
The form $\omega$ is closed if $d\omega = 0$, where $d$ is the [[exterior derivative|004FRCXH6M]].
The form $\omega$ is exact if $\omega = d\eta$ for some $(k - 1)$-form $\eta$ on $U$.

## Remarks

Each exact form $d\eta$ with $\eta$ of class $C^2$ is closed, because [[d d = 0|0X308R2DBE]].
A [[one-form|0MTENFBW3Q]] $\sum_i f_i \, dx_i$ is closed if and only if $\partial_j f_i = \partial_i f_j$ for all $i, j$. It is exact if and only if $(f_1, \dots, f_n)$ is a [[conservative|05R9NF2J49]] field. In $\mathbb{R}^3$, closed means that the [[curl|0GDNHS9J2X]] is zero.
The angle form $d\theta = \frac{-y \, dx + x \, dy}{x^2 + y^2}$ on $\mathbb{R}^2 \setminus \{0\}$ is closed but not exact. Its integral around the unit circle is $2\pi$, not $0$.
On a convex open set, each closed form is exact. This is the [[Poincaré lemma|05MC3HND79]].

## Explanations

### L1 human

Exact forms are derivatives of other forms, and closed forms only pass the local test for this: their derivative is zero.
The gap between the two notions is a measure of the holes of the domain.
