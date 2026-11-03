---
tag: 1VPYJ7R7DT
kind: statement
role: theorem
name: Jarzynski equality
msc: [82C05, 82C35, 82B30]
uses: [JXKY6C8JTA, S8H21RWQ86, 0WQNRCNY3M, 0RWMRTPC87]
about: [JXKY6C8JTA]
sources:
  - url: https://en.wikipedia.org/wiki/Jarzynski_equality
same_as:
  wikidata: Q864883
  wikipedia: Jarzynski equality
---

## Statement

Let a classical system have Hamiltonian $H_\lambda$ depending on a control parameter $\lambda$.
Let it be coupled to a heat bath at temperature $T$, and let $\beta = 1/(k_B T)$, where $k_B$ is the Boltzmann constant.
Let $F_\lambda = -k_B T \ln Z_\lambda$ be the [[Helmholtz free energy|JXKY6C8JTA]], where $Z_\lambda$ is the partition function of $H_\lambda$.
Let the system start in canonical equilibrium at $\lambda = A$.
Change $\lambda$ along a fixed protocol $\lambda(t)$, $0 \le t \le \tau$, from $\lambda(0) = A$ to $\lambda(\tau) = B$.
Assume the dynamics is either Hamiltonian, or Markovian with the canonical distribution of $H_\lambda$ stationary for each fixed $\lambda$.
Let $W$ be the [[work|S8H21RWQ86]] done on the system in one realisation, $W = \int_0^\tau \dot\lambda\, \partial_\lambda H_\lambda(x(t))\, dt$.
Then
$$\mathbb{E}\left[e^{-\beta W}\right] = e^{-\beta (F_B - F_A)},$$
where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]] over realisations.

## Remarks

For Hamiltonian dynamics the proof is a change of variables: $W = H_B(x(\tau)) - H_A(x(0))$, and Liouville's theorem turns $\mathbb{E}[e^{-\beta W}]$ into $Z_B / Z_A$.
The final state need not be in equilibrium, and the protocol can be arbitrarily fast.
By [[Jensen's inequality|0RWMRTPC87]], $e^{-\beta \mathbb{E}[W]} \le \mathbb{E}[e^{-\beta W}]$, so $\mathbb{E}[W] \ge F_B - F_A$, which is the second law for this process.
Example: a quasistatic process has $W = F_B - F_A$ in every realisation, and the equality is trivial.
Without the equilibrium initial state the result fails; it is an essential hypothesis.

## Explanations

### L1 human

Free energy differences are equilibrium quantities, normally measured by very slow processes.
The Jarzynski equality says that fast, irreversible processes also give them exactly, if one averages $e^{-\beta W}$ over many repetitions.
It is used to measure free energies of single molecules by pulling them quickly.

### L2 human

The average is dominated by rare realisations with small work, so many repetitions are needed when the process is far from quasistatic.
The equality was found by Christopher Jarzynski in 1997.
It is one of the fluctuation relations of stochastic thermodynamics, and it follows by integration from the Crooks fluctuation theorem.
