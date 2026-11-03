---
tag: PDY3N747BF
kind: definition
name: Mori–Tanaka method
msc: [74Q15, "74E30", 74A60]
defines: F79NNVV0B1
uses: [VSBFY8EN2H, X2N1EA2JGT, SX32X1D537]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_medium_approximations
---

## Definition

Let a two-phase composite consist of a matrix and of aligned ellipsoidal inclusions of the same shape.
The matrix has [[elasticity tensor|SX32X1D537]] $C_0$ and volume fraction $f_0$.
The inclusions have elasticity tensor $C_1$ and volume fraction $f_1 = 1 - f_0$.
Let $S$ be the Eshelby tensor of this ellipsoid in the matrix $C_0$, given by the solution of [[Eshelby's inclusion problem|X2N1EA2JGT]].
Let $I$ be the identity on symmetric matrices.
The *dilute strain concentration tensor* is
$$A^{\mathrm{dil}} = \left[ I + S C_0^{-1} (C_1 - C_0) \right]^{-1}.$$
The *Mori–Tanaka strain concentration tensor* is
$$A^{\mathrm{MT}} = A^{\mathrm{dil}} \left[ f_0 I + f_1 A^{\mathrm{dil}} \right]^{-1},$$
and the *Mori–Tanaka estimate* of the effective elasticity tensor is
$$C^{\mathrm{MT}} = C_0 + f_1 (C_1 - C_0) A^{\mathrm{MT}}.$$

## Remarks

The formula expresses that the average strain in the inclusions equals $A^{\mathrm{dil}}$ applied to the average strain in the matrix.
Check of the limits: for $f_1 = 0$ one gets $C^{\mathrm{MT}} = C_0$, and for $f_1 = 1$ one gets $A^{\mathrm{MT}} = I$ and $C^{\mathrm{MT}} = C_1$.
Take spherical inclusions and isotropic phases, with bulk moduli $K_0, K_1$ and matrix shear modulus $G_0$.
Then the effective bulk modulus is
$$K^{\mathrm{MT}} = K_0 + \frac{f_1 (K_1 - K_0)}{1 + 3 f_0 (K_1 - K_0)/(3 K_0 + 4 G_0)}.$$
This is the [[Hashin–Shtrikman bound|FZGYFV69HK]] with the matrix as reference phase.
It is the lower bound when the matrix is the softer phase, and the upper bound when it is the stiffer one.
Non-example: the dilute estimate $C_0 + f_1 (C_1 - C_0) A^{\mathrm{dil}}$ ignores the interaction of the inclusions and does not give $C_1$ at $f_1 = 1$, so it is not the Mori–Tanaka estimate.

## Explanations

### L1 human

First solve the problem of one inclusion alone in the matrix.
Then pretend that every inclusion sees not the applied strain but the average strain of the matrix around it.
Averaging over both phases gives the Mori–Tanaka estimate of the stiffness.
