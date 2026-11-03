---
tag: EYARCVGB0V
kind: statement
role: theorem
name: Variational method
msc: [81Q10, 49R05]
uses: [0NEGN5CRSC, BMKATJ802A, 06WHP8SE98, VXDEQB46GV]
about: [VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Variational_method_(quantum_mechanics)
same_as:
  wikidata: Q164296
  wikipedia: Variational method (quantum mechanics)
---

## Statement

Let $H$ be a [[self-adjoint operator|0NEGN5CRSC]] on a complex Hilbert space $\mathcal{H}$ with domain $D(H)$, bounded below.
Let $E_0 = \inf \sigma(H)$ be the bottom of its [[spectrum|BMKATJ802A]].
Then for every nonzero $\psi \in D(H)$,
$$\frac{\ip{\psi}{H\psi}}{\ip{\psi}{\psi}} \ge E_0,$$
and $E_0$ is the infimum of this [[Rayleigh quotient|06WHP8SE98]] over all nonzero $\psi \in D(H)$.
Equality holds for some $\psi$ if and only if $E_0$ is an eigenvalue of $H$ and $\psi$ is an eigenvector for $E_0$.

## Remarks

By the spectral theorem, $\ip{\psi}{H\psi} = \int_{\sigma(H)} \lambda \, d\mu_\psi(\lambda)$, where $\mu_\psi$ is the spectral measure of $\psi$, of total mass $\norm{\psi}^2$.
Since $\lambda \ge E_0$ on $\sigma(H)$, the integral is at least $E_0 \norm{\psi}^2$, with equality exactly when $\mu_\psi$ is concentrated at $E_0$.
Vectors whose spectral measure is concentrated near $E_0$ make the quotient as close to $E_0$ as one likes.

Example: for the hydrogen atom $H = -\frac12 \Delta - \frac{1}{\abs{x}}$ on $L^2(\R^3)$, with $E_0 = -\frac12$, try the Gaussians $\psi_\alpha(x) = e^{-\alpha \abs{x}^2}$, $\alpha > 0$.
A computation gives the quotient $\frac{3\alpha}{2} - 2\sqrt{\frac{2\alpha}{\pi}}$, which is smallest at $\alpha = \frac{8}{9\pi}$, with value $-\frac{4}{3\pi} \approx -0.424$.
This is an upper bound for $E_0 = -0.5$, as the theorem says, and it is not sharp because the true ground state $e^{-\abs{x}}$ is not a Gaussian.

The [[min-max theorem|G11NE3AT6E]] extends the principle to the higher eigenvalues below the essential spectrum.
Restricting $\psi$ to a finite-dimensional subspace gives the [[Rayleigh–Ritz method|5YSP8TWD4Q]].

## Explanations

### L1 human

The lowest energy of a quantum system is never above the average energy of any state you can write down.
So guessing a trial wave function and computing its energy always gives an upper bound for the ground state energy.
A better guess gives a lower upper bound, closer to the truth; the exact ground state gives the exact value.

### L2 human

The method turns the eigenvalue problem into a minimisation problem.
In practice one chooses a family of trial functions with a few parameters and minimises the energy over the parameters.
The [[Hartree–Fock method|8Q0QS66M7V]] is the variational method with Slater determinants as trial functions, and the [[min-max theorem|G11NE3AT6E]] gives the excited levels in the same spirit.
The method only gives upper bounds; lower bounds need other tools, such as Temple's inequality.
