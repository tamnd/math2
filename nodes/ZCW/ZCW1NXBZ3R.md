---
tag: ZCW1NXBZ3R
kind: definition
name: Immersion
msc: [57R42, 58A05]
defines: 6RW68JGBHC
uses: [F45VQ47GPV, 6P9PXQDSEN, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Immersion_(mathematics)
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]], and let $f \colon M \to N$ be a [[smooth|0V33BNKZ9S]] map.
The map $f$ is an *immersion* if for every point $p \in M$ the [[differential|6P9PXQDSEN]] $df_p \colon T_pM \to T_{f(p)}N$ is injective.

## Remarks

Equivalently, the rank of $df_p$ equals $\dim M$ at every point $p$; in particular $\dim M \le \dim N$.
An immersion that is a homeomorphism onto its image, with the subspace topology, is a *smooth embedding*.
Example: $f \colon \R \to \R^2$, $f(t) = (\cos t, \sin t)$, is an immersion.
Its derivative $f'(t) = (-\sin t, \cos t)$ never vanishes, so $df_t$ is injective for every $t$.
It is not an embedding, because it is not injective.
Non-example: $g(t) = (t^2, t^3)$ is smooth and injective but is not an immersion.
Its derivative $g'(t) = (2t, 3t^2)$ vanishes at $t = 0$, where the image has a cusp.
By the constant rank theorem, near each point an immersion has the local form $(x_1, \dots, x_m) \mapsto (x_1, \dots, x_m, 0, \dots, 0)$ in suitable charts.
