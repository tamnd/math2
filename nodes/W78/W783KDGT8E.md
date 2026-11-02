---
tag: W783KDGT8E
kind: concept
name: Dirichlet-to-Neumann operator
msc: [35J25, 35R30, 35S05]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Steklov_operator
---

## Summary

The Dirichlet-to-Neumann operator of a domain sends boundary values to normal derivatives.
Given a function $f$ on the boundary, it solves the [[Dirichlet problem|8D56GQ4AG8]] for [[Laplace's equation|S8RG6N1PRT]] with data $f$.
Then it returns the normal derivative of the solution on the boundary; conductivity equations work the same way.
It is a basic example of a [[pseudo-differential operator|FF27N0BWTP]] on the boundary.
It carries the boundary measurements of electrical impedance tomography, in the [[Calderón problem|R8Y8DDTWBM]], and its eigenvalues are the Steklov eigenvalues.

## Explanations

### L1 human

Fix the temperature, or the voltage, on the boundary of a body and let it settle to equilibrium inside.
Then measure how much heat, or current, flows out through each part of the boundary.
The Dirichlet-to-Neumann operator is the rule that turns the first list of numbers into the second.
On the unit disk, the boundary data $\cos(k\theta)$ extend to the harmonic function $r^k \cos(k\theta)$, whose radial derivative at $r = 1$ is $k \cos(k\theta)$.
So on the disk the operator multiplies the $k$-th Fourier mode by $\abs{k}$.
