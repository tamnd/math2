---
tag: ZEG3BKE4CE
kind: conjecture
name: Haldane conjecture
msc: [82B20, 82B10, 82D40]
uses: [5QG15H8P5J, WDHPPAGR65, Z0ZHN80F2B]
about: [5QG15H8P5J]
sources:
  - url: https://en.wikipedia.org/wiki/AKLT_model
history:
  posed_by: F. D. M. Haldane
  first_stated: "1983"
---

## Statement

Let $S \in \set{\tfrac12, 1, \tfrac32, 2, \dots}$ and $J > 0$, and let $H_L = J \sum_{j=1}^{L} \mathbf{S}_j \cdot \mathbf{S}_{j+1}$ be the antiferromagnetic spin-$S$ [[quantum Heisenberg model|5QG15H8P5J]] on a ring of $L$ sites.
The Haldane conjecture asserts:

1. if $S$ is an integer, the chain has a unique ground state, a uniform gap $\delta > 0$ for all large $L$, and exponentially decaying correlations;
2. if $S$ is a half-odd-integer, then the infinite chain has no spectral gap and its correlations decay as a power law.

## Remarks

For $S = \tfrac12$ the gapless behaviour follows from the Bethe ansatz solution.
For every half-odd-integer $S$, the [[Lieb–Schultz–Mattis theorem|Z0ZHN80F2B]] shows that the chain is either gapless or has a degenerate ground state, which is consistent with part 2.
For integer $S$ no proof is known, even for $S = 1$.
Numerical studies of the spin-$1$ chain give a gap of about $0.41 J$.
The [[AKLT model|WDHPPAGR65]] is a spin-$1$ chain with an added biquadratic term.
It provably has a unique ground state, a gap and exponentially decaying correlations, and it is believed to lie in the same phase as the spin-$1$ Heisenberg chain.
Haldane obtained the prediction from a mapping to the nonlinear sigma model with a topological term whose coefficient depends on whether $S$ is integer or half-odd-integer.

## Explanations

### L1 human

Chains of quantum spins behave very differently depending on whether each spin is a whole number or a half number.
Haldane predicted that whole-number spin chains have a minimum energy needed to excite them, and short-range order, while half-number chains can be excited with arbitrarily little energy.
This was a surprise in 1983, and experiments on spin-one chain materials later observed the gap.
A full mathematical proof for the Heisenberg chain is still missing.
