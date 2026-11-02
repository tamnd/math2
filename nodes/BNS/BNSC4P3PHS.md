---
tag: BNSC4P3PHS
kind: statement
role: theorem
name: Serre's vanishing theorem on affine schemes
msc: [14F06, 14A15]
uses: [B3V3XJ2W8G, KPKND0K7W6, PQ6Q143ARJ]
about: [PQ6Q143ARJ, B3V3XJ2W8G]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf_cohomology
---

## Statement

Let $X$ be an [[affine scheme|B3V3XJ2W8G]] and let $\mathcal{F}$ be a [[quasi-coherent sheaf|KPKND0K7W6]] on $X$.
Then the [[sheaf cohomology|PQ6Q143ARJ]] groups vanish in positive degrees:
$$H^i(X, \mathcal{F}) = 0 \quad \text{for all } i > 0.$$

## Remarks

The idea of the proof for $X = \operatorname{Spec} A$ with $A$ Noetherian: if $I$ is an injective $A$-module, the associated sheaf $\tilde{I}$ is flasque.
Resolve $\mathcal{F} = \tilde{M}$ by $\tilde{I}^\bullet$ for an injective resolution $M \to I^\bullet$; this is a flasque resolution, and taking global sections gives back the exact complex $I^\bullet$.
In general one uses that the Čech complex of a quasi-coherent sheaf for a cover by standard open sets $D(f_i)$ is exact in positive degrees.

Example: on a separated scheme $X$ with an affine open cover, the theorem shows that the cover is acyclic for quasi-coherent sheaves, so Čech cohomology of this cover computes $H^i(X, \mathcal{F})$.

The affine hypothesis is necessary: on $X = \mathbb{P}^1_k$, which is not affine, $H^1(X, \mathcal{O}(-2)) \cong k \ne 0$.
Conversely, Serre's criterion says that a Noetherian scheme $X$ is affine if $H^1(X, \mathcal{F}) = 0$ for every quasi-coherent sheaf $\mathcal{F}$, and it suffices to ask this for coherent ideal sheaves.

## Explanations

### L1 human

On an affine scheme, every quasi-coherent sheaf comes from a module, and global sections of a short exact sequence of such sheaves stay exact.
So there is never an obstruction to passing from local to global data, and all higher cohomology vanishes.
Affine schemes play for quasi-coherent sheaves the role that contractible open sets play in topology.

### L2 human

The theorem is the base of every computation of coherent cohomology: one covers a separated scheme by affine open sets and computes the Čech complex.
It gives the long exact sequence argument that a surjection of quasi-coherent sheaves on an affine scheme is surjective on global sections.
With Serre's converse criterion, it characterizes affine schemes cohomologically, in the same way as Cartan's Theorem B for Stein manifolds.
