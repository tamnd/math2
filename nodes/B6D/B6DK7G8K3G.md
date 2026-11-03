---
tag: B6DK7G8K3G
kind: statement
role: proposition
name: Euler relation for internal energy
msc: [80A10, 80A05]
uses: [F6JVQ12X43, SPY89W0RJ7, H9F9CNPBSN, 41NHDR6MH6, WVH4PVW64P, RBG5ZBM35Y, PAYJBE73G4]
about: [F6JVQ12X43]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_thermodynamic_relation
---

## Statement

Let a simple system have [[internal energy|F6JVQ12X43]] $U(S, V, N_1, \dots, N_r)$, a differentiable function of its [[entropy|SPY89W0RJ7]] $S$, volume $V$ and amounts of substance $N_1, \dots, N_r$.
Let $T = \partial U / \partial S$, $p = -\partial U / \partial V$ and $\mu_i = \partial U / \partial N_i$ be its temperature, pressure and [[chemical potentials|WVH4PVW64P]].
Suppose that $U$ is [[extensive|H9F9CNPBSN]], that is, $U(\lambda S, \lambda V, \lambda N_1, \dots, \lambda N_r) = \lambda \, U(S, V, N_1, \dots, N_r)$ for all $\lambda > 0$.
Then
$$U = TS - pV + \sum_{i=1}^{r} \mu_i N_i.$$

## Remarks

Differentiate the homogeneity identity with respect to $\lambda$ and set $\lambda = 1$; this is Euler's theorem on homogeneous functions of degree $1$.
The partial derivatives of $U$ are those of the [[fundamental relation|41NHDR6MH6]].
Two consequences: the [[Gibbs free energy|RBG5ZBM35Y]] is $G = U - TS + pV = \sum_i \mu_i N_i$, and the [[grand potential|PAYJBE73G4]] is $U - TS - \sum_i \mu_i N_i = -pV$.
Example: for a one-component system, $G = \mu N$, so the chemical potential is the Gibbs free energy per particle.
Extensivity is needed: it fails for small systems where surface energy matters and for systems with long-range forces, such as self-gravitating gases.

## Explanations

### L1 human

If one doubles a system by putting two copies side by side, its energy, entropy, volume and particle number all double.
This simple scaling fact pins down the energy completely in terms of the other quantities.
The energy is temperature times entropy, minus pressure times volume, plus chemical potential times particle number.

### L2 human

The Euler relation turns the differential form of the fundamental relation into an integrated form.
Differentiating it and subtracting the fundamental relation gives the Gibbs–Duhem equation.
It also explains why $\Omega = -pV$ for a homogeneous fluid, a fact used constantly in statistical mechanics.
