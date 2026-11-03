---
tag: YRV3DKKCM8
kind: statement
role: theorem
name: Fluctuation–dissipation theorem
msc: [82C10, 82C05, 82B10]
uses: [WJ78KR1K35, G1P1A0N7NZ, ENWMTRJRND, HM2HHE3J51, 0NEGN5CRSC]
about: [WJ78KR1K35, ENWMTRJRND]
sources:
  - url: https://en.wikipedia.org/wiki/Fluctuation–dissipation_theorem
same_as:
  wikidata: Q1434158
  wikipedia: Fluctuation–dissipation theorem
---

## Statement

Let $\mathcal{H}$ be a finite-dimensional [[Hilbert space|HM2HHE3J51]], let $H$ and $A$ be [[self-adjoint operators|0NEGN5CRSC]] on $\mathcal{H}$, and let $\beta > 0$.
Let $\rho = e^{-\beta H} / \tr e^{-\beta H}$ be the [[canonical ensemble|G1P1A0N7NZ]] state, write $\langle X \rangle = \tr(\rho X)$, and let $A(t) = e^{itH/\hbar} A e^{-itH/\hbar}$.
The correlation spectrum $S$ is the Fourier transform of the [[correlation function|ENWMTRJRND]] $\langle A(t) A \rangle$.
Define it and the absorptive part $\chi''$ of the [[linear response function|WJ78KR1K35]] as the distributions in $\omega \in \R$
$$S(\omega) = \int_{-\infty}^{\infty} e^{i\omega t} \langle A(t) A \rangle \, dt, \qquad \chi''(\omega) = \frac{1}{2\hbar} \int_{-\infty}^{\infty} e^{i\omega t} \langle [A(t), A] \rangle \, dt.$$
Then
$$\chi''(\omega) = \frac{1}{2\hbar}\big(1 - e^{-\beta\hbar\omega}\big) S(\omega).$$

## Remarks

The proof uses the detailed balance identity $S(-\omega) = e^{-\beta\hbar\omega} S(\omega)$.
In an eigenbasis of $H$, $S$ is a sum of Dirac masses at the Bohr frequencies $(E_m - E_n)/\hbar$ with weights $\rho_n \abs{A_{nm}}^2$, and swapping $n$ and $m$ multiplies the weight by $e^{-\beta(E_m - E_n)}$.
Since $\langle A A(t) \rangle = \langle A(-t) A \rangle$, the commutator term gives $\chi''(\omega) = (S(\omega) - S(-\omega))/(2\hbar)$, which yields the claim.
The function $\chi''$ is the imaginary part of the Fourier transform of the response function $\chi(t) = \tfrac{i}{\hbar}\theta(t)\langle [A(t), A] \rangle$, and it measures the power absorbed from a periodic force.
In the classical limit $\beta\hbar\omega \to 0$ the identity becomes $S(\omega) = \tfrac{2 k_B T}{\omega} \chi''(\omega)$.
The classical time-domain form reads $\chi(t) = -\beta \tfrac{d}{dt} \langle A(t) A(0) \rangle$ for $t > 0$.
Johnson–Nyquist noise is an application: the voltage noise of a resistor at equilibrium has spectral density $4 k_B T R$ per unit frequency at low frequency.

## Explanations

### L1 human

A system at rest in thermal equilibrium still jiggles: its quantities fluctuate.
The same system, pushed gently, resists and turns some of the push into heat.
The theorem says that these two behaviours are tied by an exact formula.
So one can predict how a system answers a push by only watching how it fluctuates on its own.

### L2 human

The theorem is a consequence of the Kubo formula together with the thermal (KMS) property of the Gibbs state.
It contains the Einstein relation between diffusion and mobility as a special case.
It is used to compute absorption spectra and transport coefficients from equilibrium correlation functions, and conversely to infer fluctuation spectra from measured responses.
Away from equilibrium the identity fails in general, and its violation is used to define effective temperatures in glassy systems.
