---
tag: ACQ7A58XY7
kind: statement
role: theorem
name: Sinai's factor theorem
msc: [37A35, 28D20]
uses: [QDDRDW9PXS, 556WBDAHNP, AZRPHS478B, D33JK3AXRZ, X1D1C7VH6P]
about: [D33JK3AXRZ, X1D1C7VH6P]
sources:
  - url: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
---

## Statement

Let $(X, \mathcal{B}, \mu)$ be a [[standard probability space|QDDRDW9PXS]] and let $T \colon X \to X$ be an invertible [[ergodic|AZRPHS478B]] [[measure-preserving transformation|556WBDAHNP]] with measurable inverse.
Assume that its [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] $h_\mu(T)$ is positive.
Let $B$ be a two-sided [[Bernoulli scheme|D33JK3AXRZ]] on a finite alphabet, acting on $(Y, \nu)$, with entropy $h(B) \le h_\mu(T)$.
Then $B$ is a factor of $T$: there is a measurable map $\varphi \colon X \to Y$ with $\mu(\varphi^{-1}C) = \nu(C)$ for every measurable $C \subseteq Y$ and $\varphi \circ T = B \circ \varphi$ almost everywhere.

## Remarks

A factor map can only lower entropy, so the hypothesis $h(B) \le h_\mu(T)$ is necessary.
Ergodicity is needed too.
Let $T$ be the disjoint union, with weight $1/2$ each, of a Bernoulli scheme $B'$ and an identity map, so that $h_\mu(T) = h(B')/2 > 0$.
Let $B$ be any Bernoulli scheme with at least two symbols of positive weight.
A factor map $\varphi$ onto $B$ satisfies $\varphi(x) = B(\varphi(x))$ on the identity part.
So it sends a set of measure $1/2$ into the fixed points of $B$, which form a null set.
So $T$ has no such factor, whatever the entropy of $B$.
The proof constructs the factor map as a limit of finite codings, using the Rokhlin lemma to build towers and the Shannon–McMillan–Breiman theorem to count typical names.
Example: an irrational rotation has entropy $0$, so the theorem says nothing about it.
Indeed it has no nontrivial Bernoulli factor, since every factor of a zero-entropy system has entropy $0$.
Example: every ergodic toral automorphism of positive entropy has Bernoulli factors of every entropy up to its own.

## Explanations

### L1 human

Any ergodic system with some randomness, measured by positive entropy, contains a perfectly random process inside it.
More precisely, by watching the system through a suitable lens one sees a sequence of independent die rolls.
The die can be any loaded die whose entropy does not exceed the entropy of the system.
So positive entropy always means genuine randomness of the coin-tossing kind.

### L2 human

It was a step toward the Ornstein isomorphism theorem, whose proof sharpens the same kind of coding argument from factor maps to isomorphisms.
It shows that positive entropy, a number defined by counting, forces a concrete structure: an independent process sitting inside the system.
