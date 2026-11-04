---
tag: YPAMM8HYP6
kind: proof
name: Proof that the curl of a gradient is zero
msc: ["26B12"]
proves: 0M2JRW1J0N
uses: [0GDNHS9J2X, 0NS2QYVC4Y, 0NNQY8WCW6, 0TCBZMEYGN, 0KXSK8TEEB, 02RSXVM1ZN]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Curl of gradient is zero
---

## Proof

We compute the curl in coordinates and use the symmetry of second derivatives.

1. Let $\phi \colon U \to \R$ be of [[class $C^2$|0TCBZMEYGN]] on the open set $U \subseteq \R^3$. Its first partial derivatives are continuous, so $\phi$ is differentiable by [[continuous partial derivatives imply differentiability|0KXSK8TEEB]].
2. By the coordinate form of the [[gradient|0NS2QYVC4Y]], $\nabla \phi = (\phi_x, \phi_y, \phi_z)$, where $\phi_x = \partial \phi / \partial x$ and so on.
3. The components of $\nabla \phi$ have first partial derivatives on $U$, since $\phi$ is $C^2$. For variables $u, v \in \set{x, y, z}$, write $\partial_u \phi_v$ for the [[second partial derivative|02RSXVM1ZN]] $\partial^2 \phi / \partial u \, \partial v$.
4. By the definition of the [[curl|0GDNHS9J2X]] with $(P, Q, R) = (\phi_x, \phi_y, \phi_z)$, $\nabla \times (\nabla \phi) = \big( \partial_y \phi_z - \partial_z \phi_y, \ \partial_z \phi_x - \partial_x \phi_z, \ \partial_x \phi_y - \partial_y \phi_x \big)$.
5. By [[Schwarz's theorem|0NNQY8WCW6]], $\partial_y \phi_z = \partial_z \phi_y$, $\partial_z \phi_x = \partial_x \phi_z$ and $\partial_x \phi_y = \partial_y \phi_x$ at each point of $U$.
6. So each component in step 4 is $0$, and $\nabla \times (\nabla \phi) = 0$ on $U$.

## Idea

Each component of the curl of $\nabla \phi$ is a difference of two mixed second partial derivatives of $\phi$, taken in the two possible orders. For a $C^2$ function these agree, so every component vanishes.
