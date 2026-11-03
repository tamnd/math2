---
tag: C02XZJBFSY
kind: statement
role: proposition
name: Lens equation
msc: [85A04, 83C99, 78A05]
uses: [JJCKCYTBXD, YDWH956TJA]
about: [JJCKCYTBXD]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_lens
---

## Statement

Let a source and a lens lie at angular diameter distances $D_s$ and $D_d$ from an observer.
Let $D_{ds}$ be the distance from the lens to the source, as in [[distance measures|YDWH956TJA]].
Assume the thin-lens approximation: the mass of the lens lies in a plane, and all angles are small.
The [[deflection of light|JJCKCYTBXD]] then happens at that plane.
Let $\beta \in \R^2$ be the true angular position of the source.
Let $\hat\alpha(\theta) \in \R^2$ be the deflection angle of a ray that crosses the lens plane at angular position $\theta \in \R^2$.
Then the source is seen at the angular positions $\theta$ that solve
$$\beta = \theta - \frac{D_{ds}}{D_s} \, \hat\alpha(\theta).$$

## Remarks

The proof is geometry in the plane of the source.
The straight line from the observer at angle $\theta$ reaches the source plane at distance $\theta D_s$ from the axis.
The deflection moves the ray by $\hat\alpha D_{ds}$, and the ray must end at the source, at $\beta D_s$; dividing by $D_s$ gives the equation.
In a curved expanding universe the same form holds when the distances are angular diameter distances.

The reduced deflection $\alpha = (D_{ds}/D_s) \hat\alpha$ is often used, so that $\beta = \theta - \alpha(\theta)$.
For a point mass $M$, $\hat\alpha = 4 G M / (c^2 D_d \abs{\theta})$ in the direction of the lens, and the equation becomes $\beta = \theta - \theta_E^2 \, \theta / \abs{\theta}^2$ with $\theta_E^2 = \frac{4 G M}{c^2} \frac{D_{ds}}{D_d D_s}$.
For $\beta = 0$ every $\theta$ with $\abs{\theta} = \theta_E$ is a solution: the image is a ring.
For $\beta \ne 0$ there are exactly two images, on either side of the lens.

## Explanations

### L1 human

Gravity bends light, so a massive object between us and a distant source acts like a lens.
The lens equation tells where on the sky the images of the source appear.
It is a map from the image position to the true position; one true position can have several images.

### L2 human

The lens equation is a map $\theta \mapsto \beta$ of the plane to itself.
Its Jacobian gives the magnification and the distortion of images, and the curves where the Jacobian vanishes are the critical curves.
Strong lensing, weak lensing and microlensing are all studied through this one equation with different deflection fields.
