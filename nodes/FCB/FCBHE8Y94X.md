---
tag: FCBHE8Y94X
kind: definition
name: Finite strain theory
msc: [74A05, 74B20]
defines: E949EQWCHF
uses: [E51Y1CMF1Q, HTYRR2WDQ6, N5G8WNQFC3, MRANPXATRD]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
---

## Definition

*Finite strain theory* (or *large deformation theory*) is the kinematics of [[deformations|E51Y1CMF1Q]] $\varphi \colon B \to \R^3$ of a body $B \subseteq \R^3$.
In it, no smallness is assumed on the displacement gradient $\nabla u = F - I$.
The local state of deformation is described exactly by the [[deformation gradient|HTYRR2WDQ6]] $F$ and the [[Cauchy–Green tensors|N5G8WNQFC3]] $C = F^T F$ and $b = F F^T$.
Strain is measured by tensors built from them, such as the [[Green–Lagrange tensor|MRANPXATRD]] $E = \tfrac12 (C - I)$.
The reference configuration $B$ and the deformed configuration $\varphi(B)$ are distinguished, and quantities are defined on one or the other.

## Remarks

A rotation of the body by $90$ degrees has $F = Q$ with $Q$ orthogonal, so $E = 0$ and finite strain theory correctly records no strain.
The small-strain tensor $\tfrac12 (\nabla u + (\nabla u)^T)$ of the same motion is not zero, so the infinitesimal theory does not apply to it.
Other common finite strain measures are the Euler–Almansi tensor $\tfrac12 (I - b^{-1})$ and the Hencky or logarithmic strain $\tfrac12 \ln C$.

## Explanations

### L1 human

Finite strain theory is the exact geometry of deformation.
It is what remains when one refuses to neglect squares of small quantities.
