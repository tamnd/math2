---
tag: 01A8JGR4JM
kind: statement
role: proposition
name: cos pi = -1
msc: [33B10]
uses: [0C1VYVNV2N, 028XEQCE88, 03H7WZ4T3K]
sources:
  - url: https://en.wikipedia.org/wiki/Pi
    locator: Definition
---

## Statement

$$\cos \pi = -1, \qquad \sin \pi = 0.$$

## Remarks

By the [[definition of $\pi$|0C1VYVNV2N]], $\cos(\pi/2) = 0$. The [[Pythagorean identity|03H7WZ4T3K]] gives $\sin(\pi/2) = 1$, since $\sin > 0$ on $(0, 2]$.
The [[double angle formulas|028XEQCE88]] then give $\cos \pi = 2 \cos^2(\pi/2) - 1 = -1$ and $\sin \pi = 2 \sin(\pi/2) \cos(\pi/2) = 0$.
Together with $\sin \pi = 0$, it gives Euler's identity $e^{i \pi} = -1$ in complex form. Mathlib states the first claim as `Real.cos_pi`.

## Explanations

### L1 human

Half a turn around the unit circle takes the point $(1, 0)$ to the point $(-1, 0)$.
So $\cos \pi = -1$ and $\sin \pi = 0$.
