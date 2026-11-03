---
tag: RJWPXT4PC3
kind: statement
role: theorem
name: Projective bundle theorem
msc: ["19E08", "14C35"]
uses: [ND6XEY68P4, P4DZM975BV, ZT9A6JK8QF, Y2467453Q5]
about: [Y2467453Q5]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_bundle
---

## Statement

Let $X$ be a [[Noetherian scheme|ND6XEY68P4]].
Let $\mathcal{E}$ be a locally free sheaf of constant rank $r + 1$ on $X$, that is, a [[vector bundle|P4DZM975BV]] of rank $r + 1$.
Let $\pi \colon \mathbb{P}(\mathcal{E}) \to X$ be the associated projective bundle, whose fibres are [[projective spaces|ZT9A6JK8QF]] of dimension $r$, and let $\mathcal{O}(1)$ be its tautological invertible sheaf.
Let $K_n$ denote the [[algebraic K-groups|Y2467453Q5]] of the exact category of vector bundles.
Then for every $n \ge 0$ the map
$$K_n(X)^{r+1} \to K_n(\mathbb{P}(\mathcal{E})), \qquad (x_0, \ldots, x_r) \mapsto \sum_{i=0}^{r} [\mathcal{O}(-i)] \cdot \pi^* x_i$$
is an isomorphism.

## Remarks

For $n = 0$ the theorem says that $K_0(\mathbb{P}(\mathcal{E}))$ is a free $K_0(X)$-module with basis $1, [\mathcal{O}(-1)], \ldots, [\mathcal{O}(-r)]$.
Quillen proved the statement for all $n$.
His proof uses Castelnuovo–Mumford regularity: it gives functorial finite resolutions of vector bundles on $\mathbb{P}(\mathcal{E})$ whose terms are sums of sheaves $\mathcal{O}(-i) \otimes \pi^* \mathcal{F}_i$ with $0 \le i \le r$.

Example: for $X = \operatorname{Spec} k$ with $k$ a field, $K_0(\mathbb{P}^r_k) \cong \Z^{r+1}$.
As a ring it is $\Z[t]/(1 - t)^{r+1}$ with $t = [\mathcal{O}(-1)]$; the relation comes from the Koszul resolution of the empty intersection of $r + 1$ hyperplanes.

## Explanations

### L1 human

A projective bundle is a family of projective spaces, one over each point of a base space.
The theorem says that its K-theory is $r + 1$ copies of the K-theory of the base.
The copies are indexed by the twisting sheaves $\mathcal{O}(0), \mathcal{O}(-1), \ldots, \mathcal{O}(-r)$.
So passing to a projective bundle never creates K-theory that cannot be read off from the base.

### L2 human

The theorem is one of the basic computations of [[K-theory of schemes|Y2467453Q5]], with the localization sequence and homotopy invariance.
It parallels the projective bundle formula for Chow groups and for cohomology, where the powers of the first Chern class of $\mathcal{O}(1)$ play the role of the classes $[\mathcal{O}(-i)]$.
It is a key step in the proof of the [[Grothendieck–Riemann–Roch theorem|3HKREN3Y3F]], where a projective morphism is factored through a projective bundle.
