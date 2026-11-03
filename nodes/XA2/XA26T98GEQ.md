---
tag: XA26T98GEQ
kind: definition
name: Higgs mechanism
msc: [81R40, 81T13, 81V15]
defines: F985ZCF9SZ
uses: [BXVB6WCMEV, 3498FHKNFK, EVHCE5VR6Y, 5JJYBJ6A8K, 2K8BZRGE8R, 707DEWCCFX]
sources:
  - url: https://en.wikipedia.org/wiki/Higgs_mechanism
---

## Definition

Let $G$ be a [[compact|EVHCE5VR6Y]] Lie group with [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{g}$, carrying an invariant inner product.
Let $V$ be a real orthogonal [[representation|2K8BZRGE8R]] of $G$, and write $X\phi$ for the action of $X \in \mathfrak{g}$ on $\phi \in V$.
Consider the [[gauge theory|2GKJQNQMVN]] on $\R^{1,3}$ with a $\mathfrak{g}$-valued gauge field $A_\mu$ and a scalar field $\phi$ with values in $V$.
Its Lagrangian density is
$$\mathcal{L} = -\frac{1}{4} \abs{F_{\mu\nu}}^2 + \frac{1}{2} \abs{D_\mu \phi}^2 - U(\phi), \qquad D_\mu \phi = \partial_\mu \phi + A_\mu \phi,$$
where $U$ is a $G$-invariant potential.
Let $\phi_0 \in V$ be a minimum point of $U$ with stabilizer $H \ne G$, so that $G$ is [[spontaneously broken|3498FHKNFK]] to $H$, and write $\phi = \phi_0 + \chi$.
The *Higgs mechanism* is the following effect of this breaking on the quadratic part of $\mathcal{L}$ in the fields $(A, \chi)$.

1. The term $\frac12 \abs{A_\mu \phi_0}^2$ is a mass term for the gauge field, with mass form $M^2(X, Y) = \ip{X\phi_0}{Y\phi_0}$ on $\mathfrak{g}$.
   Its kernel is the Lie algebra $\mathfrak{h}$ of $H$.
   So the gauge fields with values in the orthogonal complement $\mathfrak{h}^\perp$ become massive, and those in $\mathfrak{h}$ stay massless.
2. The components of $\chi$ in the tangent space $\mathfrak{g}\phi_0$ of the orbit are the would-be Goldstone bosons.
   They can be set to $0$ by a gauge transformation (the unitary gauge).
   They do not appear as particles; each massive gauge field gains one polarization instead.
3. The remaining components of $\chi$, orthogonal to $\mathfrak{g}\phi_0$, are massive scalar fields, the Higgs bosons, with mass form the Hessian of $U$ at $\phi_0$.

## Remarks

Example: the abelian Higgs model, $G = U(1)$ acting on $V = \C$, with $D_\mu \phi = (\partial_\mu + ieA_\mu)\phi$ and $\mathcal{L} = -\frac14 F_{\mu\nu}F^{\mu\nu} + \abs{D_\mu\phi}^2 - \lambda(\abs{\phi}^2 - v^2)^2$.
In unitary gauge $\phi = v + h/\sqrt{2}$ with $h$ real, and $\abs{D_\mu\phi}^2 = \frac12 (\partial_\mu h)^2 + e^2 (v + h/\sqrt2)^2 A_\mu A^\mu$.
The quadratic terms give the photon the mass $m_A = \sqrt{2}\, e v$ and the field $h$ the mass $m_h = 2\sqrt{\lambda}\, v$, and the phase of $\phi$ has disappeared.

Non-example: if $U$ has its minimum at $\phi_0 = 0$, then $H = G$, the mass form $M^2$ is zero, and all gauge fields stay massless.

The count of fields is preserved: $\dim G - \dim H$ Goldstone modes disappear and the same number of gauge fields become massive.
In the electroweak theory, $G = SU(2) \times U(1)$, $V = \C^2$ and $H$ is a $U(1)$, so three gauge fields become massive, the $W^\pm$ and $Z$ bosons, and one Higgs boson remains.
