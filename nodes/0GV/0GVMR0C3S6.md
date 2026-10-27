---
tag: 0GVMR0C3S6
kind: definition
name: Moment of inertia
msc: [26B15, "70E15"]
defines: 08ANASGBXV
uses: [0GTBGMZXV8, 0NKBMFC18R]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_of_inertia
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Moment_of_inertia
    locator: Rigid body
inventory: [W3BDM8GRKG]
---

## Definition

Let $E \subseteq \mathbb{R}^3$ be a bounded Jordan measurable set with a continuous density $\delta \colon E \to [0, \infty)$, and let $L$ be a line in $\mathbb{R}^3$.
For $x \in E$, let $d_L(x)$ be the distance from $x$ to $L$.
The moment of inertia of $E$ about $L$ is
$$I_L = \iiint_E d_L(x)^2 \, \delta(x) \, dV.$$
In particular, $I_z = \iiint_E (x^2 + y^2) \, \delta(x, y, z) \, dV$ is the moment of inertia about the $z$-axis.

## Remarks

For a plane lamina $D \subseteq \mathbb{R}^2$, the moments of inertia about the coordinate axes are $I_x = \iint_D y^2 \delta \, dA$ and $I_y = \iint_D x^2 \delta \, dA$. These are [[double integrals|0NKBMFC18R]].
For a point mass $m$ at distance $r$ from the axis, the moment of inertia is $m r^2$.
Example: a solid cylinder of radius $a$, height $h$ and constant density has mass $M = \delta \pi a^2 h$ and $I_z = \delta \int_0^h \int_0^{2\pi} \int_0^a r^3 \, dr \, d\theta \, dz = \tfrac{1}{2} M a^2$.
For rotation about $L$ with angular velocity $\omega$, the kinetic energy is $\tfrac{1}{2} I_L \omega^2$.

## Explanations

### L1 human

Mass far from the axis is harder to set spinning than mass close to it.
The moment of inertia adds up all the mass, weighted by the square of its distance from the axis.
