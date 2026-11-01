---
tag: KXTQ10RDSX
kind: definition
name: Reduced ring
msc: [13A99, 13A15]
defines: SZHY975FFX
uses: [0GYGHKX834, 0N9R5NN6TW]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_ring
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
$R$ is *reduced* if it has no nonzero [[nilpotent elements|0N9R5NN6TW]].
That is, for all $r \in R$ and all integers $n \ge 1$, if $r^n = 0$ then $r = 0$.

## Remarks

Example: $\Z/6\Z$ is reduced; if $r^n \equiv 0 \pmod 6$, then $2$ and $3$ divide $r$, so $r \equiv 0$.
Non-example: $\Z/4\Z$ is not reduced, since $2^2 = 0$ and $2 \ne 0$.
Equivalent forms: the [[nilradical|QQDN6EYQNJ]] of $R$ is zero; the zero ideal is a [[radical ideal|S4GQN5V54X]]; for all $r \in R$, $r^2 = 0$ implies $r = 0$.
Every [[integral domain|09S3PFBEPM]] is reduced, and so is every product of integral domains.
The same condition defines reduced rings that are not commutative.
