---
tag: 4K7TJE5KM4
kind: definition
name: Fresnel integrals
msc: ["33B20"]
defines: D0TQ9F2ZDW
uses: [08WFZP6P89, 04TMP0XGMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Fresnel_integral
---

## Definition

The *Fresnel integrals* are the functions $S, C \colon \R \to \R$ given by the [[definite integrals|04TMP0XGMJ]]
$$S(x) = \int_0^x \sin(t^2)\, dt, \qquad C(x) = \int_0^x \cos(t^2)\, dt,$$
where $\sin$ and $\cos$ are the [[sine and cosine|08WFZP6P89]].

## Remarks

Example: $S$ and $C$ are odd, since the integrands are even, and $S(0) = C(0) = 0$.
The curve $t \mapsto (C(t), S(t))$ has velocity $(\cos t^2, \sin t^2)$ of length $1$, so $t$ is its arc length, and its direction angle $t^2$ gives curvature $2t$.
This curve is the Euler spiral.

Non-example: $x \mapsto \int_0^x \sin(t)^2\, dt = \frac{x}{2} - \frac{\sin 2x}{4}$ is not a Fresnel integral; the square must be inside the sine.

As $x \to \infty$, $S(x) \to \sqrt{\pi/8}$ and $C(x) \to \sqrt{\pi/8}$, as one sees by rotating the contour of the [[Gaussian integral|0DFT1GP1JP]].
Many references use the normalisation $\int_0^x \sin\left(\frac{\pi t^2}{2}\right) dt$ and $\int_0^x \cos\left(\frac{\pi t^2}{2}\right) dt$ instead; then both limits are $\frac12$.
