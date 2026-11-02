---
tag: EHDXZV05JR
kind: definition
name: Cohomology ring
msc: [55N45, 55N10]
defines: RDT4785M4D
uses: [JX47MS1R1H, 6N7BC70CX0, M0Q5CFJ7ZH, 8KB4SQGC0C, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomology_ring
---

## Definition

Let $X$ be a topological space and let $R$ be a [[commutative ring|0310REJJY8]] with $1$.
The *cohomology ring* of $X$ with coefficients in $R$ is the direct sum of the [[singular cohomology|6N7BC70CX0]] groups
$$H^\bullet(X; R) = \bigoplus_{k \ge 0} H^k(X; R).$$
Its multiplication extends the [[cup product|JX47MS1R1H]] $H^k \times H^l \to H^{k+l}$ bilinearly to all of $H^\bullet(X; R)$.

## Remarks

It is an associative [[graded ring|8KB4SQGC0C]] with unit, and an $R$-algebra.
It is graded commutative: $ab = (-1)^{kl} ba$ for $a \in H^k$ and $b \in H^l$.
A continuous map $f \colon X \to Y$ induces a ring homomorphism $f^* \colon H^\bullet(Y; R) \to H^\bullet(X; R)$.

Example: $H^\bullet(S^n; \Z) \cong \Z[x]/(x^2)$ with $x$ of degree $n \ge 1$, since $x^2$ would lie in $H^{2n}(S^n) = 0$.
For the complex projective space $\C P^n$, $H^\bullet(\C P^n; \Z) \cong \Z[x]/(x^{n+1})$ with $x$ of degree $2$.

Non-example: [[singular homology|M0Q5CFJ7ZH]] $H_\bullet(X)$ is a graded group of the same shape, but in general it carries no natural product of this kind.
The cup product needs the diagonal map $X \to X \times X$, which goes the wrong way for homology.
