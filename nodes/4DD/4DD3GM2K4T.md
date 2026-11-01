---
tag: 4DD3GM2K4T
kind: definition
name: Local cohomology
msc: [13D45, 14B15]
defines: 6JB30BXDA2
uses: [0670T59HGE, 096Z9MP2ME, 0NZ8JA25WK, 85H7PRHDPZ, 4P7GBWJ4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Local_cohomology
---

## Definition

Let $R$ be a commutative [[Noetherian ring|0670T59HGE]], let $I$ be an [[ideal|096Z9MP2ME]] of $R$, and let $M$ be an [[$R$-module|0NZ8JA25WK]].
The *$I$-torsion functor* is
$$\Gamma_I(M) = \set{m \in M : I^n m = 0 \text{ for some } n \ge 1}.$$
It is a left exact functor from $R$-modules to $R$-modules.
For $i \ge 0$, the *$i$-th local cohomology module* $H^i_I(M)$ is the $i$-th right derived functor of $\Gamma_I$ at $M$.
Explicitly, choose an injective resolution $0 \to M \to E^0 \to E^1 \to \cdots$ by [[injective modules|85H7PRHDPZ]].
Then $H^i_I(M)$ is the $i$-th cohomology of the complex $0 \to \Gamma_I(E^0) \to \Gamma_I(E^1) \to \cdots$.

## Remarks

One has $H^0_I(M) = \Gamma_I(M)$, and a short exact sequence of modules gives a long exact sequence of local cohomology.
Equivalently, $H^i_I(M) \cong \varinjlim_n \operatorname{Ext}^i_R(R/I^n, M)$, a direct limit of [[Ext modules|4P7GBWJ4RR]].
If $I = (x_1, \ldots, x_n)$, then $H^i_I(M)$ is also the cohomology of the Čech complex $0 \to M \to \bigoplus_i M_{x_i} \to \bigoplus_{i<j} M_{x_i x_j} \to \cdots \to M_{x_1 \cdots x_n} \to 0$.
Example: for $R = K[x]$ and $I = (x)$, the Čech complex of $R$ is $0 \to R \to R_x \to 0$, so $H^0_I(R) = 0$ and $H^1_I(R) = K[x, x^{-1}]/K[x]$.
The functor $\Gamma_I$ is not right exact: for $0 \to K[x] \xrightarrow{x} K[x] \to K \to 0$ with $I = (x)$ one gets $0 \to 0 \to K$, and the last map is not onto.
If $(R, \mathfrak{m})$ is local and $M \ne 0$ is finitely generated, then $H^i_{\mathfrak{m}}(M) = 0$ for $i < \operatorname{depth} M$ and $i > \dim M$, and it is nonzero for $i = \operatorname{depth} M$ and $i = \dim M$.
