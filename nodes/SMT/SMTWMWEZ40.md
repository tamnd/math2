---
tag: SMTWMWEZ40
kind: definition
name: Love wave
msc: [74J15, 86A15]
defines: A2E51V42RH
uses: [T1PYEBKBAJ, GZ7E9GHQYB, J2GWW1NPTC]
sources:
  - url: https://en.wikipedia.org/wiki/Love_wave
---

## Definition

Let $x$ and $y$ be horizontal coordinates and $z$ the depth below a free surface $z = 0$.
Let a homogeneous isotropic elastic layer $0 < z < H$ have [[shear modulus|J2GWW1NPTC]] $\mu_1$ and [[S-wave|GZ7E9GHQYB]] speed $\beta_1$.
Let it lie on a homogeneous isotropic half-space $z > H$ with shear modulus $\mu_2$ and S-wave speed $\beta_2 > \beta_1$.
Consider displacements of the form
$$u = \left( 0, \, \operatorname{Re} \left[ f(z) e^{i k (x - c t)} \right], \, 0 \right), \qquad k > 0.$$
A *Love wave* is a nonzero solution of this form of the [[elastodynamic|T1PYEBKBAJ]] equations such that:

1. $u_2$ and the shear traction $\mu \, \partial u_2 / \partial z$ are continuous at $z = H$,
2. the shear traction vanishes at $z = 0$, and
3. $f(z) \to 0$ as $z \to \infty$.

Such solutions exist exactly when $\beta_1 < c < \beta_2$ and
$$\tan \left( k H \sqrt{\frac{c^2}{\beta_1^2} - 1} \right) = \frac{\mu_2 \sqrt{1 - c^2 / \beta_2^2}}{\mu_1 \sqrt{c^2 / \beta_1^2 - 1}}.$$

## Remarks

The relation comes from $f(z) = A \cos(k s_1 z)$ in the layer and $f(z) = B e^{-k s_2 (z - H)}$ in the half-space, with $s_1 = \sqrt{c^2/\beta_1^2 - 1}$ and $s_2 = \sqrt{1 - c^2/\beta_2^2}$.
The cosine satisfies the free-surface condition, and matching $f$ and $\mu f'$ at $z = H$ gives $\mu_1 s_1 \sin(k s_1 H) = \mu_2 s_2 \cos(k s_1 H)$.

Example: fix $k > 0$ and let $c$ run from $\beta_1$ to $\beta_2$.
The left side starts at $0$ and grows, up to the first pole of the tangent if there is one, while the right side decreases from $+\infty$ to $0$.
So the two sides are equal for at least one $c(k)$ in $(\beta_1, \beta_2)$, which gives the fundamental Love mode.

Non-example: a homogeneous half-space, $H = 0$.
Then decay with depth needs $c < \beta_2$, and a traction-free surface forces $f' (0) = 0$, which together with $f = B e^{-k s_2 z}$ gives $B = 0$.
So there is no Love wave without a slower layer.
