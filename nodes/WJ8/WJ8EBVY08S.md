---
tag: WJ8EBVY08S
kind: definition
name: J-integral
msc: [74R10, 74R20, 74A45]
defines: BZ2WFST50T
uses: [3E9K1DRNYN, KG2XWEMJ30, ZHK2EVRD90]
sources:
  - url: https://en.wikipedia.org/wiki/J-integral
---

## Definition

Let a two-dimensional body be made of a homogeneous [[hyperelastic material|ZHK2EVRD90]] with [[strain energy density|3E9K1DRNYN]] $W$.
Let it contain a straight crack along the negative $x_1$-axis with tip at the origin.
Let $u$ be the displacement field, $\sigma$ the [[stress|KG2XWEMJ30]], and assume there are no body forces and the crack faces are traction-free.
Let $\Gamma$ be a piecewise smooth curve from the lower crack face to the upper crack face, going counterclockwise around the tip.
Let $n$ be its outer unit normal and $s$ its arc length.
The *J-integral* along $\Gamma$ is
$$J = \int_{\Gamma} \left( W n_1 - \sigma_{ij} n_j \frac{\partial u_i}{\partial x_1} \right) ds,$$
with summation over $i, j \in \set{1, 2}$.

## Remarks

Under these hypotheses $J$ does not depend on the choice of $\Gamma$.
This follows from the divergence theorem: the integrand is the flux of the first row of the [[Eshelby energy-momentum tensor|Q94SK7PRN9]], which is divergence-free.
Example: take a linear elastic isotropic body in mode I, and evaluate $J$ on a small circle around the tip with the leading crack-tip fields.
This gives $J = K_I^2 / E'$, which is the [[energy release rate|D2D6BRJA5X]].
Non-example: if the crack faces carry tractions, or the material varies with $x_1$, the integral depends on the contour.
Its value on a given contour is then not a J-integral in the sense above.
For elastic–plastic materials the integral is evaluated with the deformation theory of plasticity, which is formally a nonlinear elastic theory.
So path independence holds as long as there is no unloading.

## Explanations

### L1 human

The J-integral adds up energy density and work along a loop around a crack tip.
Its value is the same on every loop and measures the energy that goes into the crack tip.
