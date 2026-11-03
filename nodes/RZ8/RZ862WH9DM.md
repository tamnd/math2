---
tag: RZ862WH9DM
kind: definition
name: Many-body localization
msc: [82C44, 82B44, 82C10]
defines: CS50E9MDK3
uses: [MXEZM0QJ1K, EY0X2NKA3S, MM0EJ2GDE4, 94PEKQHHHT]
sources:
  - url: https://en.wikipedia.org/wiki/Many-body_localization
---

## Definition

For each $L \ge 1$, let $\mathcal{H}_L = (\C^2)^{\otimes L}$ be the [[tensor product|EY0X2NKA3S]] Hilbert space of a chain of $L$ spins $\tfrac12$.
Let $H_L$ be a random Hamiltonian on $\mathcal{H}_L$ that is a sum of terms, each acting on boundedly many neighbouring sites.
The family $(H_L)$ is *fully many-body localized* if, with probability tending to $1$ as $L \to \infty$, there is a [[unitary operator|MM0EJ2GDE4]] $U_L$ on $\mathcal{H}_L$ such that:

1. $U_L$ is quasi-local: it maps an operator at one site to an operator whose part beyond distance $r$ has norm at most $C e^{-r/\xi}$;
2. the operators $\tau^z_i = U_L \sigma^z_i U_L^{*}$, for $i = 1, \dots, L$, commute with $H_L$;
3. $H_L$ has the form
$$H_L = \sum_i h_i \tau^z_i + \sum_{i < j} J_{ij} \tau^z_i \tau^z_j + \sum_{i < j < k} J_{ijk} \tau^z_i \tau^z_j \tau^z_k + \cdots,$$
where each coefficient of a product spread over a distance $r$ is at most $C e^{-r/\xi}$.

In clauses 1 and 3, the constants $C, \xi > 0$ do not depend on $L$.

## Remarks

The operators $\tau^z_i$ are called local integrals of motion, or l-bits.
Every eigenstate of $H_L$ is then a product state in the $\tau$ basis, so it has area-law entanglement, unlike a thermal eigenstate.
Example: take the random-field XX chain $H_L = \sum_i (\sigma^x_i \sigma^x_{i+1} + \sigma^y_i \sigma^y_{i+1}) + \sum_i h_i \sigma^z_i$.
The fields $h_i$ are independent and uniform in $[-W, W]$, with $W > 0$.
The [[Jordan–Wigner transformation|94PEKQHHHT]] maps it to free fermions with a random potential, which show [[Anderson localization|MXEZM0QJ1K]] in one dimension.
The occupation numbers of the exponentially localized orbitals are the l-bits, so the chain is localized in this sense, as a non-interacting case.
Non-example: the same chain with all $h_i = 0$ is translation invariant, its single-particle modes are plane waves, and a single flipped spin spreads ballistically along the chain.
Its natural conserved quantities, the mode occupations, are spread over the whole chain.
Its typical eigenstates have entanglement that grows with the size of a region, so they are not product states in any quasi-local basis, and the definition fails.
This definition follows the l-bit description of Serbyn, Papić and Abanin and of Huse, Nandkishore and Oganesyan.
Imbrie proved a version of it for a disordered interacting spin chain, under an assumption on the level statistics.
Whether MBL is stable in the thermodynamic limit, and in dimension above one, is still debated.
