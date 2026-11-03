---
tag: ZFYRQNNQHM
kind: definition
name: Strain rate tensor
msc: [76A02, 74A05]
defines: P1KWMQG4NZ
uses: [047NDTEPCV, 0VR671PHE5, WX302T93TW, 0XC1RDBY7A, 0MWV6ZTK6S, B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Strain-rate_tensor
---

## Definition

Let $\Omega \subseteq \R^3$ be open and let $\mathbf{u} \colon \Omega \to \R^3$ be a continuously differentiable velocity field.
Let $L = \nabla \mathbf{u}$ be its velocity gradient, the [[Jacobian matrix|047NDTEPCV]] with entries $L_{ij} = \partial u_i / \partial x_j$.
The *strain rate tensor* of $\mathbf{u}$ is the [[symmetric matrix|0VR671PHE5]] field
$$E = \tfrac{1}{2} \left( L + L^{T} \right), \qquad E_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right).$$

## Remarks

The remaining part $W = \tfrac{1}{2}(L - L^{T})$ is the spin tensor, and $W_{ij} = -\tfrac{1}{2} \sum_k \varepsilon_{ijk} \omega_k$, where $\boldsymbol{\omega}$ is the [[vorticity|B3SXT9TWFA]] and $\varepsilon_{ijk}$ is the Levi-Civita symbol.
The [[trace|0XC1RDBY7A]] of $E$ is the [[divergence|0MWV6ZTK6S]] $\nabla \cdot \mathbf{u}$.
Example: for the shear flow $\mathbf{u} = (y, 0, 0)$, $L$ has the single nonzero entry $L_{12} = 1$, so $E_{12} = E_{21} = 1/2$ and all other entries of $E$ are $0$.
Non-example: the velocity gradient $L$ of this shear flow is not the strain rate tensor, since $L$ is not symmetric.
A rigid motion $\mathbf{u}(x) = \mathbf{a} + \mathbf{b} \times x$ has $E = 0$.
It is a [[tensor field|WX302T93TW]] of rank two; other names are rate-of-strain tensor and rate-of-deformation tensor.
