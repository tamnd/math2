---
tag: EW56H41PKJ
kind: definition
name: Eilenberg swindle
msc: [16D40, "16E20", 19A13]
defines: RSFYN75DCS
uses: [0NZ8JA25WK, 0DZ9DKAKZR, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Mazur_swindle
---

## Definition

Let $R$ be a ring, and let $P$ and $Q$ be left $R$-[[modules|0NZ8JA25WK]] such that $P \oplus Q \cong F$ for a [[free module|0DZ9DKAKZR]] $F$.
Let $F^{(\infty)} = F \oplus F \oplus \cdots$ be the direct sum of countably many copies of $F$.
The *Eilenberg swindle* is the chain of isomorphisms
$$P \oplus F^{(\infty)} \cong P \oplus (Q \oplus P) \oplus (Q \oplus P) \oplus \cdots \cong (P \oplus Q) \oplus (P \oplus Q) \oplus \cdots \cong F^{(\infty)},$$
obtained by regrouping the summands of a countable direct sum.
Its conclusion is that $P \oplus F^{(\infty)} \cong F^{(\infty)}$, where $F^{(\infty)}$ is free.

## Remarks

Example: every [[projective module|BFFA03GE3V]] $P$ is a direct summand of a free module $F$, so the swindle applies to it.
Take $R = \Z/6\Z$ and $P = 3\Z/6\Z$, $Q = 2\Z/6\Z$; then $P \oplus Q \cong R$, and the swindle gives $P \oplus R^{(\infty)} \cong R^{(\infty)}$, although $P$ itself is not free.

Non-example: the regrouping needs infinitely many summands.
With finitely many summands the argument breaks.
Indeed, for $R$ commutative and $P \ne 0$, the isomorphism $P \oplus R^n \cong R^n$ fails.
To see this, compare dimensions over the residue field at a prime where $P$ is nonzero.

For this reason the Grothendieck group $K_0(R)$ uses only finitely generated projective modules: with countably generated ones every class would vanish.
