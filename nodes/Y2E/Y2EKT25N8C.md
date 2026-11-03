---
tag: Y2EKT25N8C
kind: definition
name: Upper-convected time derivative
msc: [76A10, 76A05]
defines: F16YFCJRFJ
uses: [CJW50K5HZB, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Upper-convected_time_derivative
---

## Definition

Let $u$ be a smooth [[vector field|0299VCW1TH]] on an open set of $\R^3$ depending on time $t$, the velocity of a flow.
Let $L = \nabla u$ be the velocity gradient, the matrix with entries $L_{ij} = \partial u_i / \partial x_j$.
Let $A$ be a smooth field of $3 \times 3$ matrices (a second-order tensor field) depending on position and time.
The *upper-convected time derivative* of $A$ is
$$\overset{\nabla}{A} = \frac{DA}{Dt} - L A - A L^T,$$
where $\dfrac{DA}{Dt} = \dfrac{\partial A}{\partial t} + (u \cdot \nabla) A$ is the [[material derivative|CJW50K5HZB]], taken entry by entry.

## Remarks

Example: for a uniform flow $u = (U, 0, 0)$ with constant $U$, one has $L = 0$, so $\overset{\nabla}{A} = DA/Dt$.

Example with deformation: in the simple shear $u = (\dot\gamma y, 0, 0)$, the only nonzero entry of $L$ is $L_{12} = \dot\gamma$.
For a constant symmetric tensor $A$ one gets $\overset{\nabla}{A} = -LA - AL^T$, whose $(1,1)$ entry is $-2 \dot\gamma A_{12}$.
So a constant tensor with $A_{12} \ne 0$ has nonzero upper-convected derivative, even though its material derivative is $0$.

Non-example: the material derivative alone is not frame-invariant, so it is not the upper-convected derivative; the two differ by $-LA - AL^T$, which is nonzero in the shear example.

If $F$ is the deformation gradient of the flow, then $\overset{\nabla}{A} = F \, \dfrac{D}{Dt}\big(F^{-1} A F^{-T}\big) F^T$, which explains the name: $A$ is differentiated after being pulled back to the reference configuration.
