---
tag: 46MFCQQ9VW
kind: object
name: Sinogram
msc: [44A12, 92C55, 94A08]
uses: [VJNZJ352PC]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Description

Let $f$ be a function on $\R^2$ with [[Radon transform|VJNZJ352PC]] $R f$.
Parametrize directions by an angle, $\theta(\varphi) = (\cos\varphi, \sin\varphi)$.
The *sinogram* of $f$ is the function $(\varphi, s) \mapsto R f(\theta(\varphi), s)$ on $[0, \pi) \times \R$.
It is drawn as an image with the angle $\varphi$ on one axis and the offset $s$ on the other.
The range $[0, \pi)$ suffices, because $R f(-\theta, -s) = R f(\theta, s)$.

Check of the name: let $f$ be concentrated near a single point $p = (\abs{p}\cos\alpha, \abs{p}\sin\alpha)$, a narrow bump of total mass $1$.
A line $x \cdot \theta(\varphi) = s$ meets the bump only when $s$ is close to $p \cdot \theta(\varphi) = \abs{p} \cos(\varphi - \alpha)$.
So the sinogram is concentrated near the curve $s = \abs{p} \cos(\varphi - \alpha)$, a sinusoid in $\varphi$.

Second check: take the indicator of a disk of radius $a$ centered at $0$.
Its sinogram is $2\sqrt{a^2 - s^2}$ for $\abs{s} \le a$ and $0$ otherwise, independent of $\varphi$: a band of constant profile.

## Explanations

### L1 human

A CT scanner measures, for each angle of the X-ray source, a profile of absorption values along the detector.
Stacking these profiles row by row, one row per angle, gives an image called the sinogram.
Each small dense spot in the body traces a sine wave across this image, because its shadow moves back and forth on the detector as the source turns.
A whole body gives a superposition of many such sine waves, and reconstruction means turning the sinogram back into the picture of the body.
