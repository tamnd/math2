---
tag: A2YTPG6CQF
kind: definition
name: Homotopy limit
msc: [18N40, 55U35, 55P65]
defines: 1NDRD8BHFG
uses: [SDTZVZ6B4Q, SY38F954FE, CHS5AFJGWE, 1X0WKFQX8K, 48QQ7T98Z9, E2870TEDG7, HSV1J7BJXX, TZHF6ZM92S]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_colimit_and_limit
---

## Definition

Let $\mathcal{M}$ be a [[model category|SDTZVZ6B4Q]] and let $I$ be a small category.
Assume that the [[functor category|1X0WKFQX8K]] $\mathcal{M}^I$ carries the injective model structure.
In it, [[weak equivalences|E2870TEDG7]] and cofibrations are defined objectwise; it exists, for instance, when $\mathcal{M}$ is combinatorial.
The [[limit|CHS5AFJGWE]] functor $\lim \colon \mathcal{M}^I \to \mathcal{M}$ is right [[adjoint|TZHF6ZM92S]] to the constant diagram functor, which preserves cofibrations and trivial cofibrations, so $\lim$ is a right [[Quillen functor|SY38F954FE]].
The *homotopy limit* is its total right derived functor
$$\operatorname{holim} = \mathbf{R}\lim \colon \mathrm{Ho}(\mathcal{M}^I) \to \mathrm{Ho}(\mathcal{M}),$$
between the [[homotopy categories|48QQ7T98Z9]].
On a diagram $D$ it is computed as $\lim R D$, where $D \to RD$ is a weak equivalence to a [[fibrant|HSV1J7BJXX]] diagram in the injective model structure.

## Remarks

The homotopy limit sends objectwise weak equivalences of diagrams to weak equivalences, and it comes with a natural map $\lim D \to \operatorname{holim} D$.

Example: for a diagram $X \xrightarrow{f} Z \xleftarrow{g} Y$ of topological spaces, the homotopy limit is the homotopy pullback
$$X \times_Z Z^{[0,1]} \times_Z Y = \set{(x, \omega, y) : \omega \colon [0, 1] \to Z,\ \omega(0) = f(x),\ \omega(1) = g(y)}.$$
When $f$ or $g$ is a Serre fibration, the map from the ordinary pullback to the homotopy pullback is a weak equivalence.

Non-example: the ordinary limit is not homotopy invariant.
There is a map from the diagram $\set{0} \to \R \leftarrow \set{1}$ to the diagram $\set{0} \to \R \leftarrow \set{0}$ that is the identity on $\set{0}$, sends $1$ to $0$, and is $t \mapsto t^2 - t$ on $\R$.
It commutes with the maps of the diagrams and is a weak equivalence at each object.
The pullback of the first is empty and that of the second is a point, while both homotopy pullbacks are contractible path spaces.

For a diagram $D$ of Kan complexes there is an explicit model, the Bousfield–Kan formula $\operatorname{holim} D = \int_{i \in I} \mathrm{Map}(N(I/i), D(i))$, where $N(I/i)$ is the nerve of the over category.
Homotopy colimits are defined dually, as the left derived functor of the colimit, using the projective model structure.
