---
tag: B5YGBYPDBM
kind: definition
name: Local thermodynamic equilibrium
msc: [80A17, 82C35]
defines: J027RJ924H
uses: [5EKTEE00FZ, H9F9CNPBSN, 41NHDR6MH6, KK46Q2YV1D]
sources:
  - url: https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics
---

## Definition

Let a continuous system occupy a region $\Omega$ during a time interval $I$.
The system is in *local thermodynamic equilibrium* if these conditions hold.

1. Around each point $x \in \Omega$ there are cells that are small against the lengths over which macroscopic quantities vary. Yet they contain enough particles for thermodynamics to apply.
2. At each time $t \in I$, each cell has the variables of an [[equilibrium|5EKTEE00FZ]] state. These are the specific internal energy $u(x,t)$, specific volume $v(x,t)$ and mass fractions $w_k(x,t)$. They also include the [[intensive|H9F9CNPBSN]] variables: [[temperature|KK46Q2YV1D]] $T(x,t)$, pressure $p(x,t)$ and chemical potentials $\mu_k(x,t)$.
3. These fields obey the equilibrium equations of state. The specific entropy $s(x,t)$ obeys the [[fundamental relation|41NHDR6MH6]] in the Gibbs form
$$T\,ds = du + p\,dv - \sum_k \mu_k\,dw_k$$
along the motion of each material element.

## Remarks

Example: heat conduction in a copper bar with ends at $300$ kelvin and $400$ kelvin.
The temperature changes over centimetres, while a cell of side $1\,\mu\mathrm{m}$ holds about $10^{11}$ atoms, so clauses 1 to 3 hold to high accuracy.
Non-example: a shock wave in a dilute gas, a few mean free paths thick, fails clause 1.
No cell is both small against the shock and large against the mean free path.
Here $\mu_k$ is the chemical potential per unit mass of component $k$.
