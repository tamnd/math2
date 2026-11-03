---
tag: 2MZNG3DY5E
kind: definition
name: Oseen–Frank elastic energy of liquid crystals
msc: [76A15]
defines: BYWG3ADRF3
uses: [0299VCW1TH, 0MWV6ZTK6S, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/Distortion_free_energy_density
---

## Definition

Let $\Omega \subset \R^3$ be a bounded open set filled with a nematic liquid crystal.
A *director field* is a $C^1$ [[vector field|0299VCW1TH]] $n \colon \Omega \to \R^3$ with $\abs{n(x)} = 1$ for all $x$.
Let $K_1, K_2, K_3 > 0$ be the splay, twist and bend elastic constants.
The *Oseen–Frank energy density* is
$$W(n, \nabla n) = \frac{K_1}{2} (\nabla \cdot n)^2 + \frac{K_2}{2} \big(n \cdot (\nabla \times n)\big)^2 + \frac{K_3}{2} \abs{n \times (\nabla \times n)}^2,$$
where $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]] and $\nabla \times$ is the [[curl|0NF6GQNXMY]], and the *Oseen–Frank energy* is $E(n) = \int_\Omega W(n, \nabla n) \, dx$.

## Remarks

The general form adds a saddle-splay term with a fourth constant.
It is a divergence, so it contributes only a boundary term and does not change the Euler–Lagrange equations in the interior.
The energy is unchanged under $n \mapsto -n$, as it should be, since a nematic does not distinguish the two ends of a molecule.
Example: the twisted field $n(x, y, z) = (\cos qz, \sin qz, 0)$ has $\abs{n} = 1$, $\nabla \cdot n = 0$ and $\nabla \times n = -q n$.
So $n \cdot (\nabla \times n) = -q$ and $n \times (\nabla \times n) = 0$, which gives $W = K_2 q^2 / 2$: a pure twist.
Non-example: the field $n(x) = x / \abs{x}$ is not a director field on a ball around $0$, because it is not defined at $0$.
It is the hedgehog defect, and its energy density $W = 2K_1 / \abs{x}^2$ is still integrable near $0$.
In the one-constant approximation $K_1 = K_2 = K_3 = K$, the energy equals $\frac{K}{2} \int_\Omega \abs{\nabla n}^2 \, dx$ up to a boundary term, which is the Dirichlet energy of a map into the unit sphere.

## Explanations

### L1 human

Each term of the energy is the square of one kind of distortion, multiplied by a stiffness.
The divergence measures splay, the component of the curl along $n$ measures twist, and the component of the curl across $n$ measures bend.
