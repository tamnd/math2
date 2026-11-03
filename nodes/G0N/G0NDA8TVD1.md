---
tag: G0NDA8TVD1
kind: definition
name: Airy stress function
msc: [74B05, 74G05]
defines: 7ZGSJRYBGK
uses: [KG2XWEMJ30, AS7WQTM99W, 09EGC6F8PT, AS8A9F5SKE]
sources:
  - url: https://en.wikipedia.org/wiki/Stress_functions
---

## Definition

Let $\Omega \subseteq \R^2$ be an open set, and let $\sigma = (\sigma_{11}, \sigma_{12}, \sigma_{22})$ be a symmetric plane [[stress|KG2XWEMJ30]] field on $\Omega$, as in [[plane stress|AS7WQTM99W]] or plane strain.
A $C^2$ function $\varphi \colon \Omega \to \R$ is an *Airy stress function* for $\sigma$ if
$$\sigma_{11} = \frac{\partial^2 \varphi}{\partial x_2^2}, \qquad \sigma_{22} = \frac{\partial^2 \varphi}{\partial x_1^2}, \qquad \sigma_{12} = -\frac{\partial^2 \varphi}{\partial x_1 \partial x_2}$$
at every point of $\Omega$, with [[partial derivatives|09EGC6F8PT]] in the coordinates $x_1, x_2$.

## Remarks

If $\varphi$ is of class $C^3$, then $\partial_1 \sigma_{11} + \partial_2 \sigma_{12} = \partial_1 \partial_2^2 \varphi - \partial_2 \partial_1 \partial_2 \varphi = 0$, and likewise $\partial_1 \sigma_{12} + \partial_2 \sigma_{22} = 0$; so the equilibrium equations without body force hold.
Conversely, on a simply connected $\Omega$ every symmetric $C^1$ stress field with zero divergence has an Airy stress function, unique up to adding an affine function $a + b x_1 + c x_2$.
For a homogeneous isotropic linear elastic material, the compatibility condition becomes the [[biharmonic equation|AS8A9F5SKE]] $\Delta^2 \varphi = 0$.

Example: $\varphi = \tfrac{s}{2} x_2^2$ gives $\sigma_{11} = s$ and $\sigma_{12} = \sigma_{22} = 0$, uniform tension along $x_1$; it is biharmonic.

Non-example: the field $\sigma_{11} = x_1$, $\sigma_{12} = \sigma_{22} = 0$ has no Airy stress function, because $\partial_1 \sigma_{11} + \partial_2 \sigma_{12} = 1 \ne 0$, while every field given by the formulas above with $\varphi \in C^3$ is divergence-free.

In polar coordinates $(r, \theta)$ the formulas read $\sigma_{rr} = \frac{1}{r} \partial_r \varphi + \frac{1}{r^2} \partial_\theta^2 \varphi$, $\sigma_{\theta\theta} = \partial_r^2 \varphi$ and $\sigma_{r\theta} = -\partial_r \big( \frac{1}{r} \partial_\theta \varphi \big)$.
