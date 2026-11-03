---
tag: ZMJ5MWAYDJ
kind: definition
name: Cauchy–Green deformation tensor
msc: [74A05]
defines: N5G8WNQFC3
uses: [HTYRR2WDQ6, 09DXWYRD43, 0VR671PHE5, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
    locator: Deformation tensors
---

## Definition

Let $\varphi \colon B \to \R^3$ be a deformation of an open set $B \subseteq \R^3$, with [[deformation gradient|HTYRR2WDQ6]] $F = \nabla \varphi$.
Let $F^T$ be the [[transpose|09DXWYRD43]] of $F$.
The *right Cauchy–Green deformation tensor* is the field $C = F^T F$.
The *left Cauchy–Green deformation tensor* is the field $b = F F^T$.

## Remarks

Both $C(X)$ and $b(X)$ are [[symmetric|0VR671PHE5]] and [[positive definite|0KX66CZMBB]], because $F(X)$ is invertible: $v \cdot C v = \abs{F v}^2 > 0$ for $v \neq 0$.
For the simple shear $F$ with rows $(1, \gamma, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, the right tensor $C$ has rows $(1, \gamma, 0)$, $(\gamma, 1 + \gamma^2, 0)$, $(0, 0, 1)$; it differs from $I$, which detects the shear.
For a rotation $F = Q$ with $Q^T Q = I$, one gets $C = b = I$.
A symmetric matrix with a negative eigenvalue, such as $\operatorname{diag}(-1, 1, 1)$, is not the right Cauchy–Green tensor of any $F$, since $F^T F$ is always positive definite.
The tensors $C$ and $b$ have the same eigenvalues, the squares of the principal stretches.

## Explanations

### L1 human

The Cauchy–Green tensors measure how a deformation changes lengths, ignoring rotation.
The right tensor $C$ works with arrows in the undeformed body, the left tensor $b$ with arrows in the deformed body.
