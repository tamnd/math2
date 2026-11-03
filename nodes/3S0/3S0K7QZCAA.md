---
tag: 3S0K7QZCAA
kind: example
name: Kitaev chain
msc: [82B20, 82D77, 82D55]
instance_of: [PAEME5EQRM]
uses: [PAEME5EQRM, PJZ35X5QHM, 94PEKQHHHT, 84DS4AGYNX]
sources:
  - url: https://en.wikipedia.org/wiki/Kitaev_chain
same_as:
  wikidata: Q130781668
  wikipedia: Kitaev chain
---

## Example

Let $N \ge 2$ and let $c_j, c_j^\dagger$, $j = 1, \dots, N$, be fermion annihilation and creation operators, satisfying $\set{c_i, c_j^\dagger} = \delta_{ij}$ and $\set{c_i, c_j} = 0$.
For real parameters $\mu$, $t$ and $\Delta$, the open *Kitaev chain* has Hamiltonian
$$H = \sum_{j=1}^{N} -\mu\, c_j^\dagger c_j + \sum_{j=1}^{N-1}\Big( -t\big(c_j^\dagger c_{j+1} + c_{j+1}^\dagger c_j\big) + \Delta\big(c_j c_{j+1} + c_{j+1}^\dagger c_j^\dagger\big) \Big).$$
Write each fermion through two Majorana operators, $c_j = \tfrac12(\gamma_{j,1} + i\gamma_{j,2})$, with $\gamma_{j,a}$ self-adjoint, $\gamma_{j,a}^2 = 1$, and distinct ones anticommuting.
Check at the special point $\mu = 0$, $t = \Delta > 0$: a direct computation gives
$$H = i t \sum_{j=1}^{N-1} \gamma_{j,2}\, \gamma_{j+1,1}.$$
The two operators $\gamma_{1,1}$ and $\gamma_{N,2}$ do not appear in $H$.
Each of them anticommutes with both factors of every term, so it commutes with every term and hence with $H$.

## Remarks

Each term $i\gamma_{j,2}\gamma_{j+1,1}$ has eigenvalues $\pm 1$, so at the special point the ground-state energy is $-(N-1)t$ and the ground state is two-fold degenerate.
The fermion $\tfrac12(\gamma_{1,1} + i\gamma_{N,2})$ is split between the two ends and costs zero energy: these are Majorana zero modes.
More generally, for $\Delta \ne 0$ the chain is in a topological phase when $\abs{\mu} < 2\abs{t}$ and in a trivial phase when $\abs{\mu} > 2\abs{t}$.
The end modes persist in the topological phase, with an energy splitting that decays exponentially in $N$.
Kitaev introduced the model in 2001 as a toy model of a topological superconducting wire, a simple instance of [[topological order|84DS4AGYNX]] in one dimension.
Through the [[Jordan–Wigner transformation|94PEKQHHHT]] it is equivalent to an XY spin chain in a field.
At $t = \Delta$ this is the [[transverse-field Ising chain|PJZ35X5QHM]], and the topological phase corresponds to its ordered phase.

## Explanations

### L1 human

The Kitaev chain is a line of sites that electrons can hop between, with a superconducting term that creates and removes pairs.
At a special choice of parameters, each electron splits into two halves, and the halves pair up across neighbouring sites.
One half at each end is left without a partner.
These unpaired halves together form a single state that costs no energy and is spread over both ends.
Local noise has a hard time disturbing such a state, which is why it is studied for quantum computing.
