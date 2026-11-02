---
tag: D5MMVPJ8M1
kind: definition
name: Endomorphism ring
msc: [16S50]
defines: AWSBZWWMG9
uses: [0894J980RK, 09VDS2W1E8, M8Q24XB0AF]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $M$ be a left [[$R$-module|09VDS2W1E8]].
An *endomorphism* of $M$ is a map $f \colon M \to M$ with $f(x + y) = f(x) + f(y)$ and $f(rx) = r f(x)$ for all $x, y \in M$ and $r \in R$.
The *endomorphism ring* $\End_R(M)$ is the set of endomorphisms of $M$ with the operations
$$(f + g)(x) = f(x) + g(x), \qquad (fg)(x) = f(g(x)).$$

## Remarks

$\End_R(M)$ is a ring with zero map as zero and the identity map $\id_M$ as unit element.
For an abelian group $A$, viewed as a $\Z$-module, one writes $\End(A) = \End_\Z(A)$.
Example: $\End_\Z(\Z/n\Z) \cong \Z/n\Z$.
The check: an endomorphism $f$ is determined by $f(1) = a$, since $f(k) = ka$, and every $a$ gives one; composition corresponds to multiplication of the values $a$.
Non-example: the map $x \mapsto x + 1$ on $\Z$ is not in $\End_\Z(\Z)$, since it does not preserve addition: it sends $0$ to $1$.
For a field $K$, choosing a basis gives $\End_K(K^n) \cong M_n(K)$.
For the ring $R$ as a left module over itself, $\End_R(R) \cong R^{\mathrm{op}}$, the [[opposite ring|M8Q24XB0AF]], through $f \mapsto f(1)$.
