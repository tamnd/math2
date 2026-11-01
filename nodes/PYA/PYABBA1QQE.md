---
tag: PYABBA1QQE
kind: definition
name: Universally catenary ring
msc: [13C15]
defines: 5WAFPTH09V
uses: [B2CYR292J6, 0670T59HGE, 0SDC934R52, AC5TFFQT9M]
sources:
  - url: https://en.wikipedia.org/wiki/Catenary_ring
---

## Definition

Let $R$ be a commutative [[Noetherian ring|0670T59HGE]].
The ring $R$ is *universally catenary* if every [[finitely generated|AC5TFFQT9M]] commutative $R$-algebra is [[catenary|B2CYR292J6]].

## Remarks

An equivalent condition is that the [[polynomial ring|0SDC934R52]] $R[X_1, \dots, X_n]$ is catenary for every $n \ge 0$.
This holds because every finitely generated $R$-algebra is a quotient of such a ring, and a quotient of a catenary ring is catenary.
Every Cohen–Macaulay ring is universally catenary; for example a field $k$ is, so $k[x, y]/(xy)$ is catenary.
Nagata gave a Noetherian local domain that is catenary but not universally catenary: it satisfies the condition for $n = 0$ and fails it for some polynomial ring over it.
