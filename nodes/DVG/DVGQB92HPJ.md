---
tag: DVGQB92HPJ
kind: statement
role: theorem
name: Stone's theorem on one-parameter unitary groups
msc: [47D03, 47B25, 81Q10]
uses: [HM2HHE3J51, MM0EJ2GDE4, 0NEGN5CRSC, 18KPYRRPZY]
about: [MM0EJ2GDE4, 0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Stone%27s_theorem_on_one-parameter_unitary_groups
same_as:
  wikidata: Q4455030
  wikipedia: Stone's theorem on one-parameter unitary groups
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]].
Let $(U(t))_{t \in \R}$ be a family of [[unitary operators|MM0EJ2GDE4]] on $H$ such that:

1. $U(0) = I$ and $U(s + t) = U(s)U(t)$ for all $s, t \in \R$;
2. $t \mapsto U(t)x$ is continuous from $\R$ to $H$ for every $x \in H$.

Then there is a unique [[self-adjoint operator|0NEGN5CRSC]] $A$ on $H$ with $U(t) = e^{itA}$ for all $t \in \R$.
Its domain is the set of $x$ for which $\lim_{t \to 0} (U(t)x - x)/t$ exists, and $Ax = \lim_{t \to 0} (U(t)x - x)/(it)$.
Conversely, for every self-adjoint operator $A$ on $H$, the operators $e^{itA}$, defined by the [[spectral theorem|18KPYRRPZY]], satisfy clauses 1 and 2.

## Remarks

The converse is a direct consequence of the spectral theorem and dominated convergence.
For the main direction, $A$ is defined by the limit in the statement.
Vectors $\int \varphi(t) U(t)x \, dt$ with smooth compactly supported $\varphi$ lie in its domain, so $A$ is densely defined.
The group law shows that $A$ is symmetric, and the vectors $\int_0^\infty e^{-t} U(\pm t)x \, dt$ show that $A \pm iI$ are onto, which makes $A$ self-adjoint.

Example: on $L^2(\R)$, the translations $(U(t)f)(s) = f(s + t)$ form such a group.
Its generator is $A = -i \, d/ds$ with domain the Sobolev space $H^1(\R)$, the momentum operator of quantum mechanics.

Strong continuity in clause 2 is needed only in a weak form: on a separable Hilbert space, weak measurability of $t \mapsto \ip{U(t)x}{y}$ already implies it, by a theorem of von Neumann.

## Explanations

### L1 human

A one-parameter unitary group is a way of moving the vectors of a Hilbert space continuously in time without changing lengths.
Stone's theorem says that every such motion has the form $e^{itA}$ for one self-adjoint operator $A$.
In quantum mechanics, the motion is the time evolution of a state and $A$ is the energy, the Hamiltonian.
So the theorem explains why observables and symmetries correspond to self-adjoint operators.

### L2 human

The theorem is the unbounded counterpart of the fact that a continuous group of unitary matrices is $e^{itA}$ for a Hermitian matrix $A$.
It gives a bijection between self-adjoint operators and strongly continuous unitary groups.
It is the special case of semigroup theory where the semigroup extends to negative times and each operator is unitary; compare the [[Lumer–Phillips theorem|Z2N8MPD8DH]].
It is the starting point of the representation theory of $\R$, and with the SNAG theorem, of locally compact abelian groups.
