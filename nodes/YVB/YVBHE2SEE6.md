---
tag: YVBHE2SEE6
kind: conjecture
name: Vaught conjecture
aliases: [vaughts-conjecture, vaught-conjecture]
msc: ["03C15", "03C45"]
topics: [6XEXRME4C1]
audience: research
uses: [655K8Y7VS8, MVCH6N9SNW, 01TQB88H4C, 0V2H5PGJ9B, ~ea319e25, ~630e3683, 0MN2MER9WN, ~51f2568c]
about: [655K8Y7VS8]
sources:
  - url: https://en.wikipedia.org/wiki/Vaught_conjecture
  - url: https://en.wikipedia.org/wiki/Vaught_conjecture
    locator: Original formulation
  - url: https://arxiv.org/abs/2610.15217
  - book: isbn:9780387987606
same_as:
  wikidata: Q7917378
  wikipedia: Vaught conjecture
history:
  posed_by: "Robert Vaught"
  first_stated: "1961"
---

## Statement

Let $T$ be a [[complete theory|655K8Y7VS8]] with infinite models in a countable first-order signature.
Let $I(T, \aleph_0)$ be the number of [[countable|01TQB88H4C]] [[models|MVCH6N9SNW]] of $T$ up to isomorphism.
The conjecture says that $I(T, \aleph_0)$ is at most [[$\aleph_0$|0V2H5PGJ9B]] or equal to $2^{\aleph_0}$.

## Remarks

The conjecture is open for first-order theories, as of November 2026.
By [[Morley's theorem on countable models|~630e3683]], $I(T, \aleph_0)$ is at most $\aleph_1$ or equal to $2^{\aleph_0}$.
So the conjecture holds under the [[continuum hypothesis|0MN2MER9WN]], and the open case is a theory with exactly $\aleph_1$ countable models when $\aleph_1 < 2^{\aleph_0}$.
A stronger form, equivalent to the original, says that a theory with uncountably many countable models has a perfect set of pairwise non-isomorphic ones.

All allowed values occur.
The theory of dense linear orders without endpoints has one countable model, and by [[Vaught's never-two theorem|~ea319e25]] the value $2$ never occurs.
[[Ehrenfeucht's theory|~51f2568c]] has $3$, and its variants have every finite number from $3$ on.
$\mathrm{ACF}_0$ has $\aleph_0$ countable models, one for each transcendence degree.
The theory of $(\Z, <)$ has $2^{\aleph_0}$.

The conjecture is proved for several classes of theories.
Leo Harrington, Michael Makkai and Saharon Shelah proved it for $\omega$-stable theories.
Laura Mayer proved it for o-minimal theories.

The analogous question for a sentence of the infinitary logic $L_{\omega_1 \omega}$ has a negative answer in a preprint of October 2026.
Ackerman, Freer and Knight construct an $L_{\omega_1 \omega}$ sentence with exactly $\aleph_1$ countable models and no perfect set of non-isomorphic models, with a proof checked in Lean.
This does not decide the first-order conjecture.
The [[topological Vaught conjecture|W1J18NVJYN]] is a version for orbits of Polish group actions.

## History

Vaught posed the question in 1961, in the form of a problem: can one prove, without the continuum hypothesis, that a complete theory has exactly $\aleph_1$ countable models?
Michael Morley proved the bound $\aleph_1$ or $2^{\aleph_0}$ in 1970.
Harrington, Makkai and Shelah published the $\omega$-stable case in 1984, and Mayer the o-minimal case in 1988.

## Explanations

### L1 human

A complete theory can have many non-isomorphic countable models.
The conjecture says that their number is never strictly between "countably many" and "as many as there are real numbers".
If the continuum hypothesis fails, there is a size in between, and the question is whether some theory has exactly that many countable models.

### L2 human

We sort the four examples above by the number of countable models.

1. One model: dense linear orders, by Cantor's theorem.
2. Three models: Ehrenfeucht's theory.
3. $\aleph_0$ models: $\mathrm{ACF}_0$, with transcendence degree as the invariant.
4. $2^{\aleph_0}$ models: the order of $\Z$, since each countable order $I$ gives a model $\Z \cdot I$.

The typical use of the conjecture is as a test of how well a class of theories is understood: a proof for the class requires a structure theory for its countable models.
A trap is to read Morley's theorem as a proof under the negation of the continuum hypothesis; the case of exactly $\aleph_1$ models stays open there.

### L3 human

The isomorphism relation on countable models of $T$ is the orbit relation of a continuous action of the symmetric group of $\N$ on a Polish space.
Morley's proof splits the models by their Scott sentences, using the perfect set property for analytic sets.
The conjecture asks for a perfect set of orbits whenever there are uncountably many.
