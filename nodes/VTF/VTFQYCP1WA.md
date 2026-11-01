---
tag: VTFQYCP1WA
kind: definition
name: Tensor algebra
msc: [15A72, 15A69, 16S10]
defines: P4J5JZDW0B
uses: [000AYPA9AJ, 0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_algebra
---

## Definition

Let $F$ be a field and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
For $k \ge 1$, let $T^k(V) = V \otimes \cdots \otimes V$ be the [[tensor product|0BF2DE2SYK]] of $k$ copies of $V$, and let $T^0(V) = F$.
The *tensor algebra* of $V$ is the vector space
$$T(V) = \bigoplus_{k \ge 0} T^k(V),$$
with the bilinear multiplication determined by
$$(v_1 \otimes \cdots \otimes v_k) \cdot (w_1 \otimes \cdots \otimes w_l) = v_1 \otimes \cdots \otimes v_k \otimes w_1 \otimes \cdots \otimes w_l$$
for $v_i, w_j \in V$, and with unit $1 \in T^0(V)$.

## Remarks

$T(V)$ is an associative unital algebra over $F$, graded by the degree $k$, and $V = T^1(V)$ sits inside it.
Universal property: for every associative unital $F$-algebra $A$ and every linear map $f \colon V \to A$, there is exactly one unital algebra homomorphism $\bar f \colon T(V) \to A$ with $\bar f(v) = f(v)$ for $v \in V$.
Example: if $V = F x$ has dimension $1$, then $T^k(V) = F x^{\otimes k}$, and $x^{\otimes k} \mapsto x^k$ is an isomorphism $T(V) \cong F[x]$; the check is that both products add degrees.
Non-example: for $V = F^2$ with basis $x, y$, the polynomial ring $F[x, y]$ is not $T(V)$, because $x \otimes y \ne y \otimes x$ in $T(V)$ while $xy = yx$ in $F[x, y]$.
If $V$ has a basis $(e_i)_{i \in I}$, then $T(V)$ is the free associative algebra on the set $I$.
The same construction works for a module over a commutative ring.
