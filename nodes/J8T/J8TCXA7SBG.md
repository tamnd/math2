---
tag: J8TCXA7SBG
kind: definition
name: Nichols plot
msc: [93C80, 93C05]
defines: V4178DP7FD
uses: [BMY8QZSD9H, 86JKV3TRFD, 070PFSYJJR, 04DXAFN2ES, Z7SPHAWMDX]
sources:
  - url: https://en.wikipedia.org/wiki/Nichols_plot
---

## Definition

Let $G$ be the [[transfer function|86JKV3TRFD]] of a single-input single-output linear time-invariant system.
Assume that its [[frequency response|BMY8QZSD9H]] $\omega \mapsto G(i\omega)$ is defined and nonzero for $\omega > 0$.
Let $\varphi(\omega)$ be a continuous choice of the [[argument|070PFSYJJR]] of $G(i\omega)$, in degrees.
The *Nichols plot* of $G$ is the following curve in the plane:
$$\omega \mapsto \bigl(\varphi(\omega),\ 20 \log_{10} \abs{G(i\omega)}\bigr), \qquad \omega > 0.$$
So the phase is on the horizontal axis and the gain in decibels on the vertical axis.

## Remarks

Replacing $G$ by $kG$ with a constant $k > 0$ shifts the Nichols plot vertically by $20 \log_{10} k$ decibels.
The plot is often drawn on a Nichols chart, whose curves show the gain and phase of the closed-loop function $G/(1 + G)$.

Example: for $G(s) = 1/(s + 1)$ the curve is $\omega \mapsto (-\arctan \omega \text{ (in degrees)},\ -10 \log_{10}(1 + \omega^2))$.
At $\omega = 1$ it passes through the point $(-45, -10 \log_{10} 2)$, about $(-45, -3)$.

Non-example: the [[Nyquist plot|Z7SPHAWMDX]] of $G$ also shows gain and phase together, but in polar form, with the gain on a linear scale; it is not a Nichols plot.
