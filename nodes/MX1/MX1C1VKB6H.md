---
tag: MX1C1VKB6H
kind: definition
name: Vorticity
msc: [76A02, 76B47]
defines: B3SXT9TWFA
uses: [0NF6GQNXMY, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Vorticity
---

## Definition

Let $\Omega \subseteq \R^3$ be open and let $\mathbf{u} = (u_1, u_2, u_3) \colon \Omega \to \R^3$ be a continuously differentiable velocity field.
The *vorticity* of $\mathbf{u}$ is the [[vector field|0299VCW1TH]] $\boldsymbol{\omega} = \nabla \times \mathbf{u}$, the [[curl|0NF6GQNXMY]] of $\mathbf{u}$:
$$\boldsymbol{\omega} = \left( \frac{\partial u_3}{\partial x_2} - \frac{\partial u_2}{\partial x_3},\ \frac{\partial u_1}{\partial x_3} - \frac{\partial u_3}{\partial x_1},\ \frac{\partial u_2}{\partial x_1} - \frac{\partial u_1}{\partial x_2} \right).$$
For a plane flow $\mathbf{u} = (u, v)$ the vorticity is the scalar $\omega = \partial v / \partial x - \partial u / \partial y$.
The flow is *irrotational* if $\boldsymbol{\omega} = 0$ on $\Omega$.

## Remarks

Example: the rigid rotation $\mathbf{u} = (-\Omega y, \Omega x, 0)$ has $\boldsymbol{\omega} = (0, 0, 2\Omega)$, twice its angular velocity.
Example: the shear flow $\mathbf{u} = (y, 0, 0)$ has $\boldsymbol{\omega} = (0, 0, -1)$, although its streamlines are straight lines.
Non-example of an irrotational flow: either of these, since $\boldsymbol{\omega} \ne 0$.
The field $\mathbf{u} = (x, -y, 0)$ is irrotational, since all the cross derivatives vanish.
