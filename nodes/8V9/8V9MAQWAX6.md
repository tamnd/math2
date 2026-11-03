---
tag: 8V9MAQWAX6
kind: definition
name: Fermi normal coordinates
msc: [83C10, 53B30, 53C50]
defines: APH28RGPZK
uses: [63ZKC7AFX2, RNRTS8WWNM, NX9NYGFTRV, KH9BG71N36, Y7Z0AGY1A7, RRHKMGNKG9]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi_coordinates
---

## Definition

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]] of signature $(-, +, +, +)$, in units where $c = 1$.
Let $\gamma \colon I \to M$ be a timelike curve parametrised by proper time $\tau$.
Let $e_0, \ldots, e_3$ be an orthonormal frame along $\gamma$, as in a [[frame field|KH9BG71N36]], with $e_0 = \dot\gamma$ and [[Fermi–Walker transported|NX9NYGFTRV]].
Define
$$\Phi(\tau, x^1, x^2, x^3) = \exp_{\gamma(\tau)}\big(x^1 e_1(\tau) + x^2 e_2(\tau) + x^3 e_3(\tau)\big),$$
where $\exp$ is the [[exponential map|Y7Z0AGY1A7]] of $g$.
For a compact subinterval of $I$ and small enough $\abs{x}$, $\Phi$ is a diffeomorphism onto a neighbourhood of the corresponding piece of $\gamma$.
The components $(x^0, x^1, x^2, x^3) = (\tau, x^1, x^2, x^3)$ of $\Phi^{-1}$ are the *Fermi normal coordinates* along $\gamma$.

## Remarks

Along $\gamma$, that is at $x^1 = x^2 = x^3 = 0$, one has $g_{\mu\nu} = \eta_{\mu\nu}$ with $\eta = \operatorname{diag}(-1, 1, 1, 1)$.
If $\gamma$ is a [[geodesic|RNRTS8WWNM]], then Fermi–Walker transport is parallel transport, and all Christoffel symbols vanish along $\gamma$.
Then near $\gamma$, $g_{00} = -1 - R_{0i0j} x^i x^j + O(\abs{x}^3)$, where $R_{0i0j}$ are frame components of the Riemann tensor on $\gamma$.
For a weak static field these are $\partial_i \partial_j \Phi_N$ for the Newtonian potential $\Phi_N$, and the term gives the tidal potential.
Example: in Minkowski space with a straight world line $\gamma(\tau) = (\tau, 0, 0, 0)$ and the constant frame $e_\mu = \partial_\mu$, $\Phi(\tau, x) = (\tau, x^1, x^2, x^3)$, so Fermi normal coordinates are the inertial coordinates.
Non-example: on an accelerated curve, a parallel transported frame does not qualify.
Its vector $e_0$ does not stay equal to $\dot\gamma$, so the construction does not apply.
For an accelerated curve, the Christoffel symbols along $\gamma$ do not all vanish; $g_{00} = -1 - 2 a_i x^i + O(\abs{x}^2)$, where $a_i$ are the frame components of the four-acceleration.
The construction is the analogue, along a curve, of [[normal coordinates|RRHKMGNKG9]], which are built from the exponential map at a single point.
