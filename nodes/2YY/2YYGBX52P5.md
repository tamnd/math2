---
tag: 2YYGBX52P5
kind: definition
name: Newman–Penrose formalism
msc: ["83C60", "53B30", "83C20"]
defines: TTZYRV72HN
uses: [D1SYF8F8RQ, WD15XKXW46, PCNPQ7YBDE, KH9BG71N36]
sources:
  - url: https://en.wikipedia.org/wiki/Newman%E2%80%93Penrose_formalism
---

## Definition

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|D1SYF8F8RQ]] with signature $(+,-,-,-)$, and let $\nabla$ be its [[Levi-Civita connection|PCNPQ7YBDE]].
A *null tetrad* on an open set $U \subseteq M$ is a [[frame field|KH9BG71N36]] $(l, n, m, \bar m)$ such that:

1. $l$ and $n$ are real vector fields, and $m$ is a complex vector field with complex conjugate $\bar m$.
2. All four vectors are null: $g(l,l) = g(n,n) = g(m,m) = 0$.
3. $g(l, n) = 1$ and $g(m, \bar m) = -1$, and all other products of two of them vanish.

Then $g_{ab} = l_a n_b + n_a l_b - m_a \bar m_b - \bar m_a m_b$.
The *Newman–Penrose formalism* describes the geometry on $U$ by the following components in a null tetrad.

- The directional derivatives $D = l^a \nabla_a$, $\Delta = n^a \nabla_a$, $\delta = m^a \nabla_a$ and $\bar\delta = \bar m^a \nabla_a$.
- The twelve complex *spin coefficients* $\kappa, \sigma, \rho, \tau, \nu, \lambda, \mu, \pi, \epsilon, \gamma, \alpha, \beta$, which are the components of $\nabla$ in the tetrad.
- The five complex *Weyl scalars* built from the [[Weyl tensor|WD15XKXW46]] $C_{abcd}$:
$$\Psi_0 = C_{abcd} l^a m^b l^c m^d, \quad \Psi_1 = C_{abcd} l^a n^b l^c m^d, \quad \Psi_2 = C_{abcd} l^a m^b \bar m^c n^d,$$
$$\Psi_3 = C_{abcd} l^a n^b \bar m^c n^d, \quad \Psi_4 = C_{abcd} n^a \bar m^b n^c \bar m^d.$$
- The components $\Phi_{ij}$, $0 \le i, j \le 2$, of the trace-free Ricci tensor, and $\Lambda = R/24$, where $R$ is the scalar curvature.

The Einstein equations and the Bianchi identities become first-order equations for these quantities, the *Newman–Penrose equations*.

## Remarks

Example: if $(e_0, e_1, e_2, e_3)$ is an orthonormal frame with $g(e_0, e_0) = 1$, then $l = (e_0 + e_1)/\sqrt{2}$, $n = (e_0 - e_1)/\sqrt{2}$, $m = (e_2 + i e_3)/\sqrt{2}$ is a null tetrad.
Check: $g(l, n) = \tfrac12 (1 + 1) = 1$, $g(l,l) = \tfrac12 (1 - 1) = 0$, $g(m, \bar m) = \tfrac12(-1 - 1) = -1$ and $g(m, m) = \tfrac12(-1 + 1) = 0$.
Non-example: the orthonormal frame $(e_0, e_1, e_2, e_3)$ itself is not a null tetrad, because $g(e_0, e_0) = 1 \ne 0$ violates clause 2.
The integral curves of $l$ are geodesics exactly when $\kappa = 0$, and they form a shear-free congruence when moreover $\sigma = 0$.
The vector $l$ is a principal null direction of the Weyl tensor exactly when $\Psi_0 = 0$, and a repeated one exactly when $\Psi_0 = \Psi_1 = 0$.
Up to a sign that depends on the convention, three spin coefficients are $\kappa = m^a D l_a$, $\sigma = m^a \delta l_a$ and $\rho = m^a \bar\delta l_a$.
Sign conventions for the spin coefficients and for $\Phi_{ij}$ differ between texts, and some authors use the signature $(-,+,+,+)$.

## Explanations

### L1 human

A null tetrad is a set of four reference directions, all of them light-like.
Writing every quantity in such a frame turns tensor equations into equations for complex numbers.
