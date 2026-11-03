---
tag: PX8A96Q1HH
kind: definition
name: Bogoliubov theory of the weakly interacting Bose gas
msc: [82D50, 82D05, 82B10]
defines: ZSFHAVF721
uses: [W733NG6P3M, YYBRA846TR, 1TJ8TNH331, 4PZBRJ78X4]
sources:
  - url: https://en.wikipedia.org/wiki/Bogoliubov_transformation
---

## Definition

Consider $N$ bosons of mass $m$ in a cubic box of volume $V$ with periodic boundary conditions, with density $n = N/V$, in units with $\hbar = 1$.
Let $a_k^\dagger$ and $a_k$ be the creation and annihilation operators on [[Fock space|1TJ8TNH331]] for the plane wave of momentum $k$, and let $\varepsilon_k = k^2 / (2m)$.
Let the particles interact by a real even pair potential with Fourier transform $\hat v$, such that $\hat v(0) > 0$ and $\hat v(k) \ge 0$.
The Hamiltonian is
$$H = \sum_k \varepsilon_k a_k^\dagger a_k + \frac{1}{2V} \sum_{k, p, q} \hat v(q) \, a_{k+q}^\dagger a_{p-q}^\dagger a_p a_k.$$
The *Bogoliubov approximation* consists of three steps.

1. Replace $a_0$ and $a_0^\dagger$ by the number $\sqrt{N_0}$, where $N_0$ is the number of particles in the condensate.
2. Keep only the terms of order $0$ and $2$ in the operators $a_k$, $a_k^\dagger$ with $k \ne 0$, and use $N_0 = N - \sum_{k \ne 0} a_k^\dagger a_k$.
3. The result is the quadratic Hamiltonian
$$H_B = \frac{N^2 \hat v(0)}{2V} + \sum_{k \ne 0} \Big[ (\varepsilon_k + n \hat v(k)) a_k^\dagger a_k + \frac{n \hat v(k)}{2} \big( a_k^\dagger a_{-k}^\dagger + a_k a_{-k} \big) \Big].$$

The *Bogoliubov transformation* sets $b_k = u_k a_k + v_k a_{-k}^\dagger$ with real $u_k, v_k$ such that $u_k^2 - v_k^2 = 1$, chosen so that $H_B = E_0 + \sum_{k \ne 0} E(k) \, b_k^\dagger b_k$ for a constant $E_0$, where
$$E(k) = \sqrt{\varepsilon_k \big(\varepsilon_k + 2 n \hat v(k)\big)}.$$

## Remarks

The condition $u_k^2 - v_k^2 = 1$ makes the $b_k$ satisfy the canonical commutation relations $[b_k, b_{k'}^\dagger] = \delta_{k k'}$, so the $b_k$ describe independent bosonic quasiparticles.
Example: at small $k$, $E(k) \approx k \sqrt{n \hat v(0) / m}$, since $\varepsilon_k \cdot 2 n \hat v(0) = k^2 n \hat v(0) / m$.
So the excitations are phonons with speed of sound $c = \sqrt{n \hat v(0)/m}$, and at large $k$, $E(k) \approx \varepsilon_k + n \hat v(k)$ is the free particle energy shifted by a mean field.
For a continuous $\hat v$, the ratio $E(k)/k$ is positive, tends to $c$ as $k \to 0$ and grows at large $k$, so its infimum is positive, and Landau's criterion predicts [[superfluidity|4PZBRJ78X4]].
Non-example: for the ideal gas, $\hat v = 0$, the formula gives $E(k) = \varepsilon_k$, which is quadratic at small $k$ and gives no superfluidity by Landau's criterion.
If $\hat v(0) < 0$, the expression under the square root is negative for small $k$, and the approximation breaks down: an attractive gas is unstable.

## Explanations

### L1 human

The approximation treats the condensate as a fixed large number and keeps only the processes in which pairs of particles leave or enter it.
The new operators $b_k$ mix the destruction of a particle of momentum $k$ with the creation of one of momentum $-k$.
In terms of them the Hamiltonian becomes a sum of independent harmonic oscillators, one for each momentum.
