---
tag: EA6CAV8ZSH
kind: definition
name: Green–Lagrange strain tensor
msc: [74A05]
defines: MRANPXATRD
uses: [HTYRR2WDQ6, N5G8WNQFC3, 8QS6QMJF5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
    locator: Finite strain tensors
---

## Definition

Let $\varphi \colon B \to \R^3$ be a deformation of an open set $B \subseteq \R^3$, with [[deformation gradient|HTYRR2WDQ6]] $F$ and [[right Cauchy–Green tensor|N5G8WNQFC3]] $C = F^T F$.
The *Green–Lagrange strain tensor* is the field
$$E = \tfrac12 (C - I) = \tfrac12 (F^T F - I),$$
where $I$ is the $3 \times 3$ identity matrix.

## Remarks

With the displacement $u(X) = \varphi(X) - X$, so that $F = I + \nabla u$, one has
$$E = \tfrac12 \left( \nabla u + (\nabla u)^T + (\nabla u)^T \nabla u \right).$$
Dropping the quadratic term gives the infinitesimal [[strain tensor|8QS6QMJF5Z]] $\varepsilon = \tfrac12 (\nabla u + (\nabla u)^T)$.
For the simple shear with $F$ having rows $(1, \gamma, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, the tensor $E$ has rows $(0, \gamma/2, 0)$, $(\gamma/2, \gamma^2/2, 0)$, $(0, 0, 0)$.
For a rotation by the angle $\theta$ about the third axis, $E = 0$.
But $\varepsilon$ has diagonal entries $\cos\theta - 1$, $\cos\theta - 1$, $0$, which is nonzero for $\theta \notin 2\pi\Z$.
So the small-strain tensor fails to vanish for large rotations.
The tensor $E$ is also called the Green–St. Venant or Lagrangian finite strain tensor.

## Explanations

### L1 human

The Green–Lagrange tensor is the standard strain measure for large deformations.
It compares squared lengths after and before the deformation, so pure rotations give no strain.
