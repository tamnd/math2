---
tag: Z877XDBMQ3
kind: statement
role: theorem
name: Stone–von Neumann theorem
msc: ["22E27", 81S05, "22E70"]
uses: [ZZYCV5EX9J, 74BPYJNZTM, HM2HHE3J51, MM0EJ2GDE4, 7KGF78FGEF]
about: [ZZYCV5EX9J]
sources:
  - url: https://en.wikipedia.org/wiki/Stone%E2%80%93von_Neumann_theorem
same_as:
  wikidata: Q7619449
  wikipedia: Stone–von Neumann theorem
---

## Statement

Let $n \ge 1$ and let $H$ be a [[Hilbert space|HM2HHE3J51]].
Let $U$ and $V$ be strongly continuous [[unitary representations|74BPYJNZTM]] of $\R^n$ on $H$ that satisfy the Weyl relations
$$U(s) V(t) = e^{i s \cdot t} \, V(t) U(s) \qquad (s, t \in \R^n).$$
Then $H$ is an orthogonal direct sum of closed subspaces, each invariant under all $U(s)$ and $V(t)$.
On each of them, the pair $(U, V)$ is unitarily equivalent to the Schrödinger pair on $L^2(\R^n)$:
$$(U_0(s) \psi)(x) = \psi(x + s), \qquad (V_0(t) \psi)(x) = e^{i t \cdot x} \psi(x).$$
In particular, every irreducible pair satisfying the Weyl relations is unitarily equivalent to $(U_0, V_0)$.

## Remarks

The pair $(U_0, V_0)$ satisfies the relations: $(U_0(s) V_0(t) \psi)(x) = e^{i t \cdot (x + s)} \psi(x + s) = e^{i s \cdot t} (V_0(t) U_0(s) \psi)(x)$.
The Weyl relations say that $(s, t, z) \mapsto z \, U(s) V(t)$ defines a unitary representation of the [[Heisenberg group|ZZYCV5EX9J]] in which the center acts by scalars.
So the theorem says: for each nontrivial character of the center, the Heisenberg group has exactly one irreducible unitary representation with that central character.
A standard proof considers the operators $\int\int f(s, t) U(s) V(t) \, ds \, dt$, finds a rank-one projection among them, and uses it to build an isometry onto $L^2(\R^n)$.
The exponentiated Weyl form is needed: there are self-adjoint operators $Q$ and $P$ that satisfy $[Q, P] = i$ on a common dense invariant domain but are not equivalent to the Schrödinger pair.
The finite number $n$ of degrees of freedom is also needed.
For infinitely many degrees of freedom there are many inequivalent irreducible representations, a basic phenomenon of quantum field theory.

## Explanations

### L1 human

In quantum mechanics, position and momentum do not commute.
The theorem says that once their commutation law is fixed, there is essentially only one way to realise them by operators.
So the wave mechanics of Schrödinger and the matrix mechanics of Heisenberg are two pictures of the same theory.

### L2 human

In representation theory the theorem classifies the infinite-dimensional irreducible unitary representations of the Heisenberg group.
It is the first case of the Kirillov orbit method, where these representations correspond to the planes in the dual of the Lie algebra.
Its uniqueness statement is what makes the oscillator representation of the metaplectic group possible: each symplectic map gives a second Schrödinger pair, hence an intertwining operator.
