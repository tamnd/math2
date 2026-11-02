---
tag: 2MTN8CQWME
kind: statement
role: theorem
name: Eberlein–Šmulian theorem
msc: [46B50]
uses: [06GZ956657, P6KHVSTPZV, 0R6EWFKRCF]
about: [P6KHVSTPZV, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Eberlein%E2%80%93%C5%A0mulian_theorem
same_as:
  wikidata: Q2226650
  wikipedia: Eberlein–Šmulian theorem
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$, with the [[weak topology|P6KHVSTPZV]] $\sigma(X, X^*)$, and let $A \subseteq X$.
Then $A$ is [[compact|0R6EWFKRCF]] in the weak topology if and only if the following holds.
Every sequence in $A$ has a subsequence that converges weakly to a point of $A$.

## Remarks

The weak topology of an infinite-dimensional space is not metrizable, so compactness and sequential compactness need not agree a priori.
The theorem says they agree for the weak topology of a Banach space.
For "compact implies sequentially compact", a sequence lies in a separable closed subspace $Y$.
On weakly compact subsets of $Y$ the weak topology is metrizable, because countably many functionals separate the points of $Y$.
The converse direction is harder.
One proof first shows that $A$ is bounded, then uses the [[Banach–Alaoglu theorem|1BXEJXQ2YT]] in $X^{**}$.
It then shows that the weak* closure of the image $J(A)$ under the [[canonical embedding|QKR3D65TTH]] $J$ lies in $J(X)$.
The same equivalences hold for relative compactness: the weak closure of $A$ is weakly compact exactly when every sequence in $A$ has a weakly convergent subsequence with limit in $X$.

Example: the closed unit ball of a [[reflexive space|NN8RWPC8WG]] is weakly compact, so every bounded sequence in a reflexive space has a weakly convergent subsequence.
The analogue fails for the weak* topology: the unit ball of $(\ell^\infty)^*$ is weak*-compact by Banach–Alaoglu, but the evaluations $\delta_n(x) = x_n$ have no weak* convergent subsequence.

## Explanations

### L1 human

In general topology, compactness is defined with open covers, while in metric spaces one can test it with sequences.
The weak topology of a Banach space is not given by a metric, yet the theorem says that sequences still suffice to test compactness.
This makes weak compactness much easier to handle in practice.

### L2 human

The theorem is used in analysis and partial differential equations whenever one extracts weakly convergent subsequences from bounded sequences in reflexive spaces such as $L^p$ for $1 < p < \infty$ or Sobolev spaces.
It also combines with [[James's theorem|G1VWNQSAK5]] and the [[Krein–Smulian theorem|NYVHMQJP3E]] in the theory of weakly compact sets.
