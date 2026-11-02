---
tag: SA5ZDFBHNZ
kind: definition
name: Einstein–Hilbert action
msc: [83C05, 49S05]
defines: JPE3A1SN7V
uses: [BY4QYYS788, ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein%E2%80%93Hilbert_action
---

## Definition

Let $M$ be a smooth oriented $4$-manifold, and let $g$ be a [[Lorentzian metric|BY4QYYS788]] on $M$ of signature $(-,+,+,+)$.
Let $R$ be the [[scalar curvature|ZHX2VYQDZ3]] of $g$, and let $\sqrt{-\det g}\; d^4x$ be its volume form in local coordinates $x^0, \dots, x^3$.
Let $G$ be Newton's gravitational constant, $c$ the speed of light, and $\kappa = 8\pi G / c^4$.
For a compact region $K \subseteq M$, the *Einstein–Hilbert action* of $g$ on $K$ is
$$S_{EH}[g] = \frac{1}{2\kappa} \int_K R \,\sqrt{-\det g}\; d^4x.$$

## Remarks

Let $g_t$ be a variation of the metric supported in the interior of $K$.
Write $\delta g^{\mu\nu} = \frac{d}{dt}\big|_{t=0} g_t^{\mu\nu}$.
Then
$$\frac{d}{dt}\Big|_{t=0} S_{EH}[g_t] = \frac{1}{2\kappa} \int_K \Big(R_{\mu\nu} - \tfrac12 R\, g_{\mu\nu}\Big)\, \delta g^{\mu\nu} \sqrt{-\det g}\; d^4x,$$
where $R_{\mu\nu}$ is the Ricci tensor; the term with the variation of $R_{\mu\nu}$ is a divergence and drops out.
So $g$ is a critical point of $S_{EH}$ for all such variations if and only if $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = 0$, the vacuum [[Einstein field equations|3MCZ97SW6V]].
Example: Minkowski space $\R^4$ with $g = -dt^2 + dx^2 + dy^2 + dz^2$ is flat, so its Ricci tensor vanishes, and it is a critical point.
Non-example: the Euclidean metric $dt^2 + dx^2 + dy^2 + dz^2$ is not Lorentzian, so the definition above does not apply to it; the analogous Riemannian functional $\int R \sqrt{\det g}\, d^4x$ is a different object.
With a cosmological constant $\Lambda$ one replaces $R$ by $R - 2\Lambda$.
Adding a matter action $S_M$ and setting $T_{\mu\nu} = -\frac{2}{\sqrt{-\det g}} \frac{\delta S_M}{\delta g^{\mu\nu}}$ gives $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \kappa T_{\mu\nu}$.
On a region with boundary, one adds the Gibbons–Hawking–York boundary term to obtain a well-posed variational problem with the metric fixed on the boundary.
