---
tag: VRZDAWNTCR
kind: definition
name: Sheaf cohomology in topology
msc: [55N30, 14F06]
defines: KB76923A1M
uses: [0CQHFPGJ45, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_cohomology
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $\mathrm{Sh}(X)$ be the category of [[sheaves|TB6TM6R4MD]] of [[abelian groups|082GHNPJ53]] on $X$.
The global sections functor $\Gamma(X, -) \colon \mathrm{Sh}(X) \to \mathrm{Ab}$, $F \mapsto F(X)$, is left exact, and $\mathrm{Sh}(X)$ has enough injective objects.
For a sheaf $F$, choose an [[injective resolution|ZW3W6FX4PW]] $0 \to F \to I^0 \to I^1 \to I^2 \to \cdots$ in $\mathrm{Sh}(X)$.
The *$q$-th cohomology group of $X$ with coefficients in $F$* is
$$H^q(X, F) = H^q\big(\Gamma(X, I^0) \to \Gamma(X, I^1) \to \Gamma(X, I^2) \to \cdots\big).$$
So $H^q(X, -)$ is the $q$-th right [[derived functor|NPMC3K6J2F]] of $\Gamma(X, -)$; it does not depend on the choice of resolution up to canonical isomorphism.

## Remarks

Always $H^0(X, F) = F(X)$, by left exactness of $\Gamma$.
A short exact sequence of sheaves gives a long exact sequence of cohomology groups.

Example: if $X$ is a single point, a sheaf is just an abelian group $A$, and $\Gamma$ is the identity functor, which is exact.
So $H^0(X, A) = A$ and $H^q(X, A) = 0$ for $q > 0$.

Non-example: the rule $U \mapsto$ (constant functions $U \to \Z$) is a presheaf but in general not a sheaf.
Two different constants on two disjoint open sets do not glue to a constant function on their union.
The definition needs a sheaf, here its sheafification, the sheaf of locally constant functions.

In practice one uses acyclic resolutions instead of injective ones: flasque, soft or fine resolutions compute the same groups.
If $X$ is paracompact, Hausdorff and locally contractible, then $H^q(X, \underline{A})$ for the constant sheaf $\underline{A}$ is isomorphic to singular cohomology $H^q(X; A)$.
