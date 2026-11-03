---
tag: XVF577CHTM
kind: definition
name: Multiplicative decomposition of the deformation gradient
msc: [74C15, 74A05]
defines: S6XKB3012V
uses: [HTYRR2WDQ6, K8BBMTN0KV, E949EQWCHF, X121AYEY67]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
---

## Definition

Let $\varphi$ be a deformation of an elastic–plastic body with [[deformation gradient|HTYRR2WDQ6]] $F = \nabla \varphi$, so that $\det F > 0$ at every point.
Let $F^e$ and $F^p$ be invertible $3 \times 3$ matrix fields with positive determinant.
The factorization $F = F^e F^p$ at each material point is a *multiplicative decomposition* of $F$ if:

1. $F^p$, the *plastic part*, maps material line elements of the reference configuration to a local intermediate configuration that is free of stress. Its evolution is given by a plastic flow rule for $L^p = \dot F^p (F^p)^{-1}$, the plastic velocity gradient;
2. $F^e$, the *elastic part*, maps the intermediate configuration to the current one. The stress is given by an elastic law in terms of $F^e$ alone.

## Remarks

Example: let $F^p$ be the simple shear with rows $(1, \gamma, 0)$, $(0, 1, 0)$, $(0, 0, 1)$ and let $F^e = \operatorname{diag}(1 + e, 1, 1)$.
Then $F = F^e F^p$ has rows $(1 + e, (1 + e)\gamma, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, and $\det F^p = 1$ expresses that metal plasticity preserves volume.
Non-example: the polar decomposition $F = RU$ is also a product, but $U$ is not a plastic part, since the stress depends on $U$.
It is a purely kinematic split, not an elastic–plastic one.
The fields $F^e$ and $F^p$ are in general not gradients of any map, so the intermediate configuration exists only locally.
The split is unique only up to a rotation $Q$ of the intermediate configuration: $F^e Q^T$ and $Q F^p$ give the same $F$.
For small displacement gradients, $F^e = I + H^e$ and $F^p = I + H^p$ give $F \approx I + H^e + H^p$, the additive split of [[small strain theory|X121AYEY67]].
