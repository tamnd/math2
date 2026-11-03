---
tag: VG1M7QVXBM
kind: definition
name: Anisotropic heat conduction
msc: [80A19, 80A17]
defines: M1J161A2QY
uses: [SW8X60GYZT, 9YJZ1PP2Y8, 1Y36434YTE, 0VR671PHE5, 0KX66CZMBB, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_conduction
---

## Definition

Let a body occupy an open set $\Omega \subseteq \R^n$, with temperature $T$ differentiable in $x$.
Let $K(x)$ be a [[symmetric|0VR671PHE5]] [[positive definite|0KX66CZMBB]] $n \times n$ matrix for each $x \in \Omega$, the *conductivity tensor*.
*Anisotropic heat conduction* is [[conduction|SW8X60GYZT]] whose [[heat flux|1Y36434YTE]] is
$$\mathbf{q} = -K \, \nabla T,$$
where $K$ is not a scalar multiple of the identity matrix.
With density $\rho$, specific heat $c$ and source density $f$, the temperature obeys
$$\rho \, c \, \partial_t T = \nabla \cdot \left(K \nabla T\right) + f.$$

## Remarks

When $K = k I$, this is the isotropic [[Fourier's law|9YJZ1PP2Y8]].

Example: in $\R^2$ let $K = \operatorname{diag}(4, 1)$ and $\nabla T = (1, 1)$.
Then $\mathbf{q} = (-4, -1)$, which is not parallel to $\nabla T$.
Still $\mathbf{q} \cdot \nabla T = -5 < 0$, so heat flows to the colder side.

Non-example: $K = \operatorname{diag}(1, -1)$ is symmetric but not positive definite.
With $\nabla T = (0, 1)$ it gives $\mathbf{q} = (0, 1)$, so heat would flow from cold to hot.

Positive definiteness is the condition $\mathbf{q} \cdot \nabla T = -\nabla T \cdot K \nabla T < 0$ whenever $\nabla T \ne 0$.
