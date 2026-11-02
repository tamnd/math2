---
tag: 3HKREN3Y3F
kind: statement
role: theorem
name: Grothendieck–Riemann–Roch theorem
msc: [14C40, 19L10, 14C17]
uses: [Z5G47MQ99B, EXKGG9X6J0, 56RXEJ8Z6S, 5FDMY7PDYY, EBEF6PEK4N, PAD37GKDPD, 2YDB5089FR]
about: [EBEF6PEK4N, 2YDB5089FR]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck–Riemann–Roch_theorem
same_as:
  wikidata: Q1899432
  wikipedia: Grothendieck–Riemann–Roch theorem
---

## Statement

Let $k$ be a field and let $f \colon X \to Y$ be a [[projective morphism|Z5G47MQ99B]] of [[smooth|EXKGG9X6J0]] quasi-projective varieties over $k$.
Let $K_0(X)$ be the [[Grothendieck group|5FDMY7PDYY]] of [[coherent sheaves|56RXEJ8Z6S]] on $X$, and let $f_! \colon K_0(X) \to K_0(Y)$ be the map $[\mathcal{F}] \mapsto \sum_{i \ge 0} (-1)^i [R^i f_* \mathcal{F}]$.
Let $A^*(X)_\Q$ be the rational [[Chow ring|EBEF6PEK4N]], with proper pushforward $f_* \colon A^*(X)_\Q \to A^*(Y)_\Q$.
Let $\operatorname{ch} \colon K_0(X) \to A^*(X)_\Q$ be the Chern character, built from the [[Chern classes|PAD37GKDPD]], and let $\operatorname{td}$ be the [[Todd class|2YDB5089FR]] of a tangent bundle.
Then for every $x \in K_0(X)$,
$$\operatorname{ch}(f_! x) \, \operatorname{td}(T_Y) = f_*\big(\operatorname{ch}(x) \, \operatorname{td}(T_X)\big) \quad \text{in } A^*(Y)_\Q.$$

## Remarks

The idea of the proof: factor $f$ as a closed immersion $X \to \mathbb{P}^N_Y$ followed by the projection $\mathbb{P}^N_Y \to Y$.
For the projection, both sides are computed from the explicit structure of $K_0$ and of the Chow ring of a projective bundle.
For a closed immersion, one deforms to the normal bundle and reduces to the zero section of a vector bundle, where the Koszul complex gives the formula.

Example: for $Y = \operatorname{Spec} k$, $A^*(Y)_\Q = \Q$, $\operatorname{td}(T_Y) = 1$ and $\operatorname{ch}(f_! [\mathcal{F}]) = \chi(X, \mathcal{F})$.
So the theorem becomes the Hirzebruch–Riemann–Roch formula $\chi(X, \mathcal{F}) = \int_X \operatorname{ch}(\mathcal{F}) \operatorname{td}(T_X)$.

Without the Todd classes the formula is false: the Chern character alone does not commute with pushforward, as already the case $f \colon \mathbb{P}^1_k \to \operatorname{Spec} k$ with $\mathcal{F} = \mathcal{O}$ shows, where $\chi = 1$ but $f_* \operatorname{ch}(\mathcal{O}) = 0$.

## Explanations

### L1 human

Grothendieck–Riemann–Roch is a version of Riemann–Roch for families.
It does not compute one number, the Euler characteristic of a sheaf on one variety.
Instead it computes how the cohomology of a sheaf varies over a base, as a class on the base.
The correction factor is the Todd class, which measures the geometry of the varieties involved.

### L2 human

The theorem says that the Chern character, corrected by Todd classes, is compatible with pushforward: a commutative square between K-theory and the Chow ring.
It is used to compute Chern classes of Hodge bundles and other natural bundles on moduli spaces, such as Mumford's computation on the moduli space of curves.
The case of a point recovers the Hirzebruch–Riemann–Roch theorem, and the topological analogue is the Atiyah–Singer family index theorem.
