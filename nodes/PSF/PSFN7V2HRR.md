---
tag: PSFN7V2HRR
kind: definition
name: Ehrenfest classification of phase transitions
msc: [82B26, 80A22, 80A10]
defines: 5XVRB6MTK4
uses: [6WJ0NADBT4, WVH4PVW64P, SPY89W0RJ7, SYYGZ18FF5]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_transition
---

## Definition

Let two phases $\alpha$ and $\beta$ of a pure substance meet along a curve in the $(T, p)$ plane.
Let $g(T, p)$ be the equilibrium molar Gibbs free energy, equal to the [[chemical potential|WVH4PVW64P]] of the stable phase.
Let $n \ge 1$ be an integer.
The [[phase transition|6WJ0NADBT4]] across the curve is of *order $n$* in the sense of Ehrenfest if:

1. all partial derivatives of $g$ with respect to $T$ and $p$ of order less than $n$ are continuous across the curve, and
2. at least one partial derivative of $g$ of order $n$ has a finite jump across the curve.

## Remarks

Since $g$ is continuous at any transition, order $1$ means that $s = -\partial g/\partial T$, the molar [[entropy|SPY89W0RJ7]], or $v = \partial g/\partial p$, the molar volume, jumps.
Boiling of water is first order: at $101.325\,\mathrm{kPa}$ the molar volume of steam is far larger than that of liquid water.
Order $2$ means that $s$ and $v$ are continuous but a second derivative jumps, such as the molar [[heat capacity|SYYGZ18FF5]] $c_p = -T\, \partial^2 g/\partial T^2$.
A non-example: at the lambda transition of liquid helium-4, $s$ and $v$ are continuous but $c_p$ diverges.
So no derivative of order $2$ has a finite jump, clause 2 fails for $n = 2$, and the transition has no Ehrenfest order.
For this reason the modern classification only separates first-order transitions, with latent heat, from continuous transitions.
