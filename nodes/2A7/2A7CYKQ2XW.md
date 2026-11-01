---
tag: 2A7CYKQ2XW
kind: definition
name: Integrally closed domain
msc: [13B22, 13G05]
defines: H20P600HQS
uses: [0QVD7WBFGN, 0F2PTGX1A2, 1EHN4KPSFS, G0V86SJBQW]
sources:
  - url: https://en.wikipedia.org/wiki/Integrally_closed_domain
---

## Definition

Let $A$ be an [[integral domain|0QVD7WBFGN]] with [[field of fractions|0F2PTGX1A2]] $K$.
The domain $A$ is *integrally closed* if every element of $K$ that is [[integral|1EHN4KPSFS]] over $A$ lies in $A$.
Equivalently, $A$ is equal to its [[integral closure|G0V86SJBQW]] in $K$.

## Remarks

Example: $\Z$ is integrally closed.
If $p/q$ in lowest terms is a root of $x^n + a_{n-1} x^{n-1} + \cdots + a_0$ with $a_i \in \Z$, then $p^n = -q(a_{n-1} p^{n-1} + \cdots + a_0 q^{n-1})$, so $q$ divides $p^n$, which forces $q = \pm 1$.
The same argument shows that every [[unique factorisation domain|0W4X9G6263]] is integrally closed.

Non-example: $\Z[\sqrt{-3}]$ is not integrally closed.
The element $(1 + \sqrt{-3})/2$ of its field of fractions is a root of $x^2 - x + 1$, but it is not in $\Z[\sqrt{-3}]$.

An integrally closed domain is also called a normal domain.
A domain is integrally closed if and only if all its localizations at prime ideals are integrally closed.
