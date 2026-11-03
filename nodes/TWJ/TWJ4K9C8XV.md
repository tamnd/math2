---
tag: TWJ4K9C8XV
kind: definition
name: Nambu–Goto action
msc: [81T30, "83E30", 53C80]
defines: W4GZMZ796R
uses: [BY4QYYS788, F45VQ47GPV, T0WAGV4KP4, MAJ3DH7MZS]
sources:
  - url: https://en.wikipedia.org/wiki/Nambu–Goto_action
---

## Definition

Let $(M, G)$ be a [[Lorentzian manifold|BY4QYYS788]] of dimension $D$, the spacetime.
Let $\Sigma$ be a two-dimensional [[smooth manifold|F45VQ47GPV]], possibly with boundary, with local coordinates $(\sigma^0, \sigma^1) = (\tau, \sigma)$.
A worldsheet is a smooth immersion $X \colon \Sigma \to M$ whose induced metric $h = X^* G$, with components $h_{ab} = G_{\mu\nu}(X) \, \partial_a X^\mu \, \partial_b X^\nu$, is Lorentzian at every point, that is, $\det(h_{ab}) < 0$.
Let $T > 0$ be a constant, the string tension.
The *Nambu–Goto action* of $X$ is
$$S_{\mathrm{NG}}(X) = -T \int_\Sigma \sqrt{-\det(h_{ab})} \; d\tau \, d\sigma.$$

## Remarks

The integrand is the area element of $h$, so $S_{\mathrm{NG}}$ is $-T$ times the area of the worldsheet, and it does not depend on the choice of coordinates on $\Sigma$.
In string theory one writes $T = \frac{1}{2\pi\alpha'}$, where $\alpha'$ is the Regge slope.
Its Euler–Lagrange equations say that the mean curvature vector of $X(\Sigma)$ in $M$ vanishes, the Lorentzian analogue of the equation of [[minimal surfaces|41X0YW2R9N]].

Example: in Minkowski space with $G = \operatorname{diag}(-1, 1, \dots, 1)$, a static straight string $X(\tau, \sigma) = (\tau, \sigma, 0, \dots, 0)$ with $0 \le \sigma \le L$.
Then $h = \operatorname{diag}(-1, 1)$, $\sqrt{-\det h} = 1$, and $S_{\mathrm{NG}} = -T L \int d\tau$.
This is the action $-E\int d\tau$ of a system at rest with energy $E = TL$: the string has energy $T$ per unit length.

Non-example: $X(\tau, \sigma) = (0, \tau, \sigma, 0, \dots, 0)$ has induced metric $h = \operatorname{diag}(1, 1)$, so $\det h > 0$ and the square root is not real.
This surface lies in a single instant of time and is not a worldsheet.

Classically the action is equivalent to the [[Polyakov action|HFEGZQB8SV]], which has an independent metric on $\Sigma$ and no square root.
