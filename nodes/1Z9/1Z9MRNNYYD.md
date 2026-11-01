---
tag: 1Z9MRNNYYD
kind: definition
name: Dedekind domain
msc: [13F05, 11R04]
defines: 7NPY2CN5KB
uses: [0QVD7WBFGN, 0670T59HGE, 0F2PTGX1A2, 0C3QBCR46M, 00MHHZ9SNE, 0PV74TR5FP, MWBDFS2KJ5, YB4JTB4WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_domain
---

## Definition

Let $R$ be an [[integral domain|0QVD7WBFGN]] that is not a field, and let $K$ be its [[field of fractions|0F2PTGX1A2]].
The ring $R$ is a *Dedekind domain* if:

1. $R$ is [[Noetherian|0670T59HGE]];
2. $R$ is integrally closed: every $x \in K$ that is a root of a [[monic polynomial|0C3QBCR46M]] with coefficients in $R$ lies in $R$;
3. every nonzero [[prime ideal|00MHHZ9SNE]] of $R$ is a [[maximal ideal|0PV74TR5FP]].

## Remarks

Example: $\Z$ is a Dedekind domain.
It is a principal ideal domain, hence Noetherian.
By the rational root test, a rational root of a monic integer polynomial is an integer.
Every nonzero prime ideal $(p)$ is maximal, since $\Z/(p)$ is a field.
More generally, the ring of integers of every [[number field|MWBDFS2KJ5]] is a Dedekind domain, for example $\Z[\sqrt{-5}]$, which is not a unique factorisation domain.
Non-example: $\Z[\sqrt{-3}]$ fails clause 2, since $\omega = (1 + \sqrt{-3})/2$ lies in its field of fractions, is a root of $x^2 - x + 1$, and is not in $\Z[\sqrt{-3}]$.
Another non-example: $k[x, y]$ for a field $k$ fails clause 3, since $(x)$ is a nonzero prime ideal contained in the larger ideal $(x, y)$.
For a Noetherian integral domain $R$ that is not a field, each of these conditions is equivalent to being Dedekind.
First: every nonzero proper ideal is a product of prime ideals, in a unique way up to order.
Second: every nonzero [[fractional ideal|YB4JTB4WJN]] of $R$ is invertible.
Some authors also count fields as Dedekind domains.
