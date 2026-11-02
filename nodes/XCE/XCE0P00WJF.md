---
tag: XCE0P00WJF
kind: definition
name: Prime ring
msc: [16N60]
defines: Z9TJSZZYG1
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
$R$ is a *prime ring* if $R \ne 0$ and, for all $a, b \in R$, the condition $aRb = 0$ implies $a = 0$ or $b = 0$.
Here $aRb = \set{arb : r \in R}$.

## Remarks

Example: $M_n(k)$ over a field $k$ is prime.
If $a \ne 0$ and $b \ne 0$, choose entries $a_{ij} \ne 0$ and $b_{kl} \ne 0$; then $e_{jk} \in R$ and the $(i, l)$ entry of $a e_{jk} b$ is $a_{ij} b_{kl} \ne 0$.
Non-example: $k \times k$ is not prime, since $(1, 0)\, r\, (0, 1) = 0$ for every $r \in k \times k$.
Equivalent forms: the zero ideal is a [[prime ideal|E8K2MN5V1E]] of $R$; or, for two-sided ideals $A, B$ of $R$, $AB = 0$ implies $A = 0$ or $B = 0$.
A commutative ring is prime if and only if it is an integral domain.
Every [[primitive ring|8F6EHDVJ62]] is prime.
