---
tag: XPCTJTBSQ0
kind: definition
name: Unimodular group
msc: ["22D05", "28C10"]
defines: CXG6JZGMCK
uses: [AHV05ZBCYW, VY0HXD3GC4, 63TX60RTRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with [[modular function|63TX60RTRQ]] $\Delta \colon G \to (0, \infty)$.
The group $G$ is *unimodular* if $\Delta(g) = 1$ for every $g \in G$.
Equivalently, every left [[Haar measure|VY0HXD3GC4]] $\mu$ on $G$ is also right-invariant: $\mu(Ag) = \mu(A)$ for every $g \in G$ and every Borel set $A$.

## Remarks

Example: every compact group $K$ is unimodular.
The modular function is a continuous homomorphism, so $\Delta(K)$ is a compact subgroup of $(0, \infty)$.
The only compact subgroup of $(0, \infty)$ is $\set{1}$, so $\Delta \equiv 1$.

Non-example: the group of maps $x \mapsto ax + b$ with $a > 0$ and $b \in \R$ has modular function $\Delta(a, b) = 1/a$, which is not identically $1$.

Every abelian group is unimodular, since $Ag = gA$ for all $g$.
Every discrete group is unimodular, since counting measure is invariant on both sides.
On a unimodular group, $\int_G f(x^{-1}) \, d\mu(x) = \int_G f(x) \, d\mu(x)$ for every integrable $f$.
