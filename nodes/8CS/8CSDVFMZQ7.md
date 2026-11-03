---
tag: 8CSDVFMZQ7
kind: definition
name: Magnetic reconnection
msc: [76W05, 76X05, 85A30]
defines: YZM2H540TM
uses: [T8JWCBK9M6, ZSA13P8P81]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_reconnection
---

## Definition

Let $\mathbf{u}$ and $\mathbf{B}$ be the velocity and magnetic field of a solution of the equations of [[magnetohydrodynamics|T8JWCBK9M6]] on a region of $\R^3$.
Two fluid particles are *magnetically connected* at time $t$ if they lie on the same field line of $\mathbf{B}(\cdot, t)$.
*Magnetic reconnection* is a process in which this connectivity changes.
That is, some two fluid particles are magnetically connected at one time.
The flow $\mathbf{u}$ carries them to positions that are not magnetically connected at a later time.

## Remarks

In [[ideal MHD|ZSA13P8P81]] reconnection is impossible, because field lines move with the fluid; this is [[Alfvén's frozen-in flux theorem|3C3BXAPJQA]].
So reconnection needs a non-ideal term, such as the resistive term $\eta \Delta \mathbf{B}$ of the induction equation with $\eta > 0$, acting in a thin diffusion region.
Example: the planar field $\mathbf{B} = (B_0 / L)(y, x, 0)$ has field lines along the hyperbolas $x^2 - y^2 = \text{const}$ and an X-point at the origin.
A flow that carries field lines into the X-point along one diagonal and out along the other, with resistive diffusion at the X-point, reconnects them.
Non-example: take a uniform field $B_0 \mathbf{e}_z$ and a flow independent of $z$ with no $z$-component.
Then every field line stays a straight vertical line moving with the fluid, so connectivity never changes.
The Sweet–Parker model predicts a reconnection inflow speed of order $v_A S^{-1/2}$, where $v_A$ is the Alfvén speed and $S = L v_A / \eta$ the Lundquist number.
Since $S$ is huge in the solar corona, this rate is too slow to explain flares, which motivated the study of fast reconnection.
