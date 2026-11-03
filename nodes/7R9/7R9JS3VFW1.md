---
tag: 7R9JS3VFW1
kind: definition
name: Quantum field theory
msc: [81T05, 81T08]
defines: W031YNVRE3
uses: [5QTZQV6TNG, HM2HHE3J51, 8ZQ9TA4Q2Q, 74BPYJNZTM, AES2T5JPFP]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_field_theory
---

## Definition

In the axiomatic (Wightman) sense, a *quantum field theory* of one real scalar field on four-dimensional Minkowski space is a quadruple $(\mathcal{H}, U, \Omega, \phi)$ where:

1. $\mathcal{H}$ is a separable complex [[Hilbert space|HM2HHE3J51]];
2. $U$ is a strongly continuous [[unitary representation|74BPYJNZTM]] of the identity component of the [[Poincaré group|8ZQ9TA4Q2Q]] on $\mathcal{H}$;
3. $\Omega \in \mathcal{H}$ is a unit vector, the vacuum;
4. $\phi$ assigns to each Schwartz function $f$ on $\R^4$ an operator $\phi(f)$, the smeared field.
These operators have a common dense domain, and $f \mapsto \phi(f)$ is an operator-valued [[tempered distribution|AES2T5JPFP]];

and these data satisfy the [[Wightman axioms|5QTZQV6TNG]].

## Remarks

Theories with several fields, with fields of nonzero spin, or in other dimensions $d \ge 2$ are defined in the same way.
Then $\phi$ is replaced by a finite family of fields that transform under a finite-dimensional representation of the Lorentz group.
Other axiom systems describe the same notion from other angles.
The [[Haag–Kastler axioms|MGBCX7FH2G]] use nets of operator algebras attached to regions of spacetime.
Euclidean axioms use correlation functions on $\R^d$.

Example: the free scalar field of mass $m > 0$ on the bosonic Fock space over $L^2$ of the mass hyperboloid $\set{p : p^2 = m^2,\ p^0 > 0}$ satisfies the definition.

Non-example: a field on that Fock space whose operators at spacelike separated points do not commute violates the locality axiom, so it is not a Wightman quantum field theory.

Interacting examples are known in two and three spacetime dimensions, constructed by the methods of constructive quantum field theory; in four dimensions none is known.
