---
tag: RAPF0XSNX9
kind: conjecture
name: Eigenstate thermalization hypothesis
msc: [82C10, 82B10, 81Q50]
uses: [TDGEGWHXCT, NKNSCK1JY2, 0NEGN5CRSC]
about: [TDGEGWHXCT]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenstate_thermalization_hypothesis
same_as:
  wikidata: Q17008931
  wikipedia: Eigenstate thermalization hypothesis
history:
  posed_by: J. M. Deutsch
  first_stated: "1991"
---

## Statement

Let $H$ be the Hamiltonian of an isolated quantum many-body system of size $N$ that is non-integrable (chaotic), with eigenvalues $E_n$ and orthonormal eigenvectors $\lvert E_n \rangle$.
Let $A$ be a local, or few-body, [[self-adjoint operator|0NEGN5CRSC]].
The eigenstate thermalization hypothesis concerns eigenstates in the bulk of the spectrum.
For them it asserts that
$$\langle E_m \rvert A \lvert E_n \rangle = \mathcal{A}(\bar E)\, \delta_{mn} + e^{-S(\bar E)/2} f_A(\bar E, \omega)\, R_{mn},$$
where $\bar E = (E_m + E_n)/2$ and $\omega = E_n - E_m$.
Here $\mathcal{A}$ and $f_A$ are smooth functions, and $S(E)$ is the thermodynamic entropy at energy $E$.
The numbers $R_{mn}$ behave like random variables of mean $0$ and variance $1$.
Moreover, $\mathcal{A}(E)$ equals the [[microcanonical ensemble|TDGEGWHXCT]] average of $A$ at energy $E$, up to corrections that vanish as $N \to \infty$.

## Remarks

The diagonal part implies that the long-time average of $\langle A \rangle$ in any initial state with a narrow energy distribution equals the microcanonical value.
The exponentially small off-diagonal part implies that the fluctuations around this average are small at most times.
So isolated quantum systems thermalize in the sense of local observables, without any appeal to the [[ergodic hypothesis|NKNSCK1JY2]] in phase space.
The hypothesis was proposed by Deutsch in 1991 and by Srednicki in 1994, and the matrix-element form above is due to Srednicki (1999).
It is not proved for any interacting many-body Hamiltonian of physical interest; numerical exact diagonalization supports it in many models.
It fails for integrable systems, which have extensive families of conserved quantities, and is expected to fail in many-body localized systems.

## Explanations

### L1 human

A cup of coffee left alone cools to room temperature, but quantum mechanics says an isolated system keeps its memory forever.
The hypothesis explains how both can be true.
It claims that each single energy eigenstate of a chaotic system already looks thermal when one inspects a small part of it.
So the system does not need to forget anything: a typical state just already looks like equilibrium locally.
