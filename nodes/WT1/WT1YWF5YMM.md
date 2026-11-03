---
tag: WT1YWF5YMM
kind: statement
role: theorem
name: Stability of matter
msc: [81V70, 81Q10, 35P15]
uses: [VXDEQB46GV, Y64G7W4BEC, ZQGC326NP7, 572QKEYYKX]
about: [VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Stability_of_matter
same_as:
  wikidata: Q112968598
  wikipedia: Stability of matter
---

## Statement

Let $Z > 0$.
Consider $N$ electrons at positions $x_1, \ldots, x_N \in \R^3$.
Consider $K$ fixed nuclei at distinct positions $R_1, \ldots, R_K \in \R^3$ with charges $0 < Z_k \le Z$.
In atomic units, let
$$H = -\frac12 \sum_{i=1}^{N} \Delta_i - \sum_{i=1}^{N} \sum_{k=1}^{K} \frac{Z_k}{\abs{x_i - R_k}} + \sum_{1 \le i < j \le N} \frac{1}{\abs{x_i - x_j}} + \sum_{1 \le k < l \le K} \frac{Z_k Z_l}{\abs{R_k - R_l}}$$
act on the functions of $L^2((\R^3 \times \set{\uparrow, \downarrow})^N)$ that are antisymmetric in the electrons.
Then there is a constant $C$ depending only on $Z$ such that
$$H \ge -C\,(N + K)$$
for all $N$, $K$ and all positions $R_1, \ldots, R_K$.

## Remarks

The lower bound is linear in the number of particles; this is stability of the second kind, as opposed to the mere finiteness of the ground state energy.
Dyson and Lenard proved it in 1967; Lieb and Thirring gave a much shorter proof in 1975.
Their proof bounds the kinetic energy of fermions from below by $c\int \rho^{5/3}$ through the [[Lieb–Thirring inequality|572QKEYYKX]].
This reduces the problem to a Thomas–Fermi type energy, and Thomas–Fermi theory has no binding.

The antisymmetry ([[Pauli exclusion principle|ZQGC326NP7]]) is necessary.
If the same operator acts on all functions, as for bosonic electrons, the infimum of the energy decreases faster than linearly in the number of particles.

Example: for a single hydrogen atom ($N = K = 1$, $Z = 1$) the sharp bound is $H \ge -\frac12$, the ground state energy.
The theorem says that the energy of a mole of hydrogen is at least a fixed negative constant times the number of atoms.

## Explanations

### L1 human

Ordinary matter is made of positive nuclei and negative electrons, attracting each other with forces that become infinite at short distances.
The theorem says that the energy per particle is still bounded below, so a large piece of matter does not collapse.
Its energy is at least a fixed negative constant times its size.
The key reason is the Pauli principle: electrons cannot crowd into the same state.

### L2 human

Stability of the first kind, that one atom has finite ground state energy, follows from the uncertainty principle, for instance via Hardy's inequality.
Stability of the second kind needs the Pauli principle and the screening of charges, and the Lieb–Thirring approach makes both precise.
The bound is what makes thermodynamics of Coulomb systems possible: it is the first step towards the existence of the thermodynamic limit of the free energy per particle.
