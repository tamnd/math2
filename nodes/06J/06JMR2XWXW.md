---
tag: 06JMR2XWXW
kind: definition
name: Regular curve
msc: [53A04]
defines: 0V7090SSPC
uses: [0JF1XXGWB4, 0D98771SM0]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_curve
    locator: Definitions
---

## Definition

Let $I \subseteq \mathbb{R}$ be an interval, and let $\gamma \colon I \to \mathbb{R}^n$ be a $C^1$ [[parametrised curve|0JF1XXGWB4]].
The curve $\gamma$ is regular if its [[tangent vector|0D98771SM0]] $\gamma'(t)$ is not zero for each $t \in I$.

## Remarks

The circle $t \mapsto (\cos t, \sin t)$ and each line $t \mapsto p + t v$ with $v \ne 0$ are regular.
The curve $t \mapsto (t^2, t^3)$ is not regular, since its tangent vector is zero at $t = 0$.
The curve $t \mapsto (t^3, t^3)$ is not regular at $t = 0$, but its image is a straight line. So regularity is a property of the parametrisation, not of the image.
A regular curve has an [[arc length parametrisation|00R1JDDV5X]].

## Explanations

### L1 human

A regular curve never stops.
The moving point always has non-zero speed, so the curve has no corners or cusps caused by the point coming to rest.
