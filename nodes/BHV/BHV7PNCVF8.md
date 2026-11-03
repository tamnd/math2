---
tag: BHV7PNCVF8
kind: definition
name: Magnetization
msc: [78A30, 78A25]
defines: A2WZA4QA3V
uses: [SSAWJ3JF5Y, XRED3C547P, 0299VCW1TH, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetization
---

## Definition

Let a material occupy a region $\Omega \subseteq \R^3$.
The *magnetization* of the material is the [[vector field|0299VCW1TH]] $M \colon \Omega \to \R^3$ with the following property.
For every small volume element $dV$ around a point $x$ of $\Omega$, the [[magnetic dipole moment|SSAWJ3JF5Y]] of the material in that element is $M(x) \, dV$.
So the total magnetic dipole moment of the material in a measurable region $V \subseteq \Omega$ is
$$m(V) = \int_V M(x) \, dV.$$
The magnetization is measured in amperes per metre.

## Remarks

The magnetization is a macroscopic average.
$M(x)$ is the sum of the atomic dipole moments in a region around $x$, divided by the volume of that region.
The region is small at the scale of the body but large at the atomic scale.

The [[magnetic field|XRED3C547P]] of a magnetized body equals the field of two bound currents.
They are the current density $J_b = \nabla \times M$ in its interior and the surface current density $K_b = M \times n$ on its boundary, where $n$ is the outward unit normal.
Here $\nabla \times$ is the [[curl|0NF6GQNXMY]].
The magnetizing field is defined by $H = B / \mu_0 - M$, where $\mu_0 > 0$ is the vacuum permeability.

Example: a ball of radius $R$ with constant magnetization $M_0$ has $J_b = 0$, since the curl of a constant field is zero.
Its total dipole moment is $\frac{4}{3} \pi R^3 M_0$.
The field inside the ball is the constant field $B = \frac{2}{3} \mu_0 M_0$.

Non-example: a copper wire carrying a current produces a magnetic field, but its magnetization is $0$.
Its field comes from the free current of moving conduction electrons and not from aligned dipole moments of the material.
