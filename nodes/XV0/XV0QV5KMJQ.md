---
tag: XV0QV5KMJQ
kind: statement
role: theorem
name: Classification of simple Lie superalgebras
msc: [17B20, 17B70]
uses: [7CZ4Q5H78N, XCN6HZ2GM9, T4S70DDW0A]
about: [7CZ4Q5H78N]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_superalgebra
---

## Statement

A [[Lie superalgebra|7CZ4Q5H78N]] $\mathfrak{g} = \mathfrak{g}_{\bar 0} \oplus \mathfrak{g}_{\bar 1}$ is *simple* if $\mathfrak{g}$ is not abelian and has no graded ideals other than $0$ and $\mathfrak{g}$.
Let $\mathfrak{g}$ be a finite-dimensional simple Lie superalgebra over $\C$ with $\mathfrak{g}_{\bar 1} \neq 0$.
Then $\mathfrak{g}$ is isomorphic to a member of one of the following families, for suitable values of the parameters:

1. the classical series $A(m, n)$, $B(m, n)$, $C(n)$ and $D(m, n)$, built from the special linear superalgebras $\mathfrak{sl}(m+1|n+1)$ and the orthosymplectic superalgebras $\mathfrak{osp}(p|2q)$;
2. the exceptional superalgebras $D(2, 1; \alpha)$, a one-parameter family, and $F(4)$ and $G(3)$;
3. the strange series $P(n)$ and $Q(n)$;
4. the Cartan type series $W(n)$, $S(n)$, $\widetilde{S}(n)$ and $H(n)$, built from superderivations of the exterior algebra in $n$ generators.

## Remarks

The theorem is due to Kac, in 1977.
The families in items 1 to 3 are the classical simple Lie superalgebras: those for which $\mathfrak{g}_{\bar 0}$ is a [[reductive Lie algebra|T4S70DDW0A]] acting completely reducibly on $\mathfrak{g}_{\bar 1}$.
The families in item 4 are the simple ones for which this fails.
The proof treats the two cases separately.
In the classical case it studies the representation of the reductive Lie algebra $\mathfrak{g}_{\bar 0}$ on $\mathfrak{g}_{\bar 1}$.
In the other case it studies a filtration of $\mathfrak{g}$ and its associated graded superalgebra.

Among the classical ones, the series $A$ to $D$ and the exceptional algebras carry a nondegenerate even invariant bilinear form, while $P(n)$ and $Q(n)$ do not.
For the algebras with such a form, there is a theory of root systems and Dynkin diagrams parallel to the [[classification of simple Lie algebras|XCN6HZ2GM9]].
A new feature is that a Lie superalgebra may have several inequivalent sets of simple roots.

## Explanations

### L1 human

Simple Lie superalgebras are the building blocks of Lie superalgebras, as simple Lie algebras are for Lie algebras.
Kac listed all finite-dimensional ones over the complex numbers.
Most come in infinite series built from matrices, like the series $A$, $B$, $C$, $D$ for Lie algebras.
There are also a few exceptional ones, two strange series with no counterpart for Lie algebras, and a group of series built from vector fields on spaces with odd coordinates.

### L2 human

The superalgebras $\mathfrak{sl}(m|n)$ and $\mathfrak{osp}(m|2n)$ are the direct analogues of the special linear and orthogonal or symplectic Lie algebras.
In the Cartan type series, $W(n)$ is the Lie superalgebra of all superderivations of the exterior algebra $\Lambda(n)$.
The series $S(n)$, $\widetilde{S}(n)$ and $H(n)$ are analogues of divergence-free and Hamiltonian vector fields.
Unlike the Lie algebra case, finite-dimensional representations of simple Lie superalgebras need not be completely reducible.
