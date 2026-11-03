---
tag: Q7NGBMKAQ5
kind: definition
name: Polyakov action
msc: [81T30, "83E30"]
defines: HFEGZQB8SV
uses: [T0WAGV4KP4, GH6CXWFNDJ, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Polyakov_action
---

## Definition

Let $(M, G)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] of dimension $D$, the target spacetime, with local coordinates $X^\mu$.
Let $\Sigma$ be a two-dimensional manifold, the worldsheet, with local coordinates $\sigma^a = (\sigma^0, \sigma^1)$.
Let $h$ be a [[Lorentzian|BY4QYYS788]] metric on $\Sigma$ with components $h_{ab}$, inverse $h^{ab}$ and determinant $\det h$.
Let $X \colon \Sigma \to M$ be a smooth map, and let $T > 0$ be a constant, the string tension.
The *Polyakov action* is the [[action|T0WAGV4KP4]]
$$S_P[X, h] = -\frac{T}{2} \int_\Sigma \sqrt{-\det h}\; h^{ab}\, \partial_a X^\mu\, \partial_b X^\nu\, G_{\mu\nu}(X)\; d^2\sigma,$$
with summation over repeated indices.
The tension is often written $T = 1/(2\pi\alpha')$, where $\alpha'$ is the Regge slope.

## Remarks

The action is invariant under diffeomorphisms of $\Sigma$, under isometries of $(M, G)$, and under Weyl rescalings $h \mapsto e^{2\omega} h$ for any smooth function $\omega$ on $\Sigma$.
The Weyl invariance holds because $\Sigma$ has dimension $2$: then $\sqrt{-\det h}\, h^{ab}$ does not change under rescaling.
Example: take $M = \R^{1, D-1}$ with the Minkowski metric $\eta$, and choose the flat worldsheet metric $h = \operatorname{diag}(-1, 1)$, the conformal gauge.
Then $S_P = \frac{T}{2} \int \big( \partial_0 X \cdot \partial_0 X - \partial_1 X \cdot \partial_1 X \big)\, d^2\sigma$, where the dot is the Minkowski product, and the Euler–Lagrange equations are the wave equations $(\partial_0^2 - \partial_1^2) X^\mu = 0$.
Non-example: the functional $\int h^{ab}\, \partial_a X^\mu \partial_b X^\nu G_{\mu\nu}\, d^2\sigma$ without the factor $\sqrt{-\det h}$ is not the Polyakov action; it is not invariant under diffeomorphisms of $\Sigma$, since the integrand is not a density.
Varying $h$ gives the constraint that $h$ is conformal to the metric induced by $X$ from $G$.
Putting this back into $S_P$ gives the [[Nambu–Goto action|W4GZMZ796R]] $-T \int \sqrt{-\det(X^* G)}\, d^2\sigma$.
