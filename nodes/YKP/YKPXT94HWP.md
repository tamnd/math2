---
tag: YKPXT94HWP
kind: statement
role: theorem
name: Coleman–Mandula theorem
msc: [81T05, 81U20, 81R05]
uses: [YDC9XBJDE1, 8ZQ9TA4Q2Q, 7JBRGCVJRB, 5JJYBJ6A8K]
about: [YDC9XBJDE1]
sources:
  - url: https://en.wikipedia.org/wiki/Coleman%E2%80%93Mandula_theorem
same_as:
  wikidata: Q671663
  wikipedia: Coleman–Mandula theorem
---

## Statement

Let $G$ be a connected [[Lie group|7JBRGCVJRB]] of unitary symmetries of the [[S-matrix|YDC9XBJDE1]] of a relativistic quantum theory in four spacetime dimensions.
Assume the following.

1. Lorentz invariance: $G$ contains a subgroup locally isomorphic to the [[Poincaré group|8ZQ9TA4Q2Q]].
2. Particle finiteness: for every $M > 0$ there are only finitely many types of particles of mass less than $M$.
3. Weak elastic analyticity: elastic two-body scattering amplitudes are analytic functions of the Mandelstam variables $s$ and $t$ near the physical region, except at normal thresholds.
4. Occurrence of scattering: let $T = S - 1$ be the transition part of the S-matrix.
   For one-particle momenta $p$ and $p'$, the vector $T \lvert p, p' \rangle$ is nonzero, except perhaps at isolated values of $s$.
5. Technical assumption: the generators of $G$ act on one-particle states as integral operators in momentum space with distribution kernels.

Then $G$ is locally isomorphic to the direct product of the Poincaré group and an internal symmetry group.
The generators of the internal group commute with all Poincaré generators and act only on the particle type labels.
The [[Lie algebra|5JJYBJ6A8K]] of the internal group is the direct sum of a compact semisimple Lie algebra and an abelian Lie algebra.

## Remarks

The idea of the proof: a symmetry generator must act on two-particle states as a sum of its actions on the one-particle states.
If a generator acted nontrivially on momenta beyond the Poincaré generators, it would constrain elastic scattering so strongly that, with analyticity, the amplitude could be nonzero only at isolated angles.
This contradicts the occurrence of scattering.

The hypotheses matter.
If all particles are massless, the conformal group can appear as a symmetry.
If the symmetry generators may form a [[Lie superalgebra|7CZ4Q5H78N]] rather than a Lie algebra, supersymmetry becomes possible; this is the [[Haag–Łopuszański–Sohnius theorem|WKMW5H0GJZ]].
In two spacetime dimensions, integrable models have higher conserved charges but their scattering is purely elastic, so hypothesis 4 in its four-dimensional form does not apply.

## Explanations

### L1 human

Physicists once hoped to unite the symmetries of spacetime with internal symmetries, such as the flavour symmetry of quarks, into one bigger group.
The theorem shows that, for a theory with nontrivial scattering, the only possibility is a trivial product.
Spacetime symmetries and internal symmetries do not mix.

### L2 human

The theorem is a no-go result about the symmetries of the S-matrix.
It explains why internal symmetries such as gauge symmetry groups commute with Lorentz transformations, so that all particles of a multiplet have the same mass and spin.
Its loophole through graded Lie algebras led to [[supersymmetry|S847N922FY]], the only way to combine spacetime and internal symmetries nontrivially in four dimensions.
