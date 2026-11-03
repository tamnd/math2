---
tag: DS53YCMNDZ
kind: definition
name: Einstein tensor
msc: [83C05, 53B30, 53C50]
defines: P13KTBC7MH
uses: [GH6CXWFNDJ, 4GTNM0WHDH, ZHX2VYQDZ3, TTXDZENFVB]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein_tensor
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] of dimension $n \ge 2$, with [[Ricci tensor|4GTNM0WHDH]] $\mathrm{Ric}$ and [[scalar curvature|ZHX2VYQDZ3]] $R = \tr_g \mathrm{Ric}$.
The *Einstein tensor* of $g$ is the symmetric $(0, 2)$-tensor field
$$G = \mathrm{Ric} - \tfrac12 R \, g, \qquad G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R \, g_{\mu\nu}.$$

## Remarks

By the contracted [[Bianchi identity|TTXDZENFVB]] $\nabla^\mu R_{\mu\nu} = \frac12 \nabla_\nu R$, the divergence vanishes: $\nabla^\mu G_{\mu\nu} = 0$.
Its trace is $\tr_g G = R - \frac n2 R = \frac{2 - n}{2} R$, so for $n = 4$ it is $-R$, and for $n \ge 3$ one recovers $\mathrm{Ric} = G - \frac{1}{n-2} (\tr_g G) \, g$.
Example: if $g$ is an Einstein metric, $\mathrm{Ric} = \lambda g$, then $R = n\lambda$ and $G = \lambda(1 - \frac n2) g$; for the round unit $3$-sphere, $\lambda = 2$ and $G = -g$.
Non-example: the Ricci tensor itself is not divergence-free in general; for $n \ge 3$ it is divergence-free exactly when $R$ is constant, by the contracted Bianchi identity.
In dimension $2$, $\mathrm{Ric} = \frac12 R \, g$ for every metric, so $G = 0$.
With $G$, the Einstein field equations read $G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$.
