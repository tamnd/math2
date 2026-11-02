---
tag: HQTPVQS7TY
kind: definition
name: Comodule
msc: [16T15]
defines: 7WEM2E6RTV
uses: [A06RA8KB0T, 000AYPA9AJ, 0BF2DE2SYK, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Comodule
---

## Definition

Let $K$ be a field and let $(C, \Delta, \varepsilon)$ be a [[coalgebra|A06RA8KB0T]] over $K$.
A *right $C$-comodule* is a [[vector space|000AYPA9AJ]] $M$ over $K$ with a [[linear map|0NRYHJPQG2]] $\rho \colon M \to M \otimes C$, the coaction, such that:

1. $(\id_M \otimes \Delta) \circ \rho = (\rho \otimes \id_C) \circ \rho$ as maps $M \to M \otimes C \otimes C$.
2. $(\id_M \otimes \varepsilon) \circ \rho = \id_M$, where $M \otimes K$ is identified with $M$.

A *left $C$-comodule* is defined in the same way with a map $M \to C \otimes M$.

## Remarks

Example: $C$ is a right comodule over itself with $\rho = \Delta$; clauses 1 and 2 are coassociativity and the counit law.
Example: let $C = K[S]$ with $\Delta(s) = s \otimes s$ and $\varepsilon(s) = 1$, and let $M = \bigoplus_{s \in S} M_s$ be a vector space graded by $S$.
Then $\rho(m) = m \otimes s$ for $m \in M_s$ is a coaction: both sides of clause 1 give $m \otimes s \otimes s$, and clause 2 gives $\varepsilon(s) m = m$.
Every right $K[S]$-comodule arises in this way.
Non-example: for $M \ne 0$, the zero map $\rho = 0$ satisfies clause 1 but fails clause 2.
A morphism of comodules is a linear map $f \colon M \to N$ with $\rho_N \circ f = (f \otimes \id_C) \circ \rho_M$.
