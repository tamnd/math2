---
tag: WDNE4NRKE4
kind: definition
name: Deformation gradient
msc: [74A05]
defines: HTYRR2WDQ6
uses: [E51Y1CMF1Q, 047NDTEPCV, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
    locator: Deformation gradient tensor
---

## Definition

Let $B \subseteq \R^3$ be open and let $\varphi \colon B \to \R^3$ be a [[deformation|E51Y1CMF1Q]].
The *deformation gradient* of $\varphi$ at $X \in B$ is the [[Jacobian matrix|047NDTEPCV]]
$$F(X) = \nabla \varphi(X), \qquad F_{iJ}(X) = \frac{\partial \varphi_i}{\partial X_J}(X), \quad i, J \in \set{1, 2, 3}.$$
Its [[determinant|00KDZRW4C0]] $J(X) = \det F(X)$ is the *Jacobian* of the deformation; it is positive.

## Remarks

For the simple shear $\varphi(X) = (X_1 + \gamma X_2, X_2, X_3)$ with $\gamma \in \R$, the rows of $F$ are $(1, \gamma, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, and $J = 1 > 0$, so volumes are preserved.
The matrix $\operatorname{diag}(-1, 1, 1)$ is not the deformation gradient of any deformation, since its determinant is negative.
In terms of the displacement $u(X) = \varphi(X) - X$ one has $F = I + \nabla u$.
To first order, $\varphi(X + dX) - \varphi(X) = F(X)\, dX$, and a small volume $dV$ becomes $J\, dV$.

## Explanations

### L1 human

The deformation gradient is the derivative of the deformation.
It says how a tiny arrow attached to the material is stretched and turned.
Its determinant says by what factor tiny volumes grow or shrink.
