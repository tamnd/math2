---
tag: TZYZ78HRY2
kind: definition
name: Magnetic field
msc: [78A30, 78A25]
defines: XRED3C547P
uses: [6XPSV47R56, YZ7Q9DP8RT, 0299VCW1TH, 0N5N15HWZ7, 9BWWD4QK8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_field
---

## Definition

Let $U \subseteq \R^3$ be a region of space and $I \subseteq \R$ an interval of time.
The *magnetic field* in $U$ is a [[vector field|0299VCW1TH]] $B \colon U \times I \to \R^3$ with the following property.
Let a point [[charge|6XPSV47R56]] $q$ be at $x \in U$ at time $t \in I$, moving with velocity $v \in \R^3$.
Besides the electric force $q E(x, t)$, it feels the magnetic force
$$F_{\mathrm{mag}} = q \, v \times B(x, t),$$
where $\times$ is the [[cross product|0N5N15HWZ7]] and $E$ is the [[electric field|YZ7Q9DP8RT]].

## Remarks

The field $B$ is determined by this property: the forces for velocities $v = e_1$ and $v = e_2$ give the components of $B$ orthogonal to $e_1$ and to $e_2$, hence all of $B$.
Together with $E$, the field $B$ satisfies [[Maxwell's equations|9BWWD4QK8Y]].
Example: the field $B(x) = (0, 0, B_0)$ is a uniform magnetic field of strength $B_0$ along the third axis; a charge moving along the first axis is pushed along the second axis.
Non-example: the vector field $B(x) = x$ is not a possible magnetic field, since its divergence is $3 \ne 0$, while every magnetic field is divergence-free.
Some texts call $B$ the magnetic flux density and reserve "magnetic field" for $H = B / \mu_0 - M$, where $M$ is the magnetization.
The SI unit of $B$ is the tesla.
