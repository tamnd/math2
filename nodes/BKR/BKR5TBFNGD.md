---
tag: BKR5TBFNGD
kind: definition
name: Lattice model
msc: [82B20]
defines: PAEME5EQRM
uses: [00C0BR7D7H, 059TJN0NZ1, R0KGM32QN6, 39NMDCPCCV]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_model_(physics)
---

## Definition

A (classical) *lattice model* consists of the following data.

1. A countable set $L$ of sites, usually the vertex set of a [[graph|00C0BR7D7H]] such as $\Z^d$ with nearest-neighbour edges.
2. A finite set $S$ of single-site states (spin values); a configuration is a map $\sigma \colon L \to S$.
3. An interaction: for each finite set $A \subseteq L$, a function $\Phi_A \colon S^A \to \R$, such that $\Phi_A = 0$ unless the diameter of $A$ is at most some fixed range $R$.

For a finite set $\Lambda \subseteq L$, the energy of $\sigma \in S^\Lambda$ (with free boundary condition) is $H_\Lambda(\sigma) = \sum_{A \subseteq \Lambda} \Phi_A(\sigma|_A)$.
At inverse temperature $\beta \ge 0$, the finite-volume Gibbs distribution is the [[probability measure|059TJN0NZ1]] on $S^\Lambda$ given by
$$\mu_{\Lambda, \beta}(\sigma) = \frac{e^{-\beta H_\Lambda(\sigma)}}{Z_{\Lambda, \beta}}, \qquad Z_{\Lambda, \beta} = \sum_{\tau \in S^\Lambda} e^{-\beta H_\Lambda(\tau)}.$$

## Remarks

Example: the [[Ising model|R0KGM32QN6]] on $\Z^d$ has $S = \set{-1, +1}$, $\Phi_{\set{u,v}}(\sigma) = -J \sigma(u)\sigma(v)$ for neighbours $u, v$, $\Phi_{\set{v}}(\sigma) = -h \sigma(v)$, and $\Phi_A = 0$ otherwise.
All three clauses hold, with range $R = 1$.

Non-example: a fluid of [[hard spheres|39NMDCPCCV]] has particle positions in $\R^3$ rather than variables attached to the sites of a lattice, so clause 1 fails; it is a continuum model.

Variants allow an infinite or continuous spin space $S$ with a reference measure, as for the XY model.
Other variants allow interactions of infinite range that decay fast enough, or variables on edges instead of sites.
Fixing the spins outside $\Lambda$ to a configuration $\eta$ adds the terms with $A$ meeting both $\Lambda$ and its complement, and gives the Gibbs distribution with boundary condition $\eta$.
