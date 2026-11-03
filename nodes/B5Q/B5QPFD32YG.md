---
tag: B5QPFD32YG
kind: definition
name: Projective Hilbert space
msc: ["81P16", "46C05", "51N15"]
defines: RC1C7WXX1H
uses: [HM2HHE3J51, ZT9A6JK8QF, 7GJ4STCNNM]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_Hilbert_space
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] with $\mathcal{H} \ne \set{0}$.
On $\mathcal{H} \setminus \set{0}$, let $\psi \sim \varphi$ when $\varphi = c\psi$ for some $c \in \C \setminus \set{0}$.
The *projective Hilbert space* of $\mathcal{H}$ is the quotient set
$$\mathbf{P}(\mathcal{H}) = (\mathcal{H} \setminus \set{0}) / \sim.$$
Its elements are the *rays* $[\psi]$.

## Remarks

Every ray contains unit vectors, and two unit vectors $\psi, \varphi$ lie on the same ray if and only if $\varphi = e^{i\theta}\psi$ for some $\theta \in \R$.
So $\mathbf{P}(\mathcal{H})$ is also the unit sphere of $\mathcal{H}$ modulo multiplication by phases.
It is the [[projective space|ZT9A6JK8QF]] of the vector space $\mathcal{H}$; for $\mathcal{H} = \C^{n+1}$ it is [[$\mathbb{CP}^n$|7GJ4STCNNM]].

Example: in $\C^2$, the vectors $(1, i)$ and $(i, -1) = i(1, i)$ lie on the same ray.

Non-example: $(1, 0)$ and $(0, 1)$ lie on different rays, since $(0, 1) = c(1, 0)$ would force $1 = 0$.
Also $(1, 1)$ and $(1, -1)$ lie on different rays, although their entries have the same moduli: a relative phase between the components changes the ray, an overall phase does not.
