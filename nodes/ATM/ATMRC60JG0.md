---
tag: ATMRC60JG0
kind: statement
role: proposition
name: Curie's principle
msc: [82C35, 80A17]
uses: [STR73R5MX4, FX3NEFYFFN, X4M2FFKQJ6, 0TKYAEJ8N7]
about: [STR73R5MX4]
sources:
  - url: https://en.wikipedia.org/wiki/Curie%27s_principle
---

## Statement

Consider a system that is isotropic, that is, invariant under all rotations and reflections of space.
Assume its fluxes depend linearly on the thermodynamic forces of its [[entropy production|STR73R5MX4]].
Split the fluxes and forces into irreducible parts under rotations: scalars, vectors, and traceless symmetric tensors of rank $2$, and so on.
Then a flux of one tensorial type depends only on the forces of the same type.
In particular, in an isotropic system a scalar force, such as a chemical affinity, cannot cause a vector flux, such as a heat flux.

## Remarks

The proof uses invariance: the coefficient that maps a force of one type to a flux of another type is a linear map that commutes with all rotations.
By [[Schur's lemma|X4M2FFKQJ6]] for the [[irreducible representations|FX3NEFYFFN]] of the [[orthogonal group|0TKYAEJ8N7]], such a map between different irreducible types is zero.
For instance, a linear map from scalars to vectors that commutes with rotations sends $1$ to a vector fixed by all rotations, which must be $0$.
Example: in an isotropic fluid, chemical reactions (scalars), heat conduction and diffusion (vectors), and viscous stress (rank $2$ tensors) form separate groups of coupled effects.
In an anisotropic crystal the hypothesis fails, and couplings between different types can occur.
This is the thermodynamic form of the general symmetry principle of Pierre Curie, that the symmetries of a cause are found in its effects.

## Explanations

### L1 human

In a substance that looks the same in every direction, a cause with no direction cannot produce an effect with a direction.
A chemical reaction has no preferred direction, so on its own it cannot push heat one way rather than another.
This removes many possible cross effects from the theory before any measurement.

### L2 human

Curie's principle and the Onsager relations together cut down the number of independent transport coefficients in linear irreversible thermodynamics.
In practice one first groups fluxes and forces by tensorial rank, then writes linear laws only inside each group.
The reduction is pure group theory: the isotropic tensors of each rank are known, and these are the only allowed coefficients.
