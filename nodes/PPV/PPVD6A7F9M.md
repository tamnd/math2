---
tag: PPVD6A7F9M
kind: definition
name: Strain tensor
msc: [74A05]
defines: 8QS6QMJF5Z
uses: [E51Y1CMF1Q, 0ABK9V9Y64, 09DXWYRD43, 0PBY4E9GQF]
sources:
  - url: https://en.wikipedia.org/wiki/Strain_(mechanics)
---

## Definition

Let $B \subseteq \R^3$ be open and let $u \colon B \to \R^3$ be the continuously differentiable displacement of a [[deformation|E51Y1CMF1Q]] of $B$.
Let $\nabla u$ be the matrix whose rows are the [[gradients|0ABK9V9Y64]] of the components of $u$, and let $(\nabla u)^T$ be its [[transpose|09DXWYRD43]].
The *(infinitesimal) strain tensor* of $u$ is the symmetric matrix field below.
$$\varepsilon(u) = \tfrac12 \left( \nabla u + (\nabla u)^T \right), \qquad \varepsilon_{ij} = \tfrac12 \left( \frac{\partial u_i}{\partial X_j} + \frac{\partial u_j}{\partial X_i} \right).$$

## Remarks

For $u(X) = (a X_1, 0, 0)$ with $a \in \R$, one gets $\varepsilon = \operatorname{diag}(a, 0, 0)$: a relative extension $a$ along the first axis.
For an infinitesimal rotation $u(X) = W X$ with $W$ a [[skew-symmetric matrix|0PBY4E9GQF]], one gets $\varepsilon = \tfrac12 (W + W^T) = 0$: such a displacement produces no strain.
The skew part $\omega = \tfrac12 (\nabla u - (\nabla u)^T)$ is the infinitesimal rotation tensor, and $\nabla u = \varepsilon + \omega$.
The trace $\operatorname{tr} \varepsilon = \operatorname{div} u$ is the relative change of volume to first order.
In finite strain theory the name strain tensor also refers to measures such as the Green–Lagrange tensor, whose linear part in $\nabla u$ is $\varepsilon$.

## Explanations

### L1 human

The strain tensor is the part of the displacement gradient that really stretches or shears the material.
The rest is a small rotation, which moves the material without straining it.
