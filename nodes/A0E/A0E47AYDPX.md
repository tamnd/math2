---
tag: A0E47AYDPX
kind: definition
name: Max-plus algebra
msc: [15A80, 14T10, 90C24]
defines: 64G0VSC5F4
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Tropical_semiring
---

## Definition

Let $\R_{\max} = \R \cup \set{-\infty}$.
For $a, b \in \R_{\max}$, define
$$a \oplus b = \max(a, b), \qquad a \otimes b = a + b,$$
with the conventions $\max(a, -\infty) = a$ and $a + (-\infty) = -\infty$.
The *max-plus semiring* is $(\R_{\max}, \oplus, \otimes)$.
The *max-plus algebra* is the algebra of vectors and [[matrices|0VD9ZSWWJG]] with entries in $\R_{\max}$, with the operations
$$(A \oplus B)_{ij} = a_{ij} \oplus b_{ij}, \qquad (A \otimes B)_{ij} = \bigoplus_{k} a_{ik} \otimes b_{kj} = \max_k (a_{ik} + b_{kj}).$$

## Remarks

$(\R_{\max}, \oplus, \otimes)$ is a commutative semiring with zero element $-\infty$ and unit element $0$.
It is idempotent: $a \oplus a = a$ for all $a$.
Example: $2 \oplus 7 = 7$, $2 \otimes 7 = 9$, and $2 \otimes (3 \oplus 7) = 9 = (2 \otimes 3) \oplus (2 \otimes 7)$, which checks distributivity in one case.
Non-example: $\R_{\max}$ is not a ring, since $5$ has no additive inverse: $\max(5, b) = -\infty$ has no solution $b$.
Let $A$ be an $n \times n$ matrix, with $a_{ij}$ the weight of an arc from $i$ to $j$.
Then $(A^{\otimes k})_{ij}$ is the largest weight of a path with $k$ arcs from $i$ to $j$.
The min-plus semiring $(\R \cup \set{+\infty}, \min, +)$ is isomorphic to it by $x \mapsto -x$.
