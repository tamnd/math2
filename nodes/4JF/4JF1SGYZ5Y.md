---
tag: 4JF1SGYZ5Y
kind: definition
name: Discrete valuation ring
msc: [13F30, 13H05, 13F10]
defines: MGM3CNJW9V
uses: [0CMD0BCH8T, 00MHHZ9SNE, 0QVD7WBFGN, 0F2PTGX1A2, A2KKZAV29W]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_valuation_ring
---

## Definition

A *discrete valuation ring* is a [[principal ideal domain|0CMD0BCH8T]] $R$ that has exactly one nonzero [[prime ideal|00MHHZ9SNE]].

## Remarks

Equivalently, $R$ is an [[integral domain|0QVD7WBFGN]] with [[field of fractions|0F2PTGX1A2]] $K$ such that there is a surjective [[discrete valuation|A2KKZAV29W]] $v \colon K^{\times} \to \Z$ with $R = \set{x \in K^{\times} : v(x) \ge 0} \cup \set{0}$.
A generator $\pi$ of the maximal ideal is a uniformizer; every nonzero $x \in K$ is $x = u \pi^{v(x)}$ with $u$ a unit of $R$.
The nonzero ideals of $R$ are exactly $(\pi^n)$ for $n \ge 0$.

Example: for a prime $p$, the ring $\Z_{(p)} = \set{a/b : a, b \in \Z,\ p \nmid b}$ is a discrete valuation ring.
Every nonzero element is $p^n u$ with $u$ a unit and $n \ge 0$, so every nonzero ideal is $(p^n)$, which is principal.
The only nonzero prime among these is $(p)$.
The ring $k[\![t]\!]$ of formal power series over a field $k$ and the ring $\Z_p$ of $p$-adic integers are other examples.

Non-example: $\Z$ is a principal ideal domain, but it has infinitely many nonzero prime ideals $(2), (3), (5), \ldots$, so it is not a discrete valuation ring.
A field is not a discrete valuation ring either: it has no nonzero prime ideal.
