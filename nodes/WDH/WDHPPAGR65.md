---
tag: WDHPPAGR65
kind: example
name: AKLT model
msc: [82B20, 82B10, 82D40]
instance_of: [PAEME5EQRM]
uses: [5QG15H8P5J, PAEME5EQRM, H578T160KS]
sources:
  - url: https://en.wikipedia.org/wiki/AKLT_model
same_as:
  wikidata: Q4652175
  wikipedia: AKLT model
---

## Example

Let $L \ge 3$ and consider a ring of $L$ spins $1$, with spin operators $\mathbf{S}_j$ on the factor $\C^3$ of $(\C^3)^{\otimes L}$ and $\mathbf{S}_{L+1} = \mathbf{S}_1$.
The *AKLT model* (Affleck, Kennedy, Lieb and Tasaki, 1987) has Hamiltonian
$$H = \sum_{j=1}^{L} \Big( \mathbf{S}_j \cdot \mathbf{S}_{j+1} + \tfrac13 \big(\mathbf{S}_j \cdot \mathbf{S}_{j+1}\big)^2 \Big).$$
It is a spin-$1$ [[quantum Heisenberg model|5QG15H8P5J]] with an added biquadratic term.
Check: for two spins $1$ with total spin $s \in \set{0, 1, 2}$, $\mathbf{S}_1 \cdot \mathbf{S}_2 = \tfrac12 s(s+1) - 2$ takes the values $-2, -1, 1$, so each bond term $x + x^2/3$ takes the values $-\tfrac23, -\tfrac23, \tfrac43$.
Hence each bond term equals $2 P_2 - \tfrac23$, where $P_2$ is the projection onto total spin $2$ of the pair, and $H \ge -\tfrac23 L$.

## Remarks

The bound $-\tfrac23 L$ is attained by the valence-bond solid state.
To build it, split each spin $1$ into two spins $\tfrac12$, join neighbouring halves into singlets, and project each site back onto spin $1$.
Each bond then carries total spin at most $1$, so $P_2$ annihilates it, and on the ring this state is the unique ground state.
It is a [[matrix product state|H578T160KS]] with bond dimension $2$.
The model has a spectral gap above the ground state that stays bounded away from $0$ as $L \to \infty$, and spin correlations decay exponentially, proportionally to $(-\tfrac13)^r$ at distance $r$.
On an open chain, the two unpaired spins $\tfrac12$ at the ends give four ground states, a sign of symmetry-protected topological order.

## Explanations

### L1 human

The AKLT model is a chain of spin-one particles chosen so that its lowest-energy state can be written down exactly.
Picture each spin one as two halves, and pair every half with a half on the neighbouring site.
This pattern of pairs is the ground state, and it has a finite energy gap and short-range correlations.
It gave the first rigorous example of the gapped behaviour that Haldane predicted for integer-spin chains.
