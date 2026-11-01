---
tag: WJS9TPSGVM
kind: definition
name: Local ring
msc: [13H99, 13B30]
defines: MZ02BKPHJA
uses: [0310REJJY8, 0PV74TR5FP, 0XVEZDE9J8]
sources:
  - url: https://en.wikipedia.org/wiki/Local_ring
---

## Definition

A *local ring* is a [[commutative ring|0310REJJY8]] $R$ that has exactly one [[maximal ideal|0PV74TR5FP]] $\mathfrak m$.
One writes $(R, \mathfrak m)$, or $(R, \mathfrak m, k)$ with the [[residue field|NJ3APQ8BHH]] $k = R/\mathfrak m$.

## Remarks

For a commutative ring $R$, the following are equivalent:

1. $R$ is local;
2. $R \ne 0$ and the set of non-[[units|0XVEZDE9J8]] of $R$ is an ideal;
3. $R \ne 0$ and, for every $a \in R$, $a$ or $1 - a$ is a unit.

In a local ring, the maximal ideal is exactly the set of non-units, because every non-unit lies in some maximal ideal.

Example: let $p$ be a prime and $\Z_{(p)}$ the ring of rationals $a/b$ with $p \nmid b$.
The element $a/b$ in lowest terms is a unit exactly when $p \nmid a$.
So the non-units are the elements of $p\Z_{(p)}$, which is an ideal, and $\Z_{(p)}$ is local.
Other examples are every field, the ring $\Z/p^n\Z$, the formal power series ring $k[\![x]\!]$ over a field $k$, and every [[localization at a prime ideal|X6JD4AG973]].

Non-example: $\Z$ is not local, because $2\Z$ and $3\Z$ are two different maximal ideals.
Equivalently, $3$ and $1 - 3 = -2$ are both non-units of $\Z$.
The zero ring is not local either, since it has no maximal ideal.

Some authors call a Noetherian local ring a local ring, and call the general case a quasi-local ring.
