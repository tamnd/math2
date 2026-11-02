---
tag: F4WDYPQ9VP
kind: statement
role: theorem
name: McKean–Singer formula
msc: [58J20, 58J35]
uses: [44GBFZ16SG, MT9P2X85V8, 327NP6S7H5, Z2CP530WDE, 45P2SEGGR1]
about: [44GBFZ16SG]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Statement

Let $M$ be a closed smooth manifold with a smooth positive density, and let $E$, $F$ be Hermitian vector bundles over $M$.
Let $P \colon C^\infty(M; E) \to C^\infty(M; F)$ be an [[elliptic differential operator|MT9P2X85V8]] of positive order with formal adjoint $P^*$.
Then for every $t > 0$ the operators $e^{-tP^*P}$ and $e^{-tPP^*}$ are [[trace class|Z2CP530WDE]], and
$$\operatorname{ind} P = \operatorname{tr} e^{-tP^*P} - \operatorname{tr} e^{-tPP^*},$$
where $\operatorname{ind} P$ is the [[analytic index|44GBFZ16SG]].

## Remarks

Idea of the proof: $P^*P$ and $PP^*$ have discrete spectra, with $\ker P^*P = \ker P$ and $\ker PP^* = \ker P^*$.
For $\lambda > 0$, $P$ maps the $\lambda$-eigenspace of $P^*P$ isomorphically onto the $\lambda$-eigenspace of $PP^*$, with inverse $\lambda^{-1} P^*$.
So all terms with $\lambda > 0$ cancel in the difference of the traces, and only $\dim \ker P - \dim \ker P^*$ remains.
The left side does not depend on $t$, so one may let $t \to 0^+$.
Then each trace is an integral of the [[heat kernel|327NP6S7H5]] on the diagonal, which has an asymptotic expansion in powers of $t$ with local coefficients.
Hence the index is the integral of a local density built from the coefficients of $P$, and the singular terms of the expansion cancel.
Example: for $P = d + d^*$ from even to odd forms, the formula reads $\chi(M) = \sum_k (-1)^k \operatorname{tr} e^{-t \Delta_k}$, where $\Delta_k$ is the Hodge Laplacian on $k$-forms.

## Explanations

### L1 human

The index counts solutions of $Pu = 0$ minus solutions of $P^*v = 0$.
The heat operators $e^{-tP^*P}$ and $e^{-tPP^*}$ weight every eigenvalue by $e^{-t\lambda}$.
All nonzero eigenvalues appear in pairs, one on each side, so they cancel, and only the zero modes, which give the index, survive.

### L2 human

The formula is the starting point of the heat equation proof of the index theorem.
For small $t$ the heat traces are given by the [[Minakshisundaram–Pleijel expansion|45P2SEGGR1]], so the index is the integral of the constant term of a local expansion.
The local index theorem identifies this constant term with a characteristic form, which proves the Atiyah–Singer theorem for Dirac operators.
