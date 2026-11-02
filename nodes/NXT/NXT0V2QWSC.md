---
tag: NXT0V2QWSC
kind: definition
name: Gaussian measure
msc: [28C20, 60G15, 60B11]
defines: P0DV2TCH1N
uses: [059TJN0NZ1, 2Z2QVWZ262, 0ACRGYNHSR, 06GZ956657, 0Z2P41SVDP, 03TM135G0N, 3N66TM3TSQ, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_measure
---

## Definition

Let $\gamma$ be a Borel [[probability measure|059TJN0NZ1]] on $\R$.
It is *Gaussian* in two cases.
The first case is $\gamma = \delta_m$, the [[Dirac measure|0ACRGYNHSR]] at some $m \in \R$.
The second case is that there are $m \in \R$ and $\sigma > 0$ with
$$\gamma(A) = \frac{1}{\sqrt{2 \pi \sigma^2}} \int_A e^{-(x - m)^2 / (2 \sigma^2)} \, dx$$
for every Borel set $A \subseteq \R$, where $dx$ is [[Lebesgue measure|2Z2QVWZ262]].
Let $E$ be a real [[separable|0Z2P41SVDP]] [[Banach space|06GZ956657]].
A Borel probability measure $\gamma$ on $E$ is *Gaussian* if for every [[continuous linear form|03TM135G0N]] $\ell \colon E \to \R$ the [[pushforward|3N66TM3TSQ]] $\ell_* \gamma$ is a Gaussian measure on $\R$.
It is *centered* if every $\ell_* \gamma$ has mean $0$.

## Remarks

In the second case on $\R$, $\gamma$ is the [[normal distribution|05AQE0QR0D]] $N(m, \sigma^2)$; the Dirac case is the degenerate normal distribution $N(m, 0)$.
The *standard* Gaussian measure on $\R^n$ has density $(2\pi)^{-n/2} e^{-\abs{x}^2/2}$.
Some authors call $\gamma$ Gaussian only when every $\ell_* \gamma$ with $\ell \ne 0$ is non-degenerate.

Example: on $E = \R^2$, the standard Gaussian measure is Gaussian.
For $\ell(x) = a x_1 + b x_2$, the law $\ell_* \gamma$ is $N(0, a^2 + b^2)$, since a linear combination of independent standard normal variables is normal.

Non-example: the uniform probability measure on $[-1, 1]$ is not Gaussian.
Its pushforward under the identity is not a Dirac measure and has no Gaussian density, since it vanishes outside $[-1, 1]$.

Wiener measure on the Banach space of continuous functions $\omega$ on $[0, 1]$ with $\omega(0) = 0$ is a centered Gaussian measure.

## Explanations

### L1 human

A measure on a vector space is Gaussian when every linear view of it is a bell curve, possibly squeezed to a point.
This definition works in any dimension, including infinite dimension.
