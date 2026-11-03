---
tag: WZ81H3S4KK
kind: statement
role: theorem
name: Hurwitz's theorem on composition algebras
msc: [17A75, 17A35]
uses: [1Q9G6AST10, T9XW7RBEHY, ZWXW0T3EAC, KJ145M3CVT]
about: [1Q9G6AST10]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(composition_algebras)
same_as:
  wikidata: Q1139430
  wikipedia: Hurwitz's theorem (composition algebras)
---

## Statement

Let $K$ be a field of characteristic not $2$, and let $A$ be a [[composition algebra|1Q9G6AST10]] over $K$ with a unit.
Then $\dim_K A \in \set{1, 2, 4, 8}$, and:

1. if $\dim_K A = 1$, then $A = K$;
2. if $\dim_K A = 2$, then $A$ is commutative and associative;
3. if $\dim_K A = 4$, then $A$ is a [[quaternion algebra|ZWXW0T3EAC]], associative and not commutative;
4. if $\dim_K A = 8$, then $A$ is an [[octonion algebra|KJ145M3CVT]], alternative and not associative.

Each $A$ of dimension $2$, $4$ or $8$ is obtained from a unital composition algebra of half its dimension by the [[Cayley–Dickson construction|T9XW7RBEHY]].
In particular, for $K = \R$ and a positive definite norm, $A$ is isomorphic to $\R$, $\C$, the quaternions $\mathbb{H}$ or the octonions $\mathbb{O}$.

## Remarks

The idea of the proof: let $B$ be a proper unital subalgebra of $A$ on which the norm is nondegenerate.
Choose $v$ orthogonal to $B$ with $N(v) \neq 0$.
Then $B + Bv$ is a subalgebra of twice the dimension, isomorphic to the Cayley–Dickson double of $B$ with parameter $-N(v)$.
The double of $B$ is again a composition algebra only when $B$ is associative.
The double is associative only when $B$ is commutative and associative.
So the doubling from $K$ stops after at most three steps.
Example: over $\R$, the composition law for $\mathbb{H}$ gives Euler's four-square identity, and the one for $\mathbb{O}$ gives Degen's eight-square identity.

## Explanations

### L1 human

Ask for a way to multiply vectors such that the squared length of a product is the product of the squared lengths.
Hurwitz proved that this is possible only in dimensions $1$, $2$, $4$ and $8$.
Over the real numbers with ordinary length, the answers are the real numbers, the complex numbers, the quaternions and the octonions.

### L2 human

The theorem classifies the [[normed division algebras|DZ18QZHAMS]]: they are the composition algebras over $\R$ with a positive definite norm.
It also answers the question of Hurwitz about sum-of-squares identities: an identity $(x_1^2 + \cdots + x_n^2)(y_1^2 + \cdots + y_n^2) = z_1^2 + \cdots + z_n^2$ with each $z_k$ bilinear in $x$ and $y$ exists only for $n = 1, 2, 4, 8$.
Over $\R$, $\C$ and finite fields, the classification becomes a classification of quadratic forms, since the algebra is determined by its norm.
