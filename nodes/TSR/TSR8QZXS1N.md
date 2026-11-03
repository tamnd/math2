---
tag: TSR8QZXS1N
kind: statement
role: theorem
name: Helmholtz decomposition of electromagnetic fields
msc: [78A25, 35Q61, 31B10]
uses: [0299VCW1TH, 0MWV6ZTK6S, 0NF6GQNXMY, 0ABK9V9Y64, 0E0B6RA8K0, DCMFQ01QGS, QK1KWYZNRD, YZ7Q9DP8RT, XRED3C547P]
about: [0299VCW1TH, YZ7Q9DP8RT, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz_decomposition
---

## Statement

Let $F \colon \R^3 \to \R^3$ be a twice continuously differentiable [[vector field|0299VCW1TH]] with compact support.
Define
$$\Phi(x) = \frac{1}{4\pi} \int_{\R^3} \frac{\nabla' \cdot F(x')}{\abs{x - x'}} \, dx', \qquad A(x) = \frac{1}{4\pi} \int_{\R^3} \frac{\nabla' \times F(x')}{\abs{x - x'}} \, dx',$$
where $\nabla' \cdot$ is the [[divergence|0MWV6ZTK6S]] and $\nabla' \times$ is the [[curl|0NF6GQNXMY]] in the variable $x'$.
Then
$$F = -\nabla \Phi + \nabla \times A,$$
where $\nabla \Phi$ is the [[gradient|0ABK9V9Y64]] of $\Phi$.
The field $-\nabla \Phi$ has zero curl and the field $\nabla \times A$ has zero divergence.
This splitting is unique in the following sense.
Let $F = G_1 + S_1 = G_2 + S_2$ with continuously differentiable fields $G_1, G_2, S_1, S_2$.
Assume that $G_1, G_2$ have zero curl, that $S_1, S_2$ have zero divergence, and that all four tend to $0$ as $\abs{x} \to \infty$.
Then $G_1 = G_2$ and $S_1 = S_2$.

## Remarks

Proof idea: let $W$ be the [[Newtonian potential|DCMFQ01QGS]] $W(x) = -\frac{1}{4\pi} \int F(x') / \abs{x - x'} \, dx'$, so that $\Delta W = F$ with the [[Laplacian|0E0B6RA8K0]] taken componentwise.
The identity $\Delta W = \nabla (\nabla \cdot W) - \nabla \times (\nabla \times W)$ gives the splitting with $\Phi = -\nabla \cdot W$ and $A = -\nabla \times W$, and an integration by parts turns these into the formulas above.
For uniqueness, $G_1 - G_2 = S_2 - S_1$ has zero curl and zero divergence, so each component is harmonic; it tends to $0$ at infinity, so it vanishes by [[Liouville's theorem|QK1KWYZNRD]].
The decay condition is needed: the constant field $(1, 0, 0)$ has zero curl and zero divergence, so it can be counted in either part.

In electromagnetism the splitting is applied to the [[electric field|YZ7Q9DP8RT]] $E$ and the [[magnetic field|XRED3C547P]] $B$.
Since $\nabla \cdot B = 0$, the field $B$ has no curl-free part, so $B = \nabla \times A$ for a vector potential $A$.
The curl-free part of $E$ is called its longitudinal part and the divergence-free part its transverse part.
In the Coulomb gauge $\nabla \cdot A = 0$, one has $E = -\nabla \varphi - \partial_t A$ with $-\nabla \varphi$ longitudinal and $-\partial_t A$ transverse, and $\varphi$ is the instantaneous Coulomb potential of the charge density.

## Explanations

### L1 human

Every reasonable vector field is the sum of two simpler fields.
One part flows out of sources and sinks and has no swirl, like the field of a point charge.
The other part only swirls and has no sources, like the field around a wire carrying current.
The theorem says how to find both parts, and that they are determined by the field when everything dies out far away.

### L2 human

The two parts are found from the divergence and the curl of the field, through the Newtonian potential.
So a field that decays at infinity is fixed by its divergence and curl.
Maxwell's equations give exactly these: Gauss's laws give the divergences of $E$ and $B$, and the laws of Faraday and Ampère–Maxwell give their curls.
The decomposition is the reason one can always write $B$ as a curl, and it splits $E$ into an instantaneous Coulomb part and a radiating part.
On bounded domains the analogous splitting needs boundary conditions and leads to the Hodge decomposition of vector fields.
