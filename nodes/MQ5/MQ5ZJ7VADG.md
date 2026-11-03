---
tag: MQ5ZJ7VADG
kind: definition
name: Gradient-index optics
msc: [78A05]
defines: C9TV3FZEM4
uses: [9VGK0SP6EQ, RKX9XJ0RVW, AQ5ZKPZ88R, HGMX1QGTAZ]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient-index_optics
---

## Definition

A *gradient-index medium* is an open set $\Omega \subseteq \R^3$ with a smooth [[refractive index|9VGK0SP6EQ]] $n \colon \Omega \to (0, \infty)$ that is not constant.
A *ray* in the medium is a smooth curve $s \mapsto r(s)$ in $\Omega$, parametrised by arc length $s$, that satisfies the ray equation
$$\frac{d}{ds}\left( n(r(s)) \, \frac{dr}{ds} \right) = \nabla n(r(s)).$$
*Gradient-index optics* is the study of the rays, and of the images they form, in such media.

## Remarks

The ray equation is the Euler–Lagrange equation of the [[optical path length|AQ5ZKPZ88R]] $\int n(r(s)) \, ds$, so the rays are the curves of stationary optical length, as [[Fermat's principle|RKX9XJ0RVW]] says.
Equivalently, the rays are the geodesics of the Riemannian metric $n(x)^2 \abs{dx}^2$ on $\Omega$, and the optical path length from a point solves the [[eikonal equation|HGMX1QGTAZ]] $\abs{\nabla L} = n$.
Example: in a slab with $n(x, y, z) = n_0 \sqrt{1 - \alpha^2 x^2}$, rays near the $z$-axis oscillate about it like sine curves, which is how a graded-index fibre guides light.
Non-example: if $n$ is constant, the ray equation gives $d^2 r / ds^2 = 0$, so the rays are straight lines; a homogeneous medium is not a gradient-index medium.

## Explanations

### L1 human

In a medium whose index changes from point to point, the direction of a ray changes at a rate given by the gradient of the index.
The ray curves toward the side where the index is higher.
