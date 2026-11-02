---
tag: MPNGD4V271
kind: statement
role: theorem
name: Cartan–Serre finiteness theorem
msc: [32C35, 32L10]
uses: [HXSZA44J5J, DSJET02WPR, PQ6Q143ARJ, 0TVJZYB6SH, Z4AMJS5KA6, R7VKRV8AGQ]
about: [DSJET02WPR, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf_cohomology
---

## Statement

Let $X$ be a [[complex analytic space|HXSZA44J5J]] whose underlying topological space is [[compact|0TVJZYB6SH]], and let $\mathcal{F}$ be a [[coherent analytic sheaf|DSJET02WPR]] on $X$.
Then for every integer $q \ge 0$ the [[sheaf cohomology|PQ6Q143ARJ]] group $H^q(X, \mathcal{F})$ is a finite-dimensional complex vector space.

## Remarks

The proof uses two finite coverings of $X$ by open [[Stein spaces|Z4AMJS5KA6]], one relatively compact in the other.
By [[Cartan's theorem B|R7VKRV8AGQ]] both coverings compute $H^q(X, \mathcal{F})$ by Čech cochains, which form Fréchet spaces.
The restriction map from the larger covering to the smaller one is a compact operator that induces an isomorphism on cohomology.
A theorem of Schwartz on compact perturbations of surjective maps between Fréchet spaces then gives finite dimension.

Example: on the projective line $\mathbb{P}^1$ with $\mathcal{F} = \mathcal{O}$, one has $H^0 = \C$, the constants, and $H^1 = 0$.

Compactness is necessary.
On $X = \C$, the space $H^0(\C, \mathcal{O})$ of entire functions is infinite-dimensional, since it contains $1, z, z^2, \dots$.

## Explanations

### L1 human

On a compact complex space, the spaces of global holomorphic sections of a coherent sheaf, and the higher cohomology groups that measure obstructions, are all finite-dimensional.
So each of them is described by a single number, its dimension.
Compactness is what keeps these spaces small.

### L2 human

The theorem is the source of the numerical invariants of compact complex spaces, such as the dimensions of spaces of sections of line bundles and the arithmetic genus.
It makes the Euler characteristic $\sum_q (-1)^q \dim H^q(X, \mathcal{F})$ of a coherent sheaf well defined on a compact complex space, the quantity computed by the Riemann–Roch theorem.
