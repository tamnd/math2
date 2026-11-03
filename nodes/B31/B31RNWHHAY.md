---
tag: B31RNWHHAY
kind: statement
role: theorem
name: Serre–Swan theorem
msc: [19L99, 55R50, 13C10]
uses: [0TVJZYB6SH, 0S1FJ8VEX9, P4DZM975BV, WWX7H5W1RP, HQA9YHDSH5, K7A04ZBD92]
about: [P4DZM975BV, HQA9YHDSH5]
sources:
  - url: https://en.wikipedia.org/wiki/Serre%E2%80%93Swan_theorem
same_as:
  wikidata: Q7455422
  wikipedia: Serre–Swan theorem
---

## Statement

Let $X$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]], let $\mathbb{K}$ be $\R$ or $\C$, and let $C(X)$ be the ring of continuous functions $X \to \mathbb{K}$.
For a $\mathbb{K}$-[[vector bundle|P4DZM975BV]] $E$ of finite rank on $X$, let $\Gamma(E)$ be the $C(X)$-module of continuous [[sections|WWX7H5W1RP]] of $E$.
Then $\Gamma(E)$ is a [[finitely generated projective|HQA9YHDSH5]] $C(X)$-module.
The functor $E \mapsto \Gamma(E)$ is an [[equivalence of categories|K7A04ZBD92]] from $\mathbb{K}$-vector bundles of finite rank on $X$ to finitely generated projective $C(X)$-modules.

## Remarks

The key step is that every vector bundle $E$ on a compact Hausdorff space is a direct summand of a trivial bundle $X \times \mathbb{K}^N$.
One builds the embedding from finitely many local trivializations and a partition of unity, and takes the complement to be the orthogonal complement for a metric on the fibres.
Then $\Gamma(E)$ is a direct summand of $\Gamma(X \times \mathbb{K}^N) = C(X)^N$.
Conversely, an idempotent matrix $e \in M_N(C(X))$ gives the bundle whose fibre at $x$ is the image of $e(x)$.

Example: on the $2$-sphere, the tangent bundle corresponds to the module of continuous vector fields, which is projective but not free.
In K-theory the theorem gives $K^0(X) \cong K_0(C(X))$, linking [[topological K-theory|6XCFW7YGX8]] with algebraic K-theory of rings.

The compactness is used to embed $E$ in a trivial bundle of finite rank.
Jean-Pierre Serre proved the analogous algebraic statement in 1955: for a commutative ring $A$, vector bundles on the affine scheme $\mathrm{Spec}\, A$ correspond to finitely generated projective $A$-modules.
Richard Swan proved the topological version in 1962.

## Explanations

### L1 human

A vector bundle is a geometric object: a family of vector spaces over a space.
A projective module is an algebraic object: a module that is a direct summand of a free module.
The theorem says that over a compact space these are two descriptions of the same thing.
A bundle is replaced by its module of sections, and nothing is lost.

### L2 human

The theorem is the reason projective modules are thought of as vector bundles, and why algebraic K-theory of rings is modelled on topological K-theory.
Trivial bundles correspond to free modules, Whitney sums to direct sums, and tensor products of bundles to tensor products of modules.
Questions such as [[Serre's problem|7GG0XYHB0T]] on projective modules over polynomial rings come from this dictionary.
In operator algebras, the theorem motivates treating projective modules over a noncommutative C*-algebra as vector bundles over a "noncommutative space".
