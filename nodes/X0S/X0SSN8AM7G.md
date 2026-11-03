---
tag: X0SSN8AM7G
kind: statement
role: theorem
name: Polar decomposition of the deformation gradient
msc: [74A05, 15A23]
uses: [HTYRR2WDQ6, N5G8WNQFC3, 0J2C7BDJQA, 0W02QESPJQ, 0KX66CZMBB, 63FAKMYZ2E]
about: [HTYRR2WDQ6]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_decomposition
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
---

## Statement

Let $F$ be a real $3 \times 3$ matrix with $\det F > 0$, for example the [[deformation gradient|HTYRR2WDQ6]] of a deformation at a point.
A rotation is an [[orthogonal matrix|0W02QESPJQ]] $R$ with $\det R = 1$.
Then there are a unique rotation $R$ and unique symmetric [[positive definite matrices|0KX66CZMBB]] $U$ and $V$ with $F = R U = V R$.
Moreover $U = \sqrt{C}$ and $V = \sqrt{b}$, where $C = F^T F$ and $b = F F^T$ are the [[Cauchy–Green tensors|N5G8WNQFC3]] and $\sqrt{\cdot}$ is the positive definite [[square root|63FAKMYZ2E]].

## Remarks

Since $C = F^T F$ is symmetric positive definite, it has a unique positive definite square root $U$; then $R = F U^{-1}$ satisfies $R^T R = U^{-1} C U^{-1} = I$ and $\det R = \det F / \det U > 0$, so $R$ is a rotation.
Setting $V = R U R^T$ gives $F = V R$, and $V^2 = F F^T$ forces $V = \sqrt{b}$; uniqueness follows from uniqueness of positive square roots.
This is the real, invertible case of the general [[polar decomposition|0J2C7BDJQA]].
For example, $F$ with rows $(0, -1, 0)$, $(2, 0, 0)$, $(0, 0, 1)$ has $C = \operatorname{diag}(4, 1, 1)$, $U = \operatorname{diag}(2, 1, 1)$, and $R = F U^{-1}$ is the rotation by $90$ degrees about the third axis.
If $\det F < 0$, the same construction gives an orthogonal $R$ with $\det R = -1$, a reflection.
So the hypothesis $\det F > 0$ is what makes $R$ a rotation.
If $\det F = 0$, then $U$ is not invertible and $R$ is not unique.

## Explanations

### L1 human

Every local deformation is a pure stretch followed by a rotation, or a rotation followed by a pure stretch.
The stretch part $U$ or $V$ says how much material fibres are lengthened in three perpendicular directions.
The rotation part $R$ says how the material is turned.

### L2 human

The tensors $U$ and $V$ are the right and left stretch tensors; their common eigenvalues are the principal stretches.
By frame-indifference, the stored energy of a hyperelastic material depends on $F$ only through $U$, or equivalently through $C$.
The decomposition explains why $C = U^2$ is free of rotation and why strain measures are built from $C$.
