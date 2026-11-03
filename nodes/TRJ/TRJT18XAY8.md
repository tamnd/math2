---
tag: TRJT18XAY8
kind: statement
role: fact
name: Fermi's golden rule
msc: [81Q15, 81U90]
uses: [VXDEQB46GV, 70PHYT7DCA, PNYD1NXC1M]
about: [70PHYT7DCA]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi%27s_golden_rule
same_as:
  wikidata: Q1073295
  wikipedia: Fermi's golden rule
---

## Statement

Let $H = H_0 + V$ be a [[Hamiltonian|VXDEQB46GV]], where $H_0$ is the unperturbed part and $V$ is a small time-independent perturbation.
Let $\psi_i$ be a unit eigenvector of $H_0$ with energy $E_i$.
Let the final states $\psi_f$ be eigenvectors of $H_0$ whose energies $E_f$ form a continuum with density of states $\rho(E)$ near $E_i$.
Let $\Delta E$ be the energy scale on which $\rho$ and the matrix elements vary.
Consider times long compared with $\hbar/\Delta E$ but short compared with the lifetime of $\psi_i$.
Then, to first order in $V$, the probability of a transition from $\psi_i$ into these final states grows linearly in time.
Its rate is
$$\Gamma_{i \to f} = \frac{2\pi}{\hbar} \abs{\ip{\psi_f}{V\psi_i}}^2 \rho(E_i).$$

## Remarks

First-order [[time-dependent perturbation theory|70PHYT7DCA]] gives the amplitude $-\frac{i}{\hbar}\int_0^t e^{i\omega s} \ip{\psi_f}{V\psi_i}\, ds$ with $\omega = (E_f - E_i)/\hbar$.
Hence the transition probability to one final state is
$$\abs{\ip{\psi_f}{V\psi_i}}^2 \, \frac{4 \sin^2(\omega t/2)}{\hbar^2 \omega^2}.$$
As a function of $\omega$, the factor $4\sin^2(\omega t/2)/\omega^2$ has integral $2\pi t$ and concentrates near $\omega = 0$ as $t$ grows, so it behaves like $2\pi t\, \delta(\omega) = 2\pi\hbar t\, \delta(E_f - E_i)$.
Summing over final states with the density $\rho$ gives a probability $\Gamma t$, which is the rule.

Example: the rule gives the rate at which an atom absorbs light from a broadband beam, and the rate of decay of a discrete state coupled to a continuum.
Without a continuum of final states the rule does not apply.
For a single discrete final state the probability oscillates in time instead of growing linearly, as in a [[two-state system|CBJNV2SW0V]].

## Explanations

### L1 human

An excited quantum system that can decay into a continuum of states does so at a steady rate.
The rule says that this rate is proportional to the square of the coupling between the initial and final states.
It is also proportional to the number of final states available at the same energy.
It is the standard way to compute decay rates and transition rates in atomic, nuclear and solid state physics.

### L2 human

The rule comes from the first term of the [[Dyson series|PNYD1NXC1M]] in the interaction picture.
It is an approximation, valid for weak coupling and intermediate times, not an exact theorem; a rigorous version is obtained in the weak-coupling (van Hove) limit.
Despite its name, the formula goes back to Dirac; Fermi called it a golden rule.
Its validity requires a smooth density of final states; near thresholds or band edges corrections are needed.
