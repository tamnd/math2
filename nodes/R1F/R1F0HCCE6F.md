---
tag: R1F0HCCE6F
kind: definition
name: Derivation
msc: [13N15, 12H05, 16W25]
defines: 3J89REV9WQ
uses: [0GYGHKX834, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Derivation_(differential_algebra)
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $A$ be an associative algebra over $R$.
A *derivation* of $A$ over $R$ is a map $D \colon A \to A$ such that:

1. $D$ is $R$-[[linear|0RJF668P1T]]: $D(a + b) = D(a) + D(b)$ and $D(ra) = r D(a)$ for all $a, b \in A$ and $r \in R$.
2. $D(ab) = D(a) b + a D(b)$ for all $a, b \in A$ (the Leibniz rule).

## Remarks

Example: let $k$ be a field and $A = k[X]$, and let $D$ be the formal derivative, $D(\sum_i c_i X^i) = \sum_i i c_i X^{i-1}$.
It is $k$-linear, and on monomials $D(X^i X^j) = (i + j) X^{i+j-1} = i X^{i-1} X^j + X^i \cdot j X^{j-1}$, which gives clause 2 by linearity.
Non-example: on $k[X]$ with $k$ of characteristic $0$, the second derivative $f \mapsto f''$ is linear but fails clause 2, since $(X \cdot X)'' = 2$ while $X'' \cdot X + X \cdot X'' = 0$.
Consequences: $D(1) = 0$, hence $D(r \cdot 1) = 0$ for all $r \in R$, and $D(a^n) = n a^{n-1} D(a)$ when $A$ is commutative.
If $D_1$ and $D_2$ are derivations, then $D_1 D_2 - D_2 D_1$ is a derivation.
More generally, for an $A$-bimodule $M$, a derivation $A \to M$ is an $R$-linear map with $D(ab) = D(a) b + a D(b)$.
A derivation of a ring $A$ without a chosen base ring is a derivation over $\Z$, that is, an additive map with the Leibniz rule.
