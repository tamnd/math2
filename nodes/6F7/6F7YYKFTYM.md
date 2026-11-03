---
tag: 6F7YYKFTYM
kind: statement
role: theorem
name: Kubo formula
msc: [82C10, 82C70]
uses: [WJ78KR1K35, HM2HHE3J51, 0NEGN5CRSC, G1P1A0N7NZ]
about: [WJ78KR1K35]
sources:
  - url: https://en.wikipedia.org/wiki/Kubo_formula
same_as:
  wikidata: Q114769
  wikipedia: Kubo formula
---

## Statement

Let $\mathcal{H}$ be a finite-dimensional [[Hilbert space|HM2HHE3J51]], and let $H$, $A$ and $B$ be [[self-adjoint operators|0NEGN5CRSC]] on $\mathcal{H}$.
Let $\rho_0$ be a state that commutes with $H$, for example the [[canonical ensemble|G1P1A0N7NZ]] state $e^{-\beta H}/\tr e^{-\beta H}$.
Write $\langle X \rangle_0 = \tr(\rho_0 X)$ and $X(t) = e^{itH/\hbar} X e^{-itH/\hbar}$.
Then the [[linear response function|WJ78KR1K35]] of $A$ to a perturbation $H \mapsto H - f(t) B$ is
$$\chi_{AB}(t) = \frac{i}{\hbar}\, \theta(t)\, \big\langle [A(t), B(0)] \big\rangle_0,$$
where $\theta(t) = 1$ for $t > 0$ and $\theta(t) = 0$ for $t \le 0$.

## Remarks

The proof works in the interaction picture.
Write $\rho_\varepsilon(t) = e^{-itH/\hbar} \tilde\rho(t) e^{itH/\hbar}$; then $i\hbar\,\partial_t \tilde\rho = -\varepsilon f(t) [B(t), \tilde\rho]$.
Integrating once and keeping the first order in $\varepsilon$ gives $\tilde\rho(t) = \rho_0 + \tfrac{i\varepsilon}{\hbar}\int_{-\infty}^t f(s) [B(s), \rho_0]\, ds + O(\varepsilon^2)$.
Taking the trace against $A(t)$ and using cyclicity gives $\tr([B(s), \rho_0] A(t)) = \langle [A(t), B(s)] \rangle_0$, and stationarity of $\rho_0$ replaces $(t, s)$ by $(t - s, 0)$.
Example: for $H = \tfrac{\hbar\Omega}{2}\sigma_z$, $A = B = \sigma_x$ and $\rho_0$ the ground state, the formula gives $\chi(t) = \tfrac{2}{\hbar}\theta(t)\sin(\Omega t)$.
Applied to the current operator and an electric field, it gives the Kubo formula for the electrical conductivity in terms of the current–current commutator.
For infinite systems the same formula holds formally; a rigorous version needs a thermodynamic limit and control of the dynamics.

## Explanations

### L1 human

The Kubo formula tells how a system in equilibrium answers a weak push.
The answer is written with quantities of the unpushed system only: how two of its observables fail to commute at different times.
So one never has to solve the pushed problem.
It is the basic tool for computing conductivities and susceptibilities from microscopic models.

### L2 human

The formula is first-order time-dependent perturbation theory written for density matrices.
Combined with the KMS property of the Gibbs state it gives the fluctuation–dissipation theorem.
Integrated in time, it gives the Green–Kubo relations, which express transport coefficients as integrals of equilibrium current correlations.
In many-body theory one computes the retarded commutator from imaginary-time Green functions and then continues analytically to real frequencies.
