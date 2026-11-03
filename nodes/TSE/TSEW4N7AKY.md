---
tag: TSEW4N7AKY
kind: definition
name: Martensitic transformation
msc: [74N10, 74N05, 74N15]
defines: EZRAMFGRZT
uses: [HTYRR2WDQ6, ZHK2EVRD90]
sources:
  - url: https://en.wikipedia.org/wiki/Diffusionless_transformation
---

## Definition

Let a crystalline solid have a high-temperature phase, the *austenite*, and a low-temperature phase, the *martensite*, and take the undistorted austenite as reference configuration.
Let $U \ne I$ be a symmetric positive definite $3 \times 3$ matrix, the *transformation stretch*, which maps the austenite lattice to the martensite lattice.
Let $\mathcal{P}$ be the group of rotations that leave the austenite lattice invariant.
The *variants* of martensite are the distinct matrices $U_1, \dots, U_N$ of the form $R U R^T$ with $R \in \mathcal{P}$.
A *martensitic transformation* is a first-order phase transformation from austenite to martensite such that:

1. no diffusion takes place, so each atom keeps its neighbours and the lattice change is a homogeneous [[deformation gradient|HTYRR2WDQ6]] of the lattice;
2. the point group of the martensite lattice is a proper subgroup of the point group of the austenite lattice;
3. the lattice deformation of each region is $Q U_i$ for some rotation $Q \in SO(3)$ and some variant $U_i$.

In the continuum model the free energy density $W(F, \theta)$ of a [[hyperelastic material|ZHK2EVRD90]] has minimizers $SO(3)$ above the transformation temperature and $\bigcup_i SO(3) U_i$ below it.

## Remarks

Example: in the cubic-to-tetragonal transformation, $U = \operatorname{diag}(\eta_2, \eta_1, \eta_1)$ with $\eta_1 \ne \eta_2$, and the cubic rotations produce the three variants $\operatorname{diag}(\eta_2, \eta_1, \eta_1)$, $\operatorname{diag}(\eta_1, \eta_2, \eta_1)$, $\operatorname{diag}(\eta_1, \eta_1, \eta_2)$, so $N = 3$.
Two variants can form a twin when $Q U_j - U_i = a \otimes n$ has a solution with $Q \in SO(3)$, so that the deformation is continuous across a plane with normal $n$.
Non-example: the precipitation of a new phase by diffusion of atoms in an alloy changes the composition locally and fails clause 1.
Non-example: melting is not a martensitic transformation, since the liquid has no lattice and fails clause 3.

## Explanations

### L1 human

In a martensitic transformation the crystal lattice is deformed into a less symmetric one by a uniform shift of all atoms, with no atom leaving its neighbours.
Because the lattice has several symmetric ways to do this, the new phase comes in several variants.
