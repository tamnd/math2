---
tag: 3Z7YMK2WDS
kind: definition
name: Excellent ring
msc: [13F40, "13E05"]
defines: YF7YFQ58QJ
uses: [0670T59HGE, 5WAFPTH09V, X6JD4AG973, KBN13NPYJQ, 63XXTF6B5M, FB45BHHA2J, 8SQK7RTB63, AC5TFFQT9M]
sources:
  - url: https://en.wikipedia.org/wiki/Excellent_ring
---

## Definition

Let $R$ be a [[Noetherian ring|0670T59HGE]].
A Noetherian ring $A$ is *regular* if $A_{\mathfrak{q}}$ is a [[regular local ring|63XXTF6B5M]] for every prime ideal $\mathfrak{q}$ of $A$.
An algebra $A$ over a field $\kappa$ is *geometrically regular* if $A \otimes_\kappa L$ is regular for every finite field extension $L$ of $\kappa$.
The ring $R$ is *excellent* if:

1. $R$ is [[universally catenary|5WAFPTH09V]].
2. $R$ is a G-ring: let $\mathfrak{p}$ be a prime ideal of $R$ and let $\widehat{R_{\mathfrak{p}}}$ be the [[completion|KBN13NPYJQ]] of the [[localization|X6JD4AG973]] $R_{\mathfrak{p}}$.
Then for every prime ideal $\mathfrak{q}$ of $R_{\mathfrak{p}}$ with residue field $\kappa(\mathfrak{q})$, the ring $\widehat{R_{\mathfrak{p}}} \otimes_{R_{\mathfrak{p}}} \kappa(\mathfrak{q})$ is geometrically regular over $\kappa(\mathfrak{q})$.
3. $R$ is J-2: let $S$ be a [[finitely generated|AC5TFFQT9M]] $R$-algebra.
Then the set of prime ideals $\mathfrak{q}$ of $S$ with $S_{\mathfrak{q}}$ regular is open in the [[spectrum|FB45BHHA2J]] of $S$ with the [[Zariski topology|8SQK7RTB63]].

## Remarks

Example: every field $k$ is excellent.
It is universally catenary because finitely generated $k$-algebras are catenary.
Clause 2 holds because the only prime of $k$ is $0$, the ring $k$ is its own completion, and $k \otimes_k k = k$ is geometrically regular over $k$.
The regular locus of a finitely generated $k$-algebra is open, which is clause 3.
More generally, $\Z$, every complete Noetherian local ring, and every Dedekind domain of characteristic $0$ are excellent.
Localizations and finitely generated algebras of excellent rings are excellent.

Non-example: there are Noetherian local domains whose completion has nonzero nilpotent elements.
Such a ring fails clause 2, because if a reduced Noetherian local ring is a G-ring, then its completion is reduced.

Some authors call a ring that satisfies only clauses 2 and 3 quasi-excellent.
