---
tag: 8B0RRRW08V
kind: definition
name: Spin glass
msc: [82B44, 82D30, 60K35]
defines: EHPA4B5S5W
uses: [R0KGM32QN6, DG9F3W6MZM, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_glass
---

## Definition

Let $N \ge 2$, and let $\Sigma_N = \set{-1, +1}^N$ be the set of spin configurations $\sigma = (\sigma_1, \dots, \sigma_N)$.
A *spin glass model* on $\Sigma_N$ is given by:

1. a family $(J_{ij})_{1 \le i < j \le N}$ of independent real [[random variables|0PNRKMRC55]], the couplings, each of which takes positive and negative values with positive probability;
2. the random Hamiltonian $H_N(\sigma) = -\sum_{i < j} J_{ij} \sigma_i \sigma_j$;
3. for each inverse temperature $\beta \ge 0$ and each sample of the couplings, the [[Gibbs measure|DG9F3W6MZM]] $G_N(\sigma) = e^{-\beta H_N(\sigma)} / Z_N$ on $\Sigma_N$, where $Z_N = \sum_{\tau \in \Sigma_N} e^{-\beta H_N(\tau)}$.

The couplings are *quenched*: they are fixed before the thermal average over $\sigma$ is taken.
The main quantity is the quenched free energy $F_N(\beta) = \frac{1}{N} \mathbb{E} \log Z_N$, where $\mathbb{E}$ is the expectation over the couplings.

## Remarks

Example: the [[Sherrington–Kirkpatrick model|MMSZK6CYRX]] takes $J_{ij} = g_{ij} / \sqrt{N}$ with $g_{ij}$ independent standard Gaussian variables.
A Gaussian variable is positive and negative with probability $1/2$ each, so clause 1 holds.

Non-example: the ferromagnetic [[Ising model|R0KGM32QN6]] with all $J_{ij} = J > 0$ fails clause 1, since no coupling is ever negative.
Its ground states are the two constant configurations, and there is no frustration.

Many models restrict the couplings to the edges of a graph, as in the [[Edwards–Anderson model|S5F9QX7YSP]] on $\Z^d$; then $J_{ij} = 0$ for the other pairs.
