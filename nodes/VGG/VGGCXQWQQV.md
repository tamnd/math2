---
tag: VGGCXQWQQV
kind: definition
name: Nambu mechanics
msc: [70H05, 37J39, 53D17]
defines: 86CS9DXZ6M
uses: [0NS2QYVC4Y, 047NDTEPCV, 0262JP0NV9]
sources:
  - url: https://en.wikipedia.org/wiki/Nambu_mechanics
---

## Definition

Let $V \subseteq \R^3$ be open, with coordinates $x = (x_1, x_2, x_3)$.
The *Nambu bracket* of smooth functions $f, g, h$ on $V$ is the [[Jacobian|047NDTEPCV]] determinant
$$\{f, g, h\} = \det \frac{\partial(f, g, h)}{\partial(x_1, x_2, x_3)} = \nabla f \cdot \big(\nabla g \times \nabla h\big).$$
Let $H_1, H_2$ be smooth functions on $V$.
The *Nambu system* with Hamiltonians $H_1, H_2$ is the system
$$\dot x = \nabla H_1(x) \times \nabla H_2(x),$$
where $\nabla$ is the [[gradient|0NS2QYVC4Y]] and $\times$ is the cross product.
Equivalently, every smooth function $f$ evolves by $\dot f = \{f, H_1, H_2\}$.

## Remarks

The bracket is antisymmetric in its three arguments, satisfies the Leibniz rule in each argument, and satisfies a generalized Jacobi identity, the fundamental identity.
Since $\{H_1, H_1, H_2\} = \{H_2, H_1, H_2\} = 0$, both $H_1$ and $H_2$ are [[first integrals|0262JP0NV9]].
The vector field $\nabla H_1 \times \nabla H_2$ has divergence $0$, so its flow preserves volume.
On $\R^n$ the construction uses $n - 1$ Hamiltonians and the $n \times n$ Jacobian determinant.

Example: Euler's equations of a free rigid body with principal moments $I_1, I_2, I_3 > 0$ and angular momentum $L \in \R^3$.
Take $H_1 = \frac{1}{2} \abs{L}^2$ and $H_2 = \frac{1}{2} \big(L_1^2 / I_1 + L_2^2 / I_2 + L_3^2 / I_3\big)$.
Then $\nabla H_1 = L$ and $\nabla H_2 = \omega$ with $\omega_i = L_i / I_i$, and the system is $\dot L = L \times \omega$; its first component is $I_1 \dot \omega_1 = (I_2 - I_3) \omega_2 \omega_3$.

Non-example: the damped system $\dot x = -x$ on $\R^3$ is not a Nambu system for any $H_1, H_2$, since its divergence is $-3 \ne 0$.
