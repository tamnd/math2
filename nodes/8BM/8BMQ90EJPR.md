---
tag: 8BMQ90EJPR
kind: statement
role: theorem
name: Leray spectral sequence
msc: [55T05, 18G40, 55N30]
uses: [KB76923A1M]
about: [KB76923A1M]
sources:
  - url: https://en.wikipedia.org/wiki/Leray_spectral_sequence
same_as:
  wikidata: Q6528749
  wikipedia: Leray spectral sequence
---

## Statement

Let $f \colon X \to Y$ be a continuous map of topological spaces and let $\mathcal{F}$ be a sheaf of abelian groups on $X$.
For $q \ge 0$, let $R^q f_* \mathcal{F}$ be the $q$-th higher direct image, that is, the $q$-th right derived functor of the direct image $f_*$.
It is the sheaf on $Y$ associated with the presheaf $V \mapsto H^q(f^{-1}(V); \mathcal{F})$.
Then there is a first-quadrant spectral sequence with
$$E_2^{p,q} = H^p(Y; R^q f_* \mathcal{F}) \Longrightarrow H^{p+q}(X; \mathcal{F}),$$
where $H^*$ denotes [[sheaf cohomology|KB76923A1M]], and the differentials are $d_r \colon E_r^{p,q} \to E_r^{p+r, q-r+1}$.

## Remarks

Since $\Gamma(Y, f_* \mathcal{F}) = \Gamma(X, \mathcal{F})$ and $f_*$ sends injective sheaves to flasque sheaves, which are acyclic for $\Gamma(Y, -)$, this is the Grothendieck spectral sequence of the composite functor $\Gamma(Y, -) \circ f_*$.

Example: if $R^q f_* \mathcal{F} = 0$ for all $q > 0$, the spectral sequence collapses and $H^p(X; \mathcal{F}) \cong H^p(Y; f_* \mathcal{F})$ for all $p$.
This applies when $f$ is the inclusion of a closed subspace, because then $f_*$ is exact.

Let $f$ be a fibre bundle with fibre $F$ over a nice base, and let $\mathcal{F}$ be a constant sheaf.
Then $R^q f_* \mathcal{F}$ is locally constant with stalks $H^q(F)$, and one recovers a form of the Serre spectral sequence.

## Explanations

### L1 human

The Leray spectral sequence computes the cohomology of a space $X$ by looking at it through a map $f$ to another space $Y$.
Over each small open set of $Y$, one first computes the cohomology of the part of $X$ above it.
These local answers form sheaves on $Y$, and the cohomology of $Y$ with values in them leads to the cohomology of $X$.

### L2 human

Leray introduced sheaves and spectral sequences together for this purpose.
In algebraic geometry the same spectral sequence, for a morphism of schemes and étale or coherent cohomology, is a basic tool.
It is the prototype of the Grothendieck spectral sequence for a composite of derived functors.
