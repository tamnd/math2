---
tag: ZCHHTZ1FHS
kind: definition
name: Infinitesimal strain theory
msc: [74A05, 74B05]
defines: X121AYEY67
uses: [E51Y1CMF1Q, 8QS6QMJF5Z, MRANPXATRD]
sources:
  - url: https://en.wikipedia.org/wiki/Infinitesimal_strain_theory
---

## Definition

Let $u \colon B \to \R^3$ be the displacement of a [[deformation|E51Y1CMF1Q]] of an open set $B \subseteq \R^3$.
*Infinitesimal strain theory* is the approximation valid when $\norm{\nabla u(X)} \ll 1$ for all $X \in B$, in which:

1. terms of order two and higher in $\nabla u$ are neglected;
2. the [[Green–Lagrange tensor|MRANPXATRD]] is replaced by its linear part, the [[strain tensor|8QS6QMJF5Z]] $\varepsilon = \tfrac12 (\nabla u + (\nabla u)^T)$;
3. the reference and the deformed configurations are identified, so material and spatial coordinates are not distinguished.

## Remarks

A uniform extension $u(X) = (10^{-3} X_1, 0, 0)$ satisfies the smallness condition.
Its strain $\varepsilon = \operatorname{diag}(10^{-3}, 0, 0)$ differs from $E = \operatorname{diag}(10^{-3} + \tfrac12 10^{-6}, 0, 0)$ only in the neglected term.
A rotation of the body by $90$ degrees does not satisfy the smallness condition, since $\nabla u = Q - I$ has norm of order $1$.
The linear theory would assign it a spurious strain.
The smallness of the strain alone is not enough: rotations must also be small.

## Explanations

### L1 human

Infinitesimal strain theory linearises everything about deformation.
It works when both stretches and rotations are tiny, which is the usual case for stiff structures.
