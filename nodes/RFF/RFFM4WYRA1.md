---
tag: RFFM4WYRA1
kind: definition
name: Objective stress rate
msc: [74A20, 74A10]
defines: ADN3TKD39T
uses: [KG2XWEMJ30, EZQ0E262QV, 0PBY4E9GQF, 0W02QESPJQ]
sources:
  - url: https://en.wikipedia.org/wiki/Objective_stress_rate
---

## Definition

Consider a motion of a body with velocity field $v$, and let $\sigma$ be its [[Cauchy stress tensor|KG2XWEMJ30]].
Let $\dot\sigma$ be the material time derivative of $\sigma$, and let $L = \nabla v$ be the velocity gradient.
Write $D = \tfrac12 (L + L^T)$ for the rate of deformation and $W = \tfrac12 (L - L^T)$ for the spin, a [[skew-symmetric|0PBY4E9GQF]] tensor.
A change of observer is a map $x^* = Q(t) x + c(t)$, where $c(t)$ is a vector.
Here $Q(t)$ is a rotation, that is an [[orthogonal matrix|0W02QESPJQ]] with determinant $1$.
Under a change of observer the stress transforms as $\sigma^* = Q \sigma Q^T$.
A stress rate is a tensor $\overset{\circ}{\sigma}$ built from $\sigma$, $\dot\sigma$ and the motion.
It is *objective* if, for every change of observer, it transforms in the same way as the stress:
$$\overset{\circ}{\sigma}{}^* = Q \, \overset{\circ}{\sigma} \, Q^T.$$

## Remarks

Example: the Jaumann rate $\overset{\nabla}{\sigma} = \dot\sigma - W \sigma + \sigma W$ is objective.
Under a change of observer, $\dot\sigma^* = Q \dot\sigma Q^T + \dot Q \sigma Q^T + Q \sigma \dot Q^T$ and $W^* = Q W Q^T + \dot Q Q^T$.
Substituting, the terms with $\dot Q$ cancel, because $\dot Q Q^T$ is skew-symmetric.

Non-example: the material derivative $\dot\sigma$ itself is not objective.
The formula above shows that $\dot\sigma^*$ differs from $Q \dot\sigma Q^T$ by $\dot Q \sigma Q^T + Q \sigma \dot Q^T$, which is not zero in general when $Q$ depends on time.
For instance, with $Q(t)$ a rotation about $e_3$ at constant angular speed and $\sigma = e_1 \otimes e_1$, this extra term is nonzero.

Other standard objective rates are the Truesdell rate $\dot\sigma - L \sigma - \sigma L^T + (\tr L) \sigma$ and the upper convected (Oldroyd) rate $\dot\sigma - L \sigma - \sigma L^T$.
The Green–Naghdi rate has the form of the Jaumann rate with $\dot R R^T$ in place of $W$.
Here $R$ is the rotation in the polar decomposition of the deformation gradient.
