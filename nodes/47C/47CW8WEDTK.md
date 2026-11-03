---
tag: 47CW8WEDTK
kind: statement
role: proposition
name: Energy fluctuations in the canonical ensemble
msc: [82B05, 82B30, 82B03]
uses: [G1P1A0N7NZ, 0477R9PYAE, 0WQNRCNY3M]
about: [G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_ensemble
---

## Statement

Let $\Omega$ be a countable set of microstates with energy $H \colon \Omega \to \R$.
Assume $Z(\beta) = \sum_{\omega \in \Omega} e^{-\beta H(\omega)}$ is finite for all $\beta$ in an open interval $I \subseteq (0, \infty)$.
For $\beta \in I$, let $\langle \cdot \rangle_\beta$ be the [[expected value|0WQNRCNY3M]] under the [[canonical ensemble|G1P1A0N7NZ]] $e^{-\beta H} / Z(\beta)$.
Then $\ln Z$ is infinitely differentiable on $I$, and
$$\langle H \rangle_\beta = -\frac{d}{d\beta} \ln Z(\beta), \qquad \operatorname{Var}_\beta(H) = \frac{d^2}{d\beta^2} \ln Z(\beta) = -\frac{d \langle H \rangle_\beta}{d\beta}.$$
With $\beta = 1/(k_B T)$ and the heat capacity $C_V = d \langle H \rangle / dT$, this reads $\operatorname{Var}(H) = k_B T^2 C_V$.

## Remarks

Proof idea: $Z$ is a Laplace transform that converges on an open interval, so it can be differentiated term by term.
Then $Z'/Z = -\langle H \rangle$ and $Z''/Z = \langle H^2 \rangle$, which give $(\ln Z)'' = \langle H^2 \rangle - \langle H \rangle^2$.
Since a [[variance|0477R9PYAE]] is nonnegative, the heat capacity is nonnegative: $C_V \ge 0$.
Example: for $N$ independent two-level units with energies $0$ and $\varepsilon$, $\ln Z = N \ln (1 + e^{-\beta \varepsilon})$.
So both $\langle H \rangle$ and $\operatorname{Var}(H)$ are proportional to $N$, and the relative fluctuation $\sqrt{\operatorname{Var}(H)} / \langle H \rangle$ decays like $N^{-1/2}$.

## Explanations

### L1 human

In contact with a heat bath, the energy of a system wobbles around its mean.
The size of this wobble is tied to how much heat the system needs to warm up: a large heat capacity means large energy fluctuations.
For a large system the wobble is tiny compared with the mean energy, which is why thermodynamics treats energy as a sharp quantity.

### L2 human

This is the simplest fluctuation–response relation: a response coefficient, the heat capacity, equals a variance in equilibrium.
The smallness of relative fluctuations for large $N$ is the heuristic reason for the [[equivalence of ensembles|8N7VY25V0E]].
Similar computations in the grand canonical ensemble relate the variance of the particle number to the compressibility.
At a critical point the heat capacity per particle can diverge, and then energy fluctuations are anomalously large.
