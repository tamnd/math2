---
tag: MS5PXY4D9Y
kind: definition
name: Unary algebra
msc: [08A60]
defines: XD10P9CJMD
uses: [0SJ3RX9TXA, Q2W26ZY10B, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Unary_operation
---

## Definition

Let $A$ be a [[set|0SJ3RX9TXA]] and let $I$ be an index set.
A *unary algebra* is a pair $(A, (f_i)_{i \in I})$, where each $f_i \colon A \to A$ is a [[unary operation|Q2W26ZY10B]] on $A$.
It is *mono-unary* when $I$ has exactly one element.
A *homomorphism* of unary algebras $(A, (f_i))$ and $(B, (g_i))$ with the same index set is a [[function|0EPAT51DXQ]] $h \colon A \to B$ with $h(f_i(a)) = g_i(h(a))$ for all $i \in I$ and $a \in A$.

## Remarks

Example: $(\Z, s)$ with $s(n) = n + 1$ is a mono-unary algebra, since $s$ maps $\Z$ to $\Z$.
The map $h \colon \Z \to \Z/2\Z$, $h(n) = n \bmod 2$, is a homomorphism to $(\Z/2\Z, t)$ with $t(x) = x + 1$, because $h(n + 1) = h(n) + 1$.

Non-example: $(\N, p)$ with the predecessor $p(n) = n - 1$ is not a unary algebra, since $p(0) = -1 \notin \N$; the predecessor is only a partial operation on $\N$.

A unary algebra $(A, (f_i)_{i \in I})$ is the same as an action of the free monoid $I^*$ on $A$: a word $i_1 i_2 \cdots i_k$ acts by $f_{i_k} \circ \cdots \circ f_{i_1}$ in one common convention.
