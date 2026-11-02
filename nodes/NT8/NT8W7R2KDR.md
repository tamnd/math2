---
tag: NT8W7R2KDR
kind: statement
role: theorem
name: Reiterman's theorem
msc: ["08B99", "20M07"]
uses: [XR4DPKX7T1, KBXSZC6BV1, PKD440G2XW]
about: [XR4DPKX7T1]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Statement

Let $\sigma$ be a finite algebraic signature and let $\mathcal{F}$ be the class of all finite $\sigma$-algebras.
For $n \ge 1$, an *$n$-ary implicit operation* $\pi$ assigns to each $A \in \mathcal{F}$ a map $\pi_A \colon A^n \to A$, subject to one condition.
For every [[homomorphism|KBXSZC6BV1]] $f \colon A \to B$ in $\mathcal{F}$ and all $a_1, \ldots, a_n \in A$, it requires $f(\pi_A(a_1, \ldots, a_n)) = \pi_B(f(a_1), \ldots, f(a_n))$.
A *pseudoidentity* is a pair $\pi \approx \rho$ of $n$-ary implicit operations, and $A \in \mathcal{F}$ satisfies it if $\pi_A = \rho_A$.
Let $V \subseteq \mathcal{F}$.
Then $V$ is a [[pseudovariety|XR4DPKX7T1]] if and only if there is a set $\Sigma$ of pseudoidentities with the following property.
An algebra $A \in \mathcal{F}$ is in $V$ exactly when it satisfies every member of $\Sigma$.

## Remarks

Each term gives an implicit operation, so every [[identity|PKD440G2XW]] is a pseudoidentity, but there are many more.
The $n$-ary implicit operations are the elements of the free profinite $\sigma$-algebra on $n$ generators, the inverse limit of all $n$-generated finite $\sigma$-algebras.
The easy direction holds because satisfaction of a pseudoidentity passes to quotients, subalgebras and finite products.
For the converse, one takes as $\Sigma$ all pseudoidentities true in $V$.
A finite algebra $A$ satisfying them is a continuous image of a free pro-$V$ algebra.
By compactness this map factors through a finite quotient of it that lies in $V$, so $A \in V$.

Example: in finite semigroups, each element $x$ has a unique idempotent power, written $x^\omega$; it is the limit of $x^{n!}$, and $x \mapsto x^\omega$ is a unary implicit operation.
The pseudovariety of finite groups is defined by $x^\omega y \approx y$ and $y x^\omega \approx y$.
The pseudovariety of finite aperiodic semigroups is defined by $x^\omega \approx x^{\omega + 1}$.
Neither class is the class of finite members of a variety of semigroups, so ordinary identities do not suffice.

## Explanations

### L1 human

Birkhoff's theorem says that classes of algebras closed under the usual constructions are exactly those defined by equations.
For finite algebras the equations are not enough.
Reiterman showed that they become enough once one allows "limit" operations, such as taking the idempotent power of an element, which make sense in every finite algebra.

### L2 human

The theorem is the finite counterpart of [[Birkhoff's HSP theorem|5083DHSK82]].
It is a basic tool in the algebraic theory of regular languages: through Eilenberg's correspondence, a class of regular languages is described by pseudoidentities of its syntactic monoids.
Decidability questions for pseudovarieties then become questions about the free profinite semigroup or monoid.
An earlier description, due to Eilenberg and Schützenberger, defines each pseudovariety by a sequence of identities that is eventually satisfied.
