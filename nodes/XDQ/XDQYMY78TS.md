---
tag: XDQYMY78TS
kind: definition
name: Nagata ring
msc: [13F40, 13B22]
defines: 3S5TMBAKCA
uses: [0670T59HGE, 0QVD7WBFGN, 0F2PTGX1A2, G0V86SJBQW, 05QY1VEBYD, 0C1Y04SZ1W, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Nagata_ring
---

## Definition

Let $A$ be an [[integral domain|0QVD7WBFGN]] with [[field of fractions|0F2PTGX1A2]] $K$.
The domain $A$ is *N-2* if, for every [[finite extension|0C1Y04SZ1W]] $L$ of $K$, the [[integral closure|G0V86SJBQW]] of $A$ in $L$ is a [[finitely generated|05QY1VEBYD]] $A$-module.
An N-2 domain is also called *Japanese*.
A commutative ring $R$ is a *Nagata ring* if:

1. $R$ is a [[Noetherian ring|0670T59HGE]].
2. For every [[prime ideal|00MHHZ9SNE]] $\mathfrak{p}$ of $R$, the domain $R/\mathfrak{p}$ is N-2.

## Remarks

Example: $\Z$ is a Nagata ring.
It is Noetherian, and its quotients by primes are $\Z$ and the fields $\F_p$.
A field $F$ is N-2, because the integral closure of $F$ in a finite extension $L$ is $L$, an $F$-module of finite dimension.
The integral closure of $\Z$ in a number field $L$ is the ring of integers of $L$, a free $\Z$-module of rank $[L : \Q]$.

Non-example: there are one-dimensional Noetherian local domains whose integral closure in their own field of fractions is not a finitely generated module.
Such a domain fails clause 2 at the prime $\mathfrak{p} = 0$.

A theorem of Nagata says that a Noetherian ring $R$ is a Nagata ring if and only if every finitely generated $R$-algebra that is a domain is N-2.
Such rings are also called universally Japanese.
Older texts call Nagata rings pseudo-geometric rings.
