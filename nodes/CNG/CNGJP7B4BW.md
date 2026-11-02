---
tag: CNGJP7B4BW
kind: definition
name: Characteristic class
msc: [55R40, 57R20]
defines: 7HACJC0JE2
uses: [8E37E74XVP, 6N7BC70CX0, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_class
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]], let $R$ be an [[abelian group|082GHNPJ53]] and let $k \ge 0$ be an integer.
Write $H^k(X; R)$ for [[singular cohomology|6N7BC70CX0]] with coefficients in $R$.
A *characteristic class* of degree $k$ for principal $G$-bundles is a rule $c$ that assigns to each [[principal $G$-bundle|8E37E74XVP]] $P \to X$ a class $c(P) \in H^k(X; R)$, such that:

1. If $P \to X$ and $P' \to X$ are isomorphic, then $c(P) = c(P')$.
2. For every continuous map $f \colon Y \to X$, $c(f^* P) = f^* c(P)$, where $f^* P$ is the pullback bundle and $f^*$ on the right is the induced map in cohomology.

## Remarks

The same definition applies to real or complex vector bundles of a fixed rank, which correspond to principal $GL_n(\R)$- or $GL_n(\C)$-bundles.
Over CW complexes, characteristic classes of degree $k$ correspond bijectively to elements of $H^k(BG; R)$: the class $u$ gives $c(P) = f_P^* u$, where $f_P \colon X \to BG$ classifies $P$.

Example: for real line bundles, the first Stiefel–Whitney class $w_1 \in H^1(X; \Z/2\Z)$ is a characteristic class.
For the Möbius line bundle $M$ over $S^1$, $w_1(M)$ is the generator of $H^1(S^1; \Z/2\Z)$, while $w_1$ of the trivial bundle is $0$.

Non-example: for line bundles over spaces $X$, the rule $c(P) = 1 \in H^0(X; \Z)$ if $X$ is compact and $c(P) = 0$ otherwise fails clause 2.
For the inclusion $f \colon [0, 1] \to \R$ and the trivial bundle $P$ over $\R$, $c(f^* P) = 1$ but $f^* c(P) = 0$.

Clause 2 implies that a trivial bundle $X \times G$ has $c(X \times G) = 0$ when $k > 0$, since it is pulled back from a point.
