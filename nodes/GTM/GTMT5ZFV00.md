---
tag: GTMT5ZFV00
kind: definition
name: Submersion
msc: [57R35, 58A05]
defines: BMY55EW3RF
uses: [F45VQ47GPV, 6P9PXQDSEN, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Submersion_(mathematics)
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]], and let $f \colon M \to N$ be a [[smooth|0V33BNKZ9S]] map.
The map $f$ is a *submersion* if for every point $p \in M$ the [[differential|6P9PXQDSEN]] $df_p \colon T_pM \to T_{f(p)}N$ is surjective.

## Remarks

Equivalently, the rank of $df_p$ equals $\dim N$ at every point $p$; when $M$ is not empty this forces $\dim M \ge \dim N$.
A point $p$ where $df_p$ is surjective is a regular point, so a submersion is a smooth map all of whose points are regular.
Example: the projection $\pi \colon \R^3 \to \R^2$, $\pi(x, y, z) = (x, y)$, is a submersion.
Its differential at every point is the linear map $\pi$ itself, which is onto.
Non-example: $f \colon \R^2 \to \R$, $f(x, y) = x^2 + y^2$, is not a submersion.
At the origin $df_0 = 0$, which is not surjective onto $\R$.
By the constant rank theorem, near each point a submersion has the local form $(x_1, \dots, x_m) \mapsto (x_1, \dots, x_n)$ in suitable charts.
