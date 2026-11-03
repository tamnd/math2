---
tag: BKWBKNEAKA
kind: statement
role: theorem
name: Gibbs variational principle
msc: [82B05, 82B20, 37D35]
uses: [DG9F3W6MZM, 1SFZNN31JW, FPYQWE8X12, 059TJN0NZ1]
about: [DG9F3W6MZM]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_measure
---

## Statement

Let $S$ be a finite set, $\Omega = S^{\Z^d}$, and let $\Phi = (\Phi_A)$ be a translation-invariant interaction on $\Z^d$.
Assume $\Phi$ is absolutely summable: $\sum_{A \ni 0} \norm{\Phi_A}_\infty < \infty$.
Let $\Lambda_n = \set{-n, \dots, n}^d$ and $H_n(\sigma) = \sum_{A \subseteq \Lambda_n} \Phi_A(\sigma)$.
Let $\beta > 0$, and let the pressure be the [[thermodynamic limit|FPYQWE8X12]] $P(\beta) = \lim_{n} \abs{\Lambda_n}^{-1} \ln \sum_{\sigma \in S^{\Lambda_n}} e^{-\beta H_n(\sigma)}$.
For a translation-invariant [[probability measure|059TJN0NZ1]] $\mu$ on $\Omega$, define:

1. the mean entropy $s(\mu) = \lim_n -\abs{\Lambda_n}^{-1} \sum_{\sigma \in S^{\Lambda_n}} \mu(\sigma) \ln \mu(\sigma)$, where $\mu(\sigma)$ is the probability that the spins in $\Lambda_n$ equal $\sigma$;
2. the mean energy $e(\mu) = \int_\Omega \sum_{A \ni 0} \frac{\Phi_A}{\abs{A}} \, d\mu$.

Then $s(\mu) - \beta e(\mu) \le P(\beta)$ for every translation-invariant $\mu$.
Equality holds if and only if $\mu$ is a [[Gibbs measure|DG9F3W6MZM]] for $\beta \Phi$, that is, a solution of the DLR equations.

## Remarks

The limits defining $P$ and $s(\mu)$ exist, by subadditivity.
Proof idea: in finite volume, $\ln Z_n - \big( S_n(\nu) - \beta \langle H_n \rangle_\nu \big)$ is the Kullback–Leibler divergence of a measure $\nu$ from the Boltzmann distribution, so it is nonnegative.
Here $S_n$ is the [[Gibbs entropy|1SFZNN31JW]] with $k_B = 1$; dividing by $\abs{\Lambda_n}$ and letting $n \to \infty$ gives the inequality.
The converse, that equality forces the DLR equations, is the harder part, and uses a relative entropy argument conditional on the outside of a box.
Example: for $\Phi = 0$, $P(\beta) = \ln \abs{S}$, and the only maximizer of $s(\mu)$ is the product of uniform measures, which is the only Gibbs measure.

## Explanations

### L1 human

Nature balances two tendencies: lowering energy and increasing disorder.
At inverse temperature $\beta$ the quantity to maximize is entropy minus $\beta$ times energy.
The theorem says the translation-invariant states that win this contest are exactly the equilibrium (Gibbs) states.

### L2 human

The principle is the infinite-volume form of the [[Gibbs–Bogoliubov inequality|WR3RBEH4QQ]], and the pressure is the Legendre transform of the entropy as a function of the energy.
It connects to dynamics: for shifts, equilibrium states maximize $h_\mu + \int \varphi \, d\mu$, and the maximum is the topological pressure.
When several translation-invariant measures attain the maximum, the system has coexisting phases.
The principle is a standard route to proving properties of Gibbs measures through convex analysis.
