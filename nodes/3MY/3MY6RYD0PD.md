---
tag: 3MY6RYD0PD
kind: definition
name: Ergodic hypothesis
msc: [37A60, 82B03]
defines: NKNSCK1JY2
uses: [0EDKGA2FAK, CPEC2NW2KF, AZRPHS478B]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodic_hypothesis
---

## Definition

Let $H \colon \R^{2n} \to \R$ be a smooth Hamiltonian and let $\varphi_t$ be the flow of the [[Hamiltonian system|0EDKGA2FAK]] of $H$ on the [[phase space|CPEC2NW2KF]] $\R^{2n}$.
Let $E$ be a regular value of $H$ such that the energy surface $\Sigma_E = H^{-1}(E)$ is compact.
The flow preserves $\Sigma_E$ and a finite measure $\mu_E$ on it, the Liouville (microcanonical) measure $\mu_E = d\sigma / \norm{\nabla H}$, where $\sigma$ is the surface measure.
Normalise $\mu_E$ to a probability measure.
The system satisfies the *ergodic hypothesis* on $\Sigma_E$ if for every $g \in L^1(\Sigma_E, \mu_E)$ and for $\mu_E$-almost every $x \in \Sigma_E$,
$$\lim_{T \to \infty} \frac{1}{T} \int_0^T g(\varphi_t(x)) \, dt = \int_{\Sigma_E} g \, d\mu_E .$$

## Remarks

By Birkhoff's ergodic theorem, this holds exactly when the flow on $\Sigma_E$ is [[ergodic|AZRPHS478B]] for $\mu_E$: every measurable invariant subset of $\Sigma_E$ has measure $0$ or $1$.
Example: for $H(q, p) = \tfrac12 (p^2 + q^2)$ on $\R^2$ and $E > 0$, the energy surface is a circle, the flow is a rotation at constant speed, and $\mu_E$ is the normalised arc length.
Every orbit runs once around the circle in time $2\pi$, so time averages equal the circle average and the hypothesis holds.
Non-example: for two uncoupled oscillators, $H = \tfrac12(p_1^2 + q_1^2) + \tfrac12(p_2^2 + q_2^2)$, each energy $h_1 = \tfrac12(p_1^2 + q_1^2)$ is conserved.
The set where $h_1 < E/2$ is then an invariant subset of $\Sigma_E$ of measure strictly between $0$ and $1$, so the hypothesis fails.

## Explanations

### L1 human

The definition makes precise the slogan "time average equals space average".
One fixes the total energy, follows a typical state forever, and compares the long-run average of a measured quantity with its average over all states of that energy.
