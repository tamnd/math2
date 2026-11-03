---
tag: A2R41B1DXY
kind: definition
name: Weissenberg number
msc: [76A10, 76M55]
defines: Y42Z1WX41X
uses: [T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Weissenberg_number
---

## Definition

Consider a flow of a viscoelastic fluid with relaxation time $\lambda > 0$.
Let $\dot\gamma > 0$ be a characteristic rate of deformation of the flow.
For example, $\dot\gamma$ is the shear rate, or $U / \ell$ for a characteristic speed $U$ and length $\ell$.
The *Weissenberg number* is the dimensionless quantity
$$\mathrm{Wi} = \lambda \dot\gamma.$$

## Remarks

Example: for the [[upper-convected Maxwell model|VN6MY7KWJ8]] in steady simple shear with shear rate $\dot\gamma$, the shear stress is $\tau_{12} = \eta_0 \dot\gamma$ and the first normal stress difference is $N_1 = 2 \lambda \eta_0 \dot\gamma^2$.
So $N_1 / \tau_{12} = 2 \lambda \dot\gamma = 2 \, \mathrm{Wi}$: the ratio of elastic to viscous stress is measured by $\mathrm{Wi}$.

Non-example: the quantity $\lambda \dot\gamma^2$ is not the Weissenberg number; it has the unit of an inverse time, so it is not dimensionless.

The Weissenberg number is different from the Deborah number, which compares the relaxation time with the observation time of the process rather than with the inverse rate of deformation.
For a [[Newtonian fluid|T4ZV12BVHN]] one has $\lambda = 0$ and so $\mathrm{Wi} = 0$.
